# SBI_DWSSFP

This respository provides example code used to perform parameter estimation from DW-SSFP data using simulation based inference (SBI). The code is implemented in Python using the SBI toolbox. 

# Overview
A key challenge of parameter estimation from DW-SSFP data arises from its sophisticated signal model and complicated signal dependences on $T_1$, $T_2$ & $B_1$. Simulation based inference provides an approach to perform rapid estimation of voxelwise posterior distributions. Recent work has demonstrated the potential of SBI with diffusion MRI data [(1)](https://doi.org/10.1101/2024.11.19.624267), [(2)](https://doi.org/10.7554/eLife.101069.2), [(3)](https://doi.org/10.1101/2024.11.11.622925). Here, I provide an example implementation, trained for a diffusion tensor representation with DW-SSFP. 

# Key features
The proposed implementation addresses the challenge of signal dependencies ($T_1$, $T_2$ & $B_1$) by characterising the posterior distribution as conditional on their values - i.e. $P(\theta | S, T_1, T_2, B_1)$, where $P$ is the posterior distribution, $\theta$ represents the parameters to be estimated, and $S$ is experimental data. This means that a single trained network can account for differences in relaxation values and spatial variation in flip angle. The network can additionally account for experimental data with varying levels of SNR, using a similar approach to [(1)](https://doi.org/10.1101/2024.11.19.624267). 

# Findings
When considering a diffusion tensor, an SBI network trained on a personal laptop over a weekend (31 hours) is able to achieve equivalent accurary to conventional non-linear least-squares (NLLS) methods (see below figure), whilst providing full information about the posterior distribution in a reduced estimation time.

# Navigating the software
The provided software consists of two main pieces of code for training and inference. Training.ipynb defines and trains the SBI network for DW-SSFP data. Inference.ipynb utilises the network to perform parameter estimation from experimental DW-SSFP data. Current implementation is based on two flip angle DW-SSFP data (as described in [(4)](https://doi.org/10.1016/j.neuroimage.2020.117113)), but can be modified for other acquisition protocols. Note that training time and accuracy is strongly dependent on the number of simulations performed, and can be edited in the software (_number_of_simulations_).

# Required Packages
sbi, numpy, nibabel, interruptingcow

# Example comparison
The below figure displays an principal diffusion direction (FA modulated) map estimated from experimental post-mortem DW-SSFP data. Excellent agreement is found between NLLS and SBI
![Comparison of a Tensor estimated using NLLS and SBI methods in a human post-mortem brain](https://github.com/BenjaminTendler/SBI_DWSSFP/blob/main/NLLS_SBI.png)
