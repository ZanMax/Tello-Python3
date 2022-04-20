#!/bin/bash
WIFI_NAME="TELLO-F11671"
networksetup -setairportnetwork en0 $WIFI_NAME
echo "Connected to $WIFI_NAME"
sleep 8
echo "Activating VENV"
source venv/bin/activate
echo "Starting APP"
python3 main.py
