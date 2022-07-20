# The Space-x Challenge
A bridge between the developers team and management team, it is an proposal solution for the challenge 
https://doc.clickup.com/p/h/e12h-16043/f3e54f9ffd37f57/e12h-16043

## About the software solution
it is an API based on FastApi

## How to run the project

This project is able to run by 2 ways, using docker or run from the localhost with python

For both option the iniatial steps are: 

a. Clone the project from github

`
git clone git@github.com:g3r4benitez/spaceX.git
`

b. Create a configuration file: 

`cp .env.example .env`


**Trello Board**
This board is used to receive all task created with this project, this is a public board
https://trello.com/invite/b/Dn8U4JwH/8848416402fe7c94c0c5e80023cee919/welcome-board


### Option 1: 

#### Requirements
Docker and Docker-compose

#### Steps to run the project 
1. Clone Project
2. run the command: 
    Docker-compose up
3. make request against  the localhost in the port 8000

Example 1: 

`
curl --location --request POST 'http://0.0.0.0:8000/tasks' \
--header 'Content-Type: application/json' \
--data-raw '{
    "type": "issue", 
    "title": "Send Message", 
    "description": "Let pilots send messages to Central"
}'
`

4. Also you can try the API using the documentation by Swagger UI, try it in [http://localhost:8000/docs](http://localhost:8000/docs)


### Option 2: VirtualEnv + Local

#### Requirements
Python 3.9+

#### Installation
Install the required packages in your local environment (ideally virtualenv, conda, etc.).

```sh
pip install -r requirements.txt
```

#### Setup
1. Duplicate the `.env.example` file and rename it to `.env`
2. Ask a teammate for the .env file

#### Project

#### Run It

1. Start your app with:

```sh
python3 -m uvicorn app.main:app --reload --port 8000
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).
   Here you can try the api using the documentation provided by Swagger UI

3. Make requests
Example: 

`
curl --location --request POST 'http://0.0.0.0:8000/tasks' \
--header 'Content-Type: application/json' \
--data-raw '{
    "type": "issue", 
    "title": "Send Message", 
    "description": "Let pilots send messages to Central"
}'
`