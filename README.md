# myRetailService

# Case-Study-Challenge
![Workflow](https://github.com/sujithshajee/myRetailService/actions/workflows/test.yml/badge.svg)
![Docker Image CI](https://github.com/sujithshajee/myRetailService/workflows/Docker%20Image%20CI/badge.svg)

##Description

myRetail is a rapidly growing company with HQ in Richmond, VA and over 200 stores across the east coast. 
myRetail wants to make its internal data available to any number of client devices, from myRetail.com to native mobile apps.

- Goal
  - Create an end-to-end Proof-of-Concept for a products API, which will aggregate product data from multiple sources and return it as JSON to the caller. 
  - Create a RESTful service that can retrieve product and price details by ID. 

- Build an application that performs the following actions:
  - Responds to an HTTP GET request at /products/{id} and delivers product data as JSON (where {id} will be a number. 
  - Example product IDs: 
    - 13860428
    - 54456119
    - 13264003
    - 12954218

-   Example response:
```json
{
   "id":13860428,
   "name":"The Big Lebowski (Blu-ray) (Widescreen)",
   "current_price":{
      "value":13.49,
      "currency_code":"USD"
   }
}
``` 

  - Performs an HTTP GET to retrieve the product name from an external API.
  - External api example: https://redsky.target.com/redsky_aggregations/v1/redsky/case_study_v1?key=3yUxt7WltYG7MFKPp7uyELi1K40ad2ys&tcin=13860428
  - Reads pricing information from a NoSQL data store and combines it with the product id and name from the HTTP request into a single response. 
  - BONUS: Accepts an HTTP PUT request at the same path (/products/{id}), containing a JSON request body similar to the GET response, and updates the product’s price in the data store.


## Requirements
```python
pip install -r requirements.txt
```


## Requirements for Coverage and Lint
```python
pip install coverage
pip install pylint
```

## Run Tests
```python
 python -m unittest discover
```

## Run Tests with Coverage and Generate Report
```python
coverage run -m unittest
coverage report -m
coverage html
```

## Build image using docker
```
docker build -t case-study-challenge .
```

## Build and run using docker-compose
```
docker-compose up
```