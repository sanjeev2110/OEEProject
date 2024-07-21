# Use the official Python Docker image as the base image
FROM python:3.9-slim

# Install the paho-mqtt package
RUN pip install paho-mqtt

# Copy the Python script to the container
COPY mqtttest.py /app/mqtttest.py

# Run the Python script
CMD ["python", "/app/mqtttest.py"]
