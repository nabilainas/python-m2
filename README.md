# Health Calculator Service

## Description
Health Calculator Service is a web application that allows users to calculate their Body Mass Index (BMI) and Basal Metabolic Rate (BMR). The application is built using Flask and Docker, and it includes a CI/CD pipeline for automated testing and deployment.

## Features
- Calculate BMI based on weight and height.
- Calculate BMR based on weight, height, age, and gender.
- Responsive web interface for user interaction.

## Project Structure
```
/health-calculator-service
|-- app.py
|-- health_utils.py
|-- templates
|   |-- index.html
|-- static
|   |-- css
|   |   |-- styles.css
|   |-- js
|       |-- scripts.js
|-- test.py
|-- requirements.txt
|-- Dockerfile
|-- Makefile
/.github
|-- workflows
|   |-- ci-cd.yml
.gitignore
README.md
```

## Getting Started

### Prerequisites
- Python 3.9
- Docker
- Azure account (for deployment)

### Installation
1. Clone the repository:
  ```sh
  git clone https://github.com/yourusername/health-calculator-service.git
  cd health-calculator-service
  ```

2. Set up a virtual environment and install dependencies:
  ```sh
  make setenv
  source .env/bin/activate
  make init
  ```

3. Run the application locally:
  ```sh
  make local
  ```

4. Open your browser and navigate to `http://localhost:5000`.

### Running Tests
To run the tests locally:
```sh
make test
```

### Docker
To build and run the Docker container:
```sh
make build
make run
```

To stop and remove the Docker container:
```sh
make stop
```

To push the Docker image to Azure Container Registry:
```sh
make push
```

### CI/CD Pipeline
The CI/CD pipeline is configured using GitHub Actions. It includes steps for testing, building, and deploying the application to Azure App Service.


## Acknowledgements
- Flask
- Docker
- GitHub Actions
- Azure
