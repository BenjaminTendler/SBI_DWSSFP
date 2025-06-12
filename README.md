# SBI_DWSSFP

This repository provides software associated with ongoing work integrating Neural Posterior Estimation (NPE) with DW-SSFP. The software is subject to change at any moment whilst the project is under development. For any questions, please email benjamin.tendler@ndcn.ox.ac.uk.

# Overview
This repository contains example software to:
- Train a NPE network to characterise the DW-SSFP signal under a Tensor representation (BuildNPENetwork.ipynb)
- Estimate Tensor coefficients from DW-SSFP data using an NPE network (NPE_ParameterEstimation.ipynb) or Non Linear Least Squares (NLLS) (NLLS_ParameterEstimation.ipynb)
- A Trained NPE network (Posterior.pkl)
- Example data (DW-SSFP & and dependency maps downsampled to 9 mm isotropic resolution; supporting text files).

# Required Packages
- Software written in Python (3.12.8) using the SBI Toolbox (0.23.3)
- Created using numpy (1.26.4), scipy (1.12.0), pytorch (2.5.1) and nibabel (5.3.2) integrated into Jupyter notebooks.
