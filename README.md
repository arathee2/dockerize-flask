# dockerize-tic-tac-toe
An implementation of Tic-tac-toe in Python containerized using Docker.

# Steps to Dockerize a simple Flask app
```bash
# 1. Create files for project scaffolding
touch requirements.txt
touch Makefile
touch Dockerfile
touch ttt.py

# 2. Build Docker image
docker build --tag=tic-tac-toe .

# 3. Look at local Docker images
docker image ls

# 4. Run Flask app using local image
docker run -it tic-tac-toe python3 ttt.py

# 5. Push image to DockerHub
docker login
dockerpath="arathee2/tic-tac-toe"                  # DockerHub repository address
docker image tag tic-tac-toe $dockerpath           # tag image
docker image push $dockerpath                      # push image

# 6. Pull image
docker pull arathee2/tic-tac-toe

# 7. Run Flask app using remote DockerHub image
docker run -it arathee2/tic-tac-toe python3 ttt.py
```