# ANZ Technical Test v3

Containerised Python application with a single /version endpoint.

## Getting Started 

### Prerequisites
- [Docker](https://www.docker.com/)

## Running the application
Docker build & run:
```
./start.sh
```

## Stopping the application
Docker stop & rm:
```
./stop.sh
```

## Running the tests
Pytest:
```
pytest
```

## Deploying the application
The docker image can be deployed on container-orchestration tools like [Kubernetes](https://docs.docker.com/get-started/kube-deploy/).

## CI
Using [GitHub Actions](https://github.com/marketplace?type=actions&query=python) changes on the master branch triggers
lint check with [Flake8](https://flake8.pycqa.org/en/latest/) run unit tests with [Pytest](https://docs.pytest.org/en/stable/)

## Implementation decisions

Language: Python was chosen because of its familiarity comparing to Go and NodeJS.

CI: GitHub Actions was chosen because it is already integrated with GitHub (the specified repository) and contains 
python pipelines already to use as a base.

Versioning: The versioning of the application was at first hard-coded, then through more reading it was externalized and
set at build time. In that way, the CI tool can set the correct application version before deployment.  


## Known risks

- The implemented approach of getting parameters from an ENVIRONMENT variable
can be troublesome as the variable can be malicious overwritten at runtime.