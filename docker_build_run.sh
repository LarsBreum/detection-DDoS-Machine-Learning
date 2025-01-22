#!/bin/bash

# Build the Docker image
docker build -t pandas-env:latest .

# Run the Docker container
docker run -it pandas-env
