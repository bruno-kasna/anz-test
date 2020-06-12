# ANZ Technical Test v3

Containerised Python application with a single `/version` endpoint that returns the last commit sha and app version.

Example:
```
GET /version
```


Response
```
{
   "myapplication":[
      {
         "description":"pre-interview technical test",
         "lastcommitsha":"66c57edb29e3d3cefe29cea878ebb0697e82efd2",
         "version":"1.0.0"
      }
   ]
}
```

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

For that, Kubernetes manifests were created to deploy the application in a cluster.

Assuming that credentials and cluster are already set up, run the command to deploy:

```
./deploy.sh
```

## CI
The CI was created using [GitHub Actions](https://github.com/marketplace?type=actions&query=python). The pipeline is
triggered by changes on any branch or pull-requests. It run the lint check with [Flake8](https://flake8.pycqa.org/en/latest/)
and unit tests execution with [Pytest](https://docs.pytest.org/en/stable/).

## Implementation decisions

**Language:** Python was chosen because of its familiarity comparing to Go and NodeJS.

**CI:** GitHub Actions was chosen because it is already integrated with GitHub (the specified repository) and already contains 
python pipelines to use as example.

**Versioning:** The versioning of the application was at first hard-coded, then through more reading it was externalized and
set at build time. In that way, the CI tool can set the correct version before deploying the application.  

## Known risks

- The implemented approach of getting parameters from an ENVIRONMENT variable
can be troublesome as the variable can be malicious overwritten at runtime.