# Jupyter-Chart
![img](assets/jup,k8s.png)

## This repository includes ```Helm Chart``` for deploying Jupyter Lab on K8s.

### Image
- There are two separate Dockerfile for both ```CPU``` and ```GPU``` usage.
- The ```python``` version is ```3.10.12``` for ```Cuda``` and ```3.12``` for ```CPU```.
- The minimum version of ```Cuda``` should be ```11.7```.

### Build step
Use ```make build-cpu``` or ```make build-cuda``` to build image.

### Deploy
Use ```make deploy-jupyter``` to deploy in on ```k8s```.
