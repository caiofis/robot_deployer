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

### Demo:
https://youtu.be/88bWkjUvrhE


### File descriptions:

* **docker/Dockerfile:** Dockerfile describing the system configs
* **docker/build.sh:** Script for building the docker image
* **docker/run.sh:** Script for run the application
* **__init__.py:** Python script that orchestrate that application
* **main.py:** Python script that deals with get and post requests, including file uploading
* **auth.py:** Python script responsible for the user authentication
* **models.py:** Python script with the data abstraction object (DAO) for accessing the database
* **db.sqlite:** SQLite3 database with the user table
* **templates/base.html:** HMTL file describing the base for the other templates
* **templates/index.html:** Main page
* **templates/login.html:** Login page
* **templates/profile.html:** Welcome page
* **templates/signup.html:** Signup page
* **templates/uoload.html:** File upload page
