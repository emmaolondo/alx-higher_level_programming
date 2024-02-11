#!/bin/bash
# Scripts that sends a GET request with a header variable X-School-User-Id with value 98
curl -sL -X GET -H "X-School-User-Id: 98" "$1"
