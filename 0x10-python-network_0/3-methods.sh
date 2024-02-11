#!/bin/bash
# Script that displays all HHTP methods the server will accept
curl -sILX OPTIONS "$1" | grep -i 'Allow' | cut -f2- -d' '
