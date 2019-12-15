# byrd backend developer task

### Project Setup
* [Install python3](https://www.python.org/downloads/)
* Clone project
* Open the terminal and navigate to the cloned path
* `cd` to the project and make sure you are on the same level as `manage.py` file
* execute `python3 -m venv path_to_project/venv` (i.e. path_to_project: cloned folder path)
* execute `source venv/bin/activate`
* execute `pip3 install -r requirements.txt`
* execute `python3 manage.py migrate`
* execute `python3 manage.py runserver`

### Endpoints
Open the browser and navigate to `http://127.0.0.1:8000/api/`

#### SKU Endpoints:
* http://127.0.0.1:8000/api/sku/help
* http://127.0.0.1:8000/api/sku

[Post Call] To create an sku, paste the following json to the content section and click post button

`
{
    "product_name": "Apple"
}
`

[Post Call] To update an sku, paste the following json to the content section and click post button

`
{
    "id": 1,
    "product_name": "Apple"
}
`

[Delete Call] To delete an sku, navigate to following url and click delete button
`http://127.0.0.1:8000/api/sku/?id=1`

#### Storage Endpoints:
* http://127.0.0.1:8000/api/storage/help
* http://127.0.0.1:8000/api/storage

[Post Call] To create a storage, paste the following json to the content section and click post button

`
{
    "quantity": 5,
    "sku": 1
}
`

[Post Call] To update a storage, paste the following json to the content section and click post button

`
{
    "id": 1
    "quantity": 5,
    "sku": 1
}
`

[Delete Call] To delete a store, navigate to following url and click delete button
`http://127.0.0.1:8000/api/store/?id=1`


#### Order Endpoints:
* http://127.0.0.1:8000/api/order/help
* http://127.0.0.1:8000/api/order
* http://127.0.0.1:8000/api/order/q=Thomas

[Post Call] To create an order, paste the following json to the content section and click post button

`
{
    "customer_name": "Thomas Müller",
    "lines": [
        {
            "sku": 1,
            "quantity": 3
        }
    ]
}
`
