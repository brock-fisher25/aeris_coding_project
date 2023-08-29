Repository for coding project assigned by Aeris LLC

Introduction

Welcome to the documentation of the Aeris Coding Project. This documentation will help you understand exactly what the Aeris Coding Project is and how to get it up and running with using Docker.
The project uses a given list of data points that have x, y, z, and concentration values. The concentration is a measurement of how dense something is at the given point in space.
The project introduces an API featuring four endpoints, each designed to provide distinct data measures on the concentration. The endpoints are get-mean, get-sum, get-std-deviation, and get-image.
Flask is used to define and create the API and endpoints within it.
Docker is used to package/deploy the project as a Docker Image to other users.

How to run the Docker Image:

- This project uses a Docker Image to deploy, so make sure you have Docker installed on your PC.
- If you do not have Docker installed on your PC, visit this link for installation instructions https://docs.docker.com/engine/install/
- Download this entire repository
- Run the program using Docker with the command:
  docker run --publish 5000:5000 aeris_coding_project //check to make sure this is correct command
- Please note, that inside the program, it is specified to run on container port 5000. If that port is taken up by your PC with another task, please map another port to the 5000 port.
- For example, if port 5000 is unavailable on your local PC, try running it on port 8000 with the following command:
  docker run --publish 8000:5000 aeris_coding_project //check to make sure this is correct command
- Once you have successfully began running the docker image, the API should be working on your localhost. Test each endpoint mentioned above, and they all should return the desired information.
