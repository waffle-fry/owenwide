# Owenwide

_Banking, for every Owen._

The project consists of an incredibly basic Python API, which uses Flask.

## Prerequisites

This project requires the installation of Python version 3, and the libraries required to run the API.

There is a devcontainer, which can be used with VSCode.

To install the libraries, run:

`pip install -r requirements.txt`

## The Setup

This project has been structured across three files:

`owenwide.py` contains all of the "logic". This is a shared library file that is referenced elsewhere, enabling us to implement the API in different ways.

`api.py` contains the API implementation - this will serve the complete API, making it available in the browser.

`customers_lambda.py` is our first Lambda implementation for our customers functionality/endpoint.

## The API

We have three endpoints:

/health - returns "ok" if the API is running
/customers - returns a (hard-coded, for the moment) list of Owenwide's customers
/account_balances - returns a (also hard-coded) list of balances for all customers

## Running

The API can be run with:

`python api.py`

It should then be availble at [http://127.0.0.1:5000](http://127.0.0.1:5000) (though the output will list the correct address if it is different).

## Testing

There is a suite of unit tests for `api.py`:

`python -m unittest test_api.py`


## Tasks

Each task will reside in its own `README.md` file in a numbered folder.
