build-cpu:
	docker build -t jupyterhub-cpu -f Dockerfile.cpu .

build-cuda:
	docker build -t jupyterhub-cuda -f Dockerfile.cuda .

deploy-jupyter:
	helm upgrade jupyter deployments -i --values ./deployments/values.yaml
