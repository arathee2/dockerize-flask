dockerpath="arathee2/tic-tac-toe"

# tag image
docker image tag app $dockerpath

# push image
docker image push $dockerpath
