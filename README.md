# Learn Blockchains by Building One

[![Build Status](https://travis-ci.org/dvf/blockchain.svg?branch=master)](https://travis-ci.org/dvf/blockchain)

This is the source code for my post on [Building a Blockchain](https://medium.com/p/117428612f46). 

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install [pipenv](https://github.com/kennethreitz/pipenv). 

```
$ pip install pipenv 
```

3. Create a _virtual environment_ and specify the Python version to use. 

```
$ pipenv --python=python3.6
```

4. Install requirements.  

```
$ pipenv install 
``` 

5. Run the server:
    * `$ pipenv run python blockchain.py` 
    * `$ pipenv run python blockchain.py -p 5001`
    * `$ pipenv run python blockchain.py --port 5002`
    
## Parameters

    '-p', '--port', default=5000, type=int, help='port to listen on'
    '-k', '--kwport', default=55554, type=int, help='port keyworker to listen on'
    '-i', '--ip', default='127.0.0.1', help='ip keyworker to listen on'
    '-d', '--db', default='', help='db file, if not passed, then no persistance'
    '-v', '--variant', default='s', help='variant of blockchain s or q, where s-SimpleBlockChain, q-QuatuBlockChain'

