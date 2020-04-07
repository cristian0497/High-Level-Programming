#!/bin/bash
# Display the size of the body of the response
curl -s -o/dev/null 0.0.0.0:5000 -w '%{size_download}'
