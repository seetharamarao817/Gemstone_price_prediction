# Autodbconnect
============
Autodbconnect is a Python package that provides a simple and efficient way to connect with MongoDB databases. It includes a few classes and functions that allow you to easily create, manage, and interact with MongoDB databases and collections.
Installation
------------
You can install autodbconnect using pip:
```
pip install autodbconnect
```
Features
--------
* **MongoClient**: A class that represents a MongoDB client. It takes a URL parameter and returns a MongoDB client object.
* **MongoDatabase**: A class that represents a MongoDB database. It takes a client object and a database name parameter and returns a MongoDB database object.
* **MongoCollection**: A class that represents a MongoDB collection. It takes a database object and a collection name parameter and returns a MongoDB collection object.
* **insert_record**: A function that inserts a record into a MongoDB collection. It takes a record parameter, which can be a dictionary or a list of dictionaries, and a collection name parameter.
* **bulk_insert**: A function that inserts multiple records into a MongoDB collection. It takes a data file path parameter and a collection name parameter.
Usage
-----
Here's an example of how to use autodbconnect to insert a record into a MongoDB collection:
```python
from autodbconnect import MongoClient
client = MongoClient('mongodb://localhost:27017/')
database = client['mydatabase']
collection = database['mycollection']
record = {'name': 'John', 'age': 30}
collection.insert_one(record)
```
This code creates a MongoDB client object, creates a database object, creates a collection object, and inserts a record into the collection.
Contributing
------------
Contributions are welcome! If you'd like to contribute to autodbconnect, please open a pull request with your proposed changes.
License
-------
Autodbconnect is licensed under the MIT license. See the LICENSE file for more information.
Acknowledgments
---------------
Thanks to MongoDB for their excellent documentation and resources, which were invaluable in the development of this package.