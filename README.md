# Setu Assignment

## API to figure out encryption and checksum and create 2 APIs, a bill fetch API and bill pay API which will hit given url and fetch data 

## Requirements
The requirements.txt file should list all Python libraries that is required to run the app

pip install -r requirements.txt

## Instructions to run the App

run python app.py (Running on http://127.0.0.1:5000/)

## Fetch API
http://127.0.0.1:5000/setu/fetch

payload
{
    "loan_number": "BAS123JKE"
}

## Pay API
http://127.0.0.1:5000/setu/pay

payload
{
    "loan_number": "BAS123JKE"
}
