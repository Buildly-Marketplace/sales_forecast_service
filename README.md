# sales forecast service
This project predicts sales based on collected data.


## Installation 
Clone the repository
- `git clone https://github.com/Buildly-Marketplace/sales_forecast_service.git`

Install the required dependencies
> See [requirements.txt](requirements.txt)

## Usage
Run 

`python3 model.py` 

to generate the serialized model in `.pkl` format.

## Endpoints in app.py
`/dataset`  
Submitting a GET request to this endpoint will return the dataset used to train the model.

`/results`
Submitting a POST request to this endpoint will return the predicted amount of sales.

Example request body:
`{"rate":5, "sales_in_first_month":200, "sales_in_second_month":400}`

## TODOs
- [ ] Create a docker file.
