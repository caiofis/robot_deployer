# robot_deployer 🤖
This is my final project for CS50. It is a web application running flask that allows you to upload a tar.gz file to the server.

Working as a robotics engineer for autonomous agricultural machines I frequently have to deploy some upgrades on robots operating on locations without internet. 
With this application, I can send the new software to the operator, who can easily upload it using his smartphone. On the startup the robot looks for the earliest 
file on this particular folder and update itself if a new software version is available.

### Usage:
Since it is running on Docker you just have to run: 
``` bash
./docker/run.sh
```
