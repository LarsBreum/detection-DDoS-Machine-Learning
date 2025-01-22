# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container
COPY requirements.txt /app/requirements.txt

# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the Python script into the container
COPY app /app/
# Copy the data files into the container
COPY data /app/data

# Command to run the specific Python script
CMD ["python3", "/app/data_preproc.py"]