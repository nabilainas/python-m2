IMAGE_NAME = nabilainas.azurecr.io/health-metrics
CONTAINER_NAME = health-metrics-container


setenv:
	python -m venv .env
	source .env/bin/activate

init:
	@echo "Creating virtual environment..."
	pip install --upgrade pip
	pip install -r requirements.txt

local:
	@echo "Running the application locally..."
	python health-calculator-service/app.py

test:
	@echo "Running the tests locally..."
	python health-calculator-service/test.py

build:
	@echo "Building docker image..."
	docker build -t $(IMAGE_NAME) .

push:
	@echo "Pushing docker image..."
	docker push $(IMAGE_NAME)

run:
	@echo "Running the docker container..."
	docker run -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	@echo "Stopping the docker container..."
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

clean:
	@echo "Removing docker image..."
	docker rmi $(IMAGE_NAME)
