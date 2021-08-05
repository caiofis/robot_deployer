#!/bin/bash
docker run -it --rm --volume="$(pwd):/home/robot_deployer" --net=host robot_deployer bash
