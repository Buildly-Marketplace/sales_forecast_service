# Sales Forecast Service
Predict sales based on collected data.

## Prerequisites
Clone the repository, install the requirements, then run
`python model.py`
to generate the serialized model in `.pkl` format. 

## Endpoints
- `/dataset`  
    - Submitting a GET request to this endpoint will return the dataset used to train the model.

- `/results`
    - Submitting a POST request to this endpoint will return the predicted amount of sales.

## Examples
- Sample request body:
```json
{"rate": 5, "sales_in_first_month": 200, "sales_in_second_month": 400}
```
