### Powerplant power 
This app uses the flask python framework and a virtual environment, to run the powerplant app is required to install '''requirements.txt''' and recomended to do it in a virtual environment. 
#### To run the App
Is required to install Docker or other container manager.
**build the image with:**
    `docker build powerplant:codechallenge .`
**then run the container exposing the port 8888:**
    `docker run -dp 127.0.0.1:80:8888 powerplant:codechallenge`
Once the container is runing just execute the `client.py`
this software will POST the json payload to the containerized server.

Thank You :)