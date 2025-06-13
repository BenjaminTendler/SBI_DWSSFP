# SBI_DWSSFP

This repository provides software associated with ongoing work integrating Neural Posterior Estimation (NPE) with Diffusion-Weighted Steady-State Free precession (DW-SSFP) for parameter estimation. The software is subject to change at any moment whilst the project is under development. For any questions, please email benjamin.tendler@ndcn.ox.ac.uk.

# Overview
This repository contains example software to:
- Train a NPE network to characterise the DW-SSFP signal under a Tensor representation (_BuildNPENetwork.ipynb_)
- Estimate Tensor coefficients from DW-SSFP data using an NPE network (_NPE_ParameterEstimation.ipynb_) or Non Linear Least Squares (NLLS) (_NLLS_ParameterEstimation.ipynb_)
- A Trained NPE network (_Posterior.pkl_)
- Example data (DW-SSFP & and dependency maps downsampled to 9 mm isotropic resolution + supporting text files).

# Required Packages
- Software written in _Python_ (3.12.8) using the _SBI Toolbox_ (0.23.3)
- Created using _NumPy_ (1.26.4), _SciPy_ (1.12.0), _PyTorch_ (2.5.1) and _NiBabel_ (5.3.2), integrated into _Jupyter_ notebooks.

# Example

The below figure displays an example V1 map (FA-modulated) estimated using NPE from experimental DW-SSFP data acquired in a post-mortem human brain (0.85 mm isotropic resolution). 

![Example V1 map (FA-modulated) estimated using NPE from experimental DW-SSFP data acquired in a post-mortem human brain (0.85 mm isotropic resolution)](https://github.com/BenjaminTendler/SBI_DWSSFP/blob/main/NPE_ExampleImage.png)

