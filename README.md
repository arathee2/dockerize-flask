# dockerize-flask
A simple Flask app containerized using Docker.

# Steps to Dockerize a simple Flask app
```python
# 1. Create files for project scaffolding: requirements.txt, Makefile, Dockerfile, and app.py
touch requirements.txt
touch Makefile
touch Dockerfile
touch app.py

# 2. Build Docker image
docker build --tag=app .

# 3. Look at local Docker images
docker image ls

# 4. Run Flask app using local image
docker run -it app python app.py --name "Amandeep"

# 5. Push image to DockerHub
docker login
dockerpath="arathee2/flask-hello-world"    # DockerHub repository address
docker image tag app $dockerpath           # tag image
docker image push $dockerpath              # push image

# 6. Pull image
docker pull arathee2/flask-hello-world

# 7. Run Flask app using remote DockerHub image
docker run -it arathee2/flask-hello-world python app.py --name "Amandeep"