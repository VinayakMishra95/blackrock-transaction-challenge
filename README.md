# Blackrock Transaction Challenge API

This project provides a REST API built with FastAPI to handle financial transaction processing and validation.

## Features

- Transaction Builder: Receives raw expense data and enriches it with a calculated 'ceiling' (rounded up to the nearest 100) and the 'remanent' investment amount.
- Transaction Validator: Processes a list of enriched transactions and a wage value to separate valid transactions from invalid ones (e.g., flagging negative amounts).

## Technical Stack

- Python: Core programming language.
- FastAPI: Web framework used for the API endpoints.
- Pydantic: Used for strict data validation and schema definitions.
- Uvicorn: ASGI server to run the application locally.

## Installation

1. Clone the project:
   git clone https://github.com/VinayakMishra95/blackrock-transaction-challenge.git
   cd blackrock-transaction-challenge

2. Set up Virtual Environment:
   python -m venv venv
   .\venv\Scripts\activate

3. Install Requirements:
   pip install -r requirements.txt

## How to Run

Start the server using the following command in your terminal:
uvicorn main:app --reload

Once started, the interactive API documentation (Swagger UI) can be accessed at:
http://127.0.0.1:8000/docs

## API Endpoints

1. Parse Transactions
- Endpoint: /blackrock/challenge/v1/transactions:parse
- Method: POST
- Description: Takes a list of dates and amounts to calculate investment ceilings.

2. Validate Transactions
- Endpoint: /blackrock/challenge/v1/transactions:validator
- Method: POST
- Description: Validates transactions based on specific business rules like negative amount checks.