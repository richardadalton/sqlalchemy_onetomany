
# Flask SQLAlchemy One-To-Many Demo

This is a demo of creating a Postgres database with two tables, Users and Messages and a One-To-Many relationship between the two.

## Installation
Clone the repo then install dependencies 

$ sudo pip3 install -r requirements.txt

## Provision a Postgres database.

In heroku, create a new application, go to resources and 
provision a postgres database.

The URL for the database will be available in the config_vars 
section of the application's settings page.

Insert the Postgres DB URL into the trysqlal.py file on line 5

## Run and Create Database
Run the python 3 shell

$ python3

Create the database

>>> from trysqlal import db
>>> db.create_all()

This should create the database tables in the postgres db

## Create a User and Message (Method 1)

>>> from trysqlal import User
>>> from trysqlal import Message
>>> u1 = User(username='user1', email='user1@example.com') 
>>> m1 = Message(content='Hello World', author=u1)
>>> db.session.add(m1)
>>> db.session.commit()

## Create a User and Message (Method 2)
This may work better if creating a number of child entries for the 
same user.

>>> from trysqlal import User
>>> from trysqlal import Message
>>> u2 = User(username='user2', email='user2@example.com')
>>> m2 = Message(content='Hello World 2')
>>> u2.messages.add(m2)
>>> u2.messages.append(m2)
>>> db.session.commit()



