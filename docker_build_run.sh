#!/bin/bash

# Build the Docker image
docker build -t pandas-env:latest .

# Run the Docker container
docker run -v ./app/out_data:/app/out_data -v ./app/7_classes:/app/7_classes pandas-env:latest

