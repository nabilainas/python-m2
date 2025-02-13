# Variables
IMAGE_NAME = health-metrics
CONTAINER_NAME = health-metrics-container

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop the Docker container
stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

# Push the Docker image to Docker Hub (optional)
push:
	docker push $(IMAGE_NAME)

# Cleanup Docker images
clean:
	docker rmi $(IMAGE_NAME)
