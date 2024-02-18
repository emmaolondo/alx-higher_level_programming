#!/bin/bash
# Display status code
curl -L -s -X HEAD -w "%{http_code}" "$1"
