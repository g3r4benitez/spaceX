# Forward-Export-API
An API to export some data from Forward like demographic, documents, income, utility, rent, etc.   

## Requirements

Python 3.9+

## Installation
Install the required packages in your local environment (ideally virtualenv, conda, etc.).

```sh
pip install -r requirements.txt
```

## Setup
1. Duplicate the `.env.example` file and rename it to `.env`
2. Ask a teammate for the .env file

## Postgres
1. run this query: 
CREATE EXTENSION IF NOT EXISTS tablefunc;


## Project

### Run It

1. Start your app with:

```sh
python3 -m uvicorn app.main:app --reload --port 9009
```

2. Go to [http://localhost:9009/docs](http://localhost:8000/docs).

### Launch Rabbit locally
```sh
docker-compose up rabbit
```


### Launch Rabbit Worker 
Using with virtual environment activated
```sh
celery -A app.core.celery_worker worker --loglevel=info
```


