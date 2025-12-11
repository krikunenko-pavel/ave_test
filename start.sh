#!/usr/bin/bash

echo "Start PhoneAddressService..."
docker compose -f deployment/docker-compose.yml up --build
