# FARM-Demo

![BlaBlaConf](https://uploads-ssl.webflow.com/6138df4b2a63f4613fb7fb42/6138fb95d8f448dacbf64936_logo.svg)

This code is an example FARM (FastAPI, React, MongoDB) project that implements a simple TODO List system.

The FARM stack is FastAPI, React, and MongoDB. It is a simpler form of the MERN stack that can make developing apps even faster. You will learn how to connect this with a mongoDB database. Then you will learn to connect the backend to the frontend. A React app will send and receive HTTP requests to and from the server.

## Configuration

Before Configure the FARM project, you need to install:

- Python 3.6 or higher [Python](https://www.python.org/downloads/). (What is recommended for a FastAPI project)
- MongoDB [MongoDB](https://www.mongodb.com/download-center/community/).

### Backend

- After Providing Python in your computer, you need to create your own [virtual environment](https://docs.python.org/3/tutorial/venv.html), don't forget to switch to the project directory `/backend`:

```shell
# creating virtual environment
$ virtualenv venv

# activate virtual environment
$ source venv/bin/activate

# install all dependencies
$ pip install -r requirements.txt
```

- You'll need to set the following environment variables before running the project:

```bash
    # The following will work on Linux & OSX:
    export MONGODB_URI = "mongodb://localhost:27017"
```

- Run the code with the following command:

```bash
uvicorn main:app --reload --port 8000
```

### Frontend

- Here we need to install all dependencies by running the following command:

```bash
    # I use here the `yarn` command, you can use `npm` instead.
    yarn install
```

- Then we need to run the following command to start the frontend:

```bash
    # start the frontend part
    npm run start
```
