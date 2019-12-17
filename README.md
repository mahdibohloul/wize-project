# wize-project
A site for wize company

# Introduction
  I designed a site for wize analaystics compony that they want me to do for second step of their interview and also for my resume and also i will compelete it for my resume  

# Technologies 
   * Python 3.6.9
   * Django 3.0
   * Postgres 3.0.0
   * HTML5
   
  This site is based on Python and Django and the database that we used on it is Postgres that we chose because of this reasons:
  
  postgres is faster than MYSQL in calling field and rows, Also in data analysis topic it is faster and more effective because of its structure and facilities and it's worth mentioning that Postgre also supports many NoSQL features as well.
  
 
 
# Lunch
  After clone the project into your drive for work with it, follow the following instructions:
  (The requirments.txt is in the project folder)
  
  $ cd wize_project
  
  $ virtualenv venv
  
  $ source venv/bin/activate
  
  $ pip install -r requirments.txt
  
  * Create wize_project database in your Postgres server
  
  $ python manage.py makemigrations
  
  $ python manage.py migrate
  
  $ python manage.py runserver
  
# The Content Of The Project
  In this project we have 4 apps:
  Accounts, Office, Notifications, Task
  
  Accounts app include the databse off the all the users and we keep all of them in it.
  
  The job of the Notifications app is to sending messages from a user to another.
  The model of Notifications app is related to Accounts and Office model.
  
  In Office app  have names of the companies that registered by admin.
  Also Office model is related to Task, Accounts and Notifications model.
  
  In the Task app we define task and duty for user who works in the specific office.
  
  
  
 # For Wize
  سلام و ممنون بابت وقتی که گذاشتید, پروژه یک سری نواقص داره که متاسفانه فرصت تکمیل نبود با عرض پوزش و بازم ممنون بابت وقتی که میگذارید.
