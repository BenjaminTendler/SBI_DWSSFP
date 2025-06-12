import numpy as np
import nibabel as nib

class read_in:
    def __init__(self,DataPath):
        self.data=np.asanyarray(nib.load(DataPath).dataobj)
        self.aff=nib.load(DataPath).affine


def ImportDataDWSSFP(DataPath):
    Data = read_in(''.join([DataPath,'/data.nii.gz']))
    T1 = read_in(''.join([DataPath,'/T1map.nii.gz']))
    T2 = read_in(''.join([DataPath,'/T2map.nii.gz']))
    B1 = read_in(''.join([DataPath,'/B1map.nii.gz']))
    mask = read_in(''.join([DataPath,'/nodif_brain_mask.nii.gz']))
    noisefloor = np.loadtxt(''.join([DataPath,'/noisefloor']))
    bvecs = np.loadtxt(''.join([DataPath,'/bvecs']))
    FlipAngles = np.loadtxt(''.join([DataPath,'/flipAngles']))
    tau = np.loadtxt(''.join([DataPath,'/DiffGradDurs']))
    G = np.loadtxt(''.join([DataPath,'/DiffGradAmps']))
    TRs = np.loadtxt(''.join([DataPath,'/TRs']))
    b0s = np.loadtxt(''.join([DataPath,'/b0s']))
    return Data, T1, T2, B1, mask, noisefloor, bvecs, FlipAngles, tau, G, TRs, b0s

def ImportTextDataDWSSFP(DataPath):
    bvecs = np.loadtxt(''.join([DataPath,'/bvecs']))
    FlipAngles = np.loadtxt(''.join([DataPath,'/flipAngles']))
    tau = np.loadtxt(''.join([DataPath,'/DiffGradDurs']))
    G = np.loadtxt(''.join([DataPath,'/DiffGradAmps']))
    TRs = np.loadtxt(''.join([DataPath,'/TRs']))
    b0s = np.loadtxt(''.join([DataPath,'/b0s']))
    return bvecs, FlipAngles, tau, G, TRs, b0s
    
    
