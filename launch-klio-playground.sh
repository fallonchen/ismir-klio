#!/bin/bash

docker run -e HOME=$(pwd) --workdir=$(pwd)  \
           -v /var/run/docker.sock:/var/run/docker.sock \
           --mount type=bind,source=$(pwd),target=$(pwd) \
           -it \
           --rm docker.io/fallon/ismir-klio 
