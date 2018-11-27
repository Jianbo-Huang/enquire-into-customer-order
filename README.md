# enquire-into-customer-order
Client-server interaction of large dateset using Numpy and Flask


# Purpose

The purpse of this small project  is to use a list as a storage for customer orders, and the client
makes various of enquiries into this order list. The idea to do this is to illustrate
some software engineering techniques for handling large lists, for client-server
interaction and  for writing 'clean', easily extensible code using Python, Flask and
Numpy.

This design is readily useable when the list is filled with data from a database.

The package Numpy is chosen as it is an efficient and reliable package
for doing statistics, linear algebra on large arrays.

# Requirement

Python3 (Python 3.5.2 is used for doing the test)
Flask
Numpy

The task is implemented in Linux Ubuntu 16.04. If Flask or
Numpy is not in your system, just type

pip3 install flask
pip3 install numpy

# Design consideration

The task uses Flask as web framework.

For simple tasks like this one, Flask is a better choice. For complex tasks involving
user authentication,  database models etc, Django is a better choice, as Django
has a comprehensive build-in module for handling database IO

# Coding structure

Coding structure in Flask framework is very simple: a single  Python startup script file is usually
enough to implement a project of moderate complexity. Different functionalities of a project
can be handled by separate html files which provide  REST API to communicate between clients
and the server. Django's structure is much more complex, involving multiple files and sub-directories
for models, views and url lists. For relatively simple tasks, using Flask is more productive.

# Functionality list

The code in this task implements the following functionalities:
     total sum of all elements in a list
     total customer orders (suppose the list stores the customer orders)
     average customer orders 
     maximum customer orders
     a list of top 10 orders (this can be customised easily for top N orders, where N is a parameter the client specified)
     a list of customer id with top 10 orders (this can be customised easily for top N orders, where N is a parameter 
     the client specified)
     Number of customers with order >= a given value
Note:
    In all the above, the list is very large (10 million elements), so the structure is useful
    for handling real-world  data sets.

    Due to the above consideration, Python loops are not used to handle the list operations, as it
    will be very slow to loop over large range in Python. The internal functions are used
    to handle the list operations.

    Other functionalities involving list operations, such as statistics, data ploting, data mining etc,
    can be implemented in the same fasion. For data ploting, the matplotlib is highly recommended.
     
# Tests

All the functionalities implemented in this task are tested throughly. The math
operations are  build-in Python or Numpy functions, which are throughly tested. This greatly
reduces the efforts for implementation tasting.

# Run the code

Assume you are using Linux OS, and have Python3 installed as python3 (instead of python),
under a Linux terminal, change your working directory to the one which contains
this README.md file, then just type:

./start.py

You need to change permision to executable (e.g. chmod 755 start.py)

Alternatively, you may type:

python  start.py

# JSON objects

The Json object format is popular in webservice. To show the use of Json, I delibrately
included it. For this  task, use of Jason is not necessary. To turn a dictionaly object
into a string, using str(dictionary) is sufficient.
