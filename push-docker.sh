dockerpath="arathee2/flask-hello-world"

# tag image
docker image tag app $dockerpath

# push image
docker image push $dockerpath