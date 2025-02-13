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
	docker build -t $(IMAGE_NAME) .

push:
	docker push $(IMAGE_NAME)

run:
	docker run -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

push:
	docker push $(IMAGE_NAME)

clean:
	docker rmi $(IMAGE_NAME)
