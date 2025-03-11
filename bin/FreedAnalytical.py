##
#Define required libraries
import numpy as np
import torch

##
#Pulsed Gradient Freed
def FreedDWSSFP(G, tau, TR, alpha, D, T1, T2):

    # Code calculates steady-state magnetization with diffusion weighting for monopolar diffusion gradient based on the Freed model.
    #
    # input:
    #	G   = strength of diffusion gradient (mT/m)
    #	tau = duration of diffusion gradient (ms)
    #	TR  = repetition time (ms)
    #	alpha = flip angle (degrees)
    #	D   = diffusion coefficient (mm2/s)
    #	T1  = longitudinal relaxation time (ms)
    #	T2  = transverse relaxation time (ms)
    #
    # output:
    #	S = Measured signal

    ##
    #Define parameters
    gamma = 4258*2*np.pi;      # Hz/G
    T1 = T1*10**-3;          # Convert to s
    T2 = T2*10**-3;          # Convert to s
    G = G*10**-1;            # Convert to G/mm
    alpha = alpha*np.pi/180;   # Convert to radians

    ##
    #Implementation based on Freed et al: Steady-state free precession experiments and exact treatment of diffusion in a uniform gradient J. Chem. Phys. 115, 4249 (2001); https://doi.org/10.1063/1.1389859
    cosa=np.cos(alpha)
    sina=np.sin(alpha)

    def E1p(p):
        return np.exp(-TR/T1-D*gamma**2*G**2*tau**2*TR*p**2)
    
    def E2p(p):
        return np.exp(-TR/T2-D*gamma**2*G**2*tau**2*((p**2+p+1/3)*(tau)+(p+1)**2*(TR-tau)))
    
    def Ap(p):
        return 1/2*(E1p(p)-1)*(1+cosa)
    
    def Bp(p):
        return 1/2*(E1p(p)+1)*(1-cosa)
    
    def Cp(p):
        return(E1p(p)-cosa)
    
    def np_(p):
        return -E2p(-p)*E2p(p-1)*(Ap(p)**2)*Bp(p-1)/Bp(p)
    
    def dp(p):
        return (Ap(p)-Bp(p))+E2p(-p-1)*E2p(p)*Bp(p)*Cp(p+1)/Bp(p+1)
    
    def ep(p):
        return -E2p(p)*E2p(-p-1)*Bp(p)*Cp(p+1)/Bp(p+1)

    ##
    #Perform Recursive Operation
    x1 = 0
    for k in range(10,0,-1):
        if k==1000:
            x1=np_(k)/(dp(k)+ep(k))
        else:
            x1=np_(k)/(dp(k)+x1)

    ##
    ##Estimate r1
    r1=x1/(E2p(-1)*Bp(0))+(E2p(0)*Cp(1))/Bp(1)
    
    ##
    #Calculate Signal
    S=r1*sina*(1-E1p(0))*E2p(-1)/(Ap(0)-Bp(0)+E2p(-1)*Cp(0)*r1)

    return np.abs(S)

##
#Pulsed Gradient Freed + Tensor
def FreedDWSSFPTensor(G, tau, TR, alpha, T1, T2, bvecs, Dxx, Dyy, Dzz, Dxy, Dxz, Dyz):

    ##
    #Estimate ADC associated with Diffusion Tensor & Each Gradient Orientation
    ADC=bvecs[0,:]**2*Dxx+bvecs[1,:]**2*Dyy+bvecs[2,:]**2*Dzz+2*bvecs[0,:]*bvecs[1,:]*Dxy+2*bvecs[0,:]*bvecs[2,:]*Dxz+2*bvecs[1,:]*bvecs[2,:]*Dyz

    ##
    #Calculate Signal
    S=FreedDWSSFP(G,tau,TR,alpha,ADC,T1,T2)

    return S


def FreedDWSSFPTensor_Conditional(theta, G, tau, TR, alpha, bvecs, B1, T1, T2):
    
    ##
    #Expand Tensor & SNR Estimate
    Dxx, Dyy, Dzz, Dxy, Dxz, Dyz = theta

    ##
    #Perform Eigenvalue Decomposition
    DTensor = np.array([[Dxx,Dxy,Dxz],[Dxy,Dyy,Dyz],[Dxz,Dyz,Dzz]])
    eigenvalues, eigenvectors = np.linalg.eig(DTensor)
    
    ##
    #Assign B1 to modify flip angle
    alpha_B1=alpha*B1

    ##
    #Ignore simulation if any eigenvalue less than zero (aka invalid parameter region)
    if np.any(eigenvalues<0):
        #Set equal to nan
        S=np.ones(G.shape)*np.nan
    else:
        #Calculate Signal
        S=FreedDWSSFPTensor(G,tau,TR,alpha_B1,T1,T2,bvecs,Dxx,Dyy,Dzz,Dxy,Dxz,Dyz)

    return np.concatenate((S,[B1/100],[T1/100000],[T2/10000]))


def FreedDWSSFPTensor_Conditional_SBIWrapper(theta, G, tau, TR, alpha, bvecs):

    ##
    #Convert theta into 1D array
    theta = np.squeeze(np.asarray(theta))

    ##
    #Define B1 & Relaxation Times
    B1 = np.random.uniform(0.2,1.2)
    T1 = np.random.uniform(300,1200)
    T2 = np.random.uniform(20,80)

    ##
    #Run Signal Estimation
    S = FreedDWSSFPTensor_Conditional(theta,G,tau,TR,alpha,bvecs, B1, T1, T2)

    ##
    #Output as torch array
    return torch.from_numpy(S[np.newaxis,:]).type(torch.float32)

