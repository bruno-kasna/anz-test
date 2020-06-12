#!/bin/bash
app="myapp"
version=1
last_commit=`git rev-parse HEAD`
docker build -t ${app}:latest --build-arg VERSION=${version} --build-arg LAST_COMMIT_SHA=${last_commit} .
docker run -p 5000:5000 --name=${app} ${app}