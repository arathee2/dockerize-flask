# Tic-tac-toe

A text-based implementation of Tic-tac-toe that can be played in command line. To play the game, install [Docker](https://docs.docker.com/get-docker/) and run the following command:

`docker run -it arathee2/tic-tac-toe python3 ttt.py`

# How to Dockerize a simple Python project.

Here is how I Dockerized this project.

```bash
# 1. Create your project along with Dockerfile and Makefile. For this project I created the following files.
touch requirements.txt
touch Makefile
touch Dockerfile
touch ttt.py

# 2. Build Docker image
docker build --tag=tic-tac-toe .

# 3. Ensure that image is built by looking at all local Docker images
docker image ls

# 4. Run ttt.py app using local image
docker run -it tic-tac-toe python3 ttt.py

# 5. Push image to DockerHub
docker login
dockerpath="arathee2/tic-tac-toe"                  # DockerHub repository address
docker image tag tic-tac-toe $dockerpath           # tag image
docker image push $dockerpath                      # push image

# 6. Pull image
docker pull arathee2/tic-tac-toe

# 7. Run ttt.py using remote DockerHub image
docker run -it arathee2/tic-tac-toe python3 ttt.py
```
