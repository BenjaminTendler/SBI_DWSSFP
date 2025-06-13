# SBI_DWSSFP

This repository provides software associated with ongoing work integrating Neural Posterior Estimation (NPE) with Diffusion-Weighted Steady-State Free precession (DW-SSFP) for parameter estimation. The software is subject to change at any moment whilst the project is under development. For any questions, please email benjamin.tendler@ndcn.ox.ac.uk.

# Overview
This repository contains example software to:
- Train a NPE network to characterise the DW-SSFP signal under a Tensor representation (_BuildNPENetwork.ipynb_)
- Estimate Tensor coefficients from DW-SSFP data using an NPE network (_NPE_ParameterEstimation.ipynb_) or Non Linear Least Squares (NLLS) (_NLLS_ParameterEstimation.ipynb_)
- A Trained NPE network (_Posterior.pkl_)
- Example data (DW-SSFP & and dependency maps downsampled to 9 mm isotropic resolution + supporting text files).

# Required Packages
- Software written in Python (3.12.8) using the SBI Toolbox (0.23.3)
- Created using NumPy (1.26.4), SciPy (1.12.0), PyTorch (2.5.1) and NiBabel (5.3.2), integrated into Jupyter notebooks.

# Example

The below figure displays an example V1 map (FA-modulated) estimated using NPE from experimental DW-SSFP data acquired in a post-mortem human brain (0.85 mm isotropic resolution). 

![Example V1 map (FA-modulated) estimated using NPE from experimental DW-SSFP data acquired in a post-mortem human brain (0.85 mm isotropic resolution)](https://github.com/BenjaminTendler/SBI_DWSSFP/blob/main/NPE_ExampleImage.png)

