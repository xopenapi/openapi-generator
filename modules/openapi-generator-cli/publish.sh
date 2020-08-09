#!/bin/sh

docker build -t xopenapi/openapi-generator-cli .
docker tag xopenapi/openapi-generator-cli:latest xopenapi/openapi-generator-cli:latest
docker push xopenapi/openapi-generator-cli
