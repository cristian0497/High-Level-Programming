#!/bin/bash
# All Options methods
curl -Is -X OPTIONS $1 | grep Allow | sed "s/Allow: //"
