#!/bin/bash
app="myapp"
docker stop ${app}
docker rm ${app}