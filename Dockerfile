# Use the official Node-RED Docker image as the base image
FROM nodered/node-red:latest

# Copy Node-RED configuration files
COPY package.json /data/package.json
COPY flows.json /data/flows.json

# Install Node-RED packages
RUN npm install --unsafe-perm --no-update-notifier --no-fund --only=production
