#!/bin/bash
#takes in a url, sends a request to the url and display the size
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
