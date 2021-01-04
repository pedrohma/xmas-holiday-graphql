# xmas-holiday-graphql

## Installation

1. Run the command to setup the enviroment:<br/>
``python -m venv xmas-env``

2. Let's activate the virtual enviroment by clicking in:<br/>
``xmas-env\Scripts\activate.bat``

3. Let's install the following packages:<br/>
``pip install flask ariadne flask-sqlalchemy``

## Setting up the API

#### Populating the database
Open a **new** `python` terminal and run the commands from [scripts.txt](database/scripts.txt)

#### Defining the FLASK_APP
```python
$env:FLASK_APP = "main.py"
```

#### Running the API locally
```python
python -m flask run
```

Access the local application at http://127.0.0.1:5000/graphql

## Exploring GraphQL Functions
1. Open the file [queries](graphql/queries.graphql) to see how to retrieve data using the GraphQL Queries.
2. Open the file [mutations](graphql/mutations.graphql) to see how to post data using the GraphQL Mutations.

## Useful Links

1. https://graphql.org/learn/
2. https://www.howtographql.com/graphql-python/0-introduction/
3. https://flask.palletsprojects.com/en/1.1.x/
4. https://ariadnegraphql.org/
5. https://flask-sqlalchemy.palletsprojects.com/en/2.x/
