#!/bin/bash
#takes in a URL,sends a GET request to the URL,output the body of the response
curl -sX GET "$1" "X-School-User-Id: 98"-L
