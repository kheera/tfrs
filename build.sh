#!/usr/bin/bash
docker stop -t0 test
docker rm test
docker build -t tfrs .
docker ps
