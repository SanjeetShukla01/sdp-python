#!/bin/bash

python backend-servers.py &
# Get the PID of the background process
PID=$!
echo "PID is:" $PID
# Wait for 10 seconds
sleep 5
# Start the load balancer
python load-balancer.py
# Optionally, wait for the background process to complete
wait $PID