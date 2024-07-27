# This dockerfile  is just to show that the test scripts in the test directory work on a container. Not sure if we'll develop with it or not.

# Use the official Ubuntu base image
FROM ubuntu:20.04

# Set environment variables to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-pyqt5 \
    libxkbcommon-x11-0 \
    libgl1-mesa-glx \
    x11-apps \
    && apt-get clean

# Set the working directory in the container
WORKDIR /usr/src/app

COPY requirements.txt .

# Install Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

#Attempt to fix a bug
#RUN pip3 uninstall opencv-python && \
    #pip install opencv-python-headless

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Command to run the Python script
CMD ["python3", "test/main.py"]


