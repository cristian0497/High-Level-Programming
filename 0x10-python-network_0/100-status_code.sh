#!/bin/bash
# olnly Code Status
curl -I -s -w "%{http_code}" "$1" -o /dev/null
