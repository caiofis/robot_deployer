#!/bin/bash
docker run -it --rm --volume="$(pwd):/home/" --net=host robot_deployer bash
