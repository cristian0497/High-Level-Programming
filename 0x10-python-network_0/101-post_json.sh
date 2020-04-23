#!/bin/bash
# POST method json
curl -s -X POST -H "Content-Type: application/json" --data @"$2" "$1"
