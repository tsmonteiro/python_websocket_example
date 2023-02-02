# Simple Python Websocket Example

This projects contains a simple client-server websocket architecture implemented in python. 

A client makes a dummy requests and receives a `pandas` data frame in response. Data is carried over as binary json. 

## Installation

Create a virtual environment and activate it
```bash
virtualenv .venv
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Starting the server

```bash
python3 server.py
```

Then make the request
```bash
python3 client.py
```