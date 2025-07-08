# SBI_DWSSFP

This repository provides software associated with the manuscript "Integration of steady-state diffusion MRI with Neural Posterior Estimation (NPE) for post-mortem investigations". The software is subject to change at any moment whilst the project is under development. For any questions, please email benjamin.tendler@ndcn.ox.ac.uk.

# Overview
This repository contains software to:
- Train a NPE network to characterise the DW-SSFP signal under a Tensor representation (_BuildNPENetwork.ipynb_)
- Estimate Tensor coefficients from DW-SSFP data using an NPE network (_NPE_ParameterEstimation.ipynb_) or Non Linear Least Squares (NLLS) (_NLLS_ParameterEstimation.ipynb_)
- A Trained NPE network (_Posterior.pkl_) based on the acquisition protocol described in the manuscript
- Example data based on the acquisition protocol described in the manuscript (DW-SSFP & dependency maps downsampled to 9 mm isotropic resolution + supporting text files)
- Scripts to recreate many of the figures in the manuscript (_Figures_)

# Required Packages
- Software written in _Python_ (3.12.8) using the _SBI Toolbox_ (0.23.3)
- Created using _NumPy_ (1.26.4), _SciPy_ (1.12.0), _PyTorch_ (2.5.1) and _NiBabel_ (5.3.2), integrated into _Jupyter_ notebooks
- Installation can be performed via Conda using _conda create -n "SBI_DWSSFP" python=3.12.8 sbi=0.23.3 nibabel=5.3.2 pytorch=2.5.1 scipy=1.12.0 numpy=1.26.4_

# Example

The below figure displays an example V1 map (FA-modulated) estimated using NPE from experimental DW-SSFP data acquired in a post-mortem human brain (0.85 mm isotropic resolution). 

![Example V1 map (FA-modulated) estimated using NPE from experimental DW-SSFP data acquired in a post-mortem human brain (0.85 mm isotropic resolution)](https://github.com/BenjaminTendler/SBI_DWSSFP/blob/main/NPE_ExampleImage.png)

