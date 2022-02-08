# Django with mongoDB
This POC is an example of authentication apis with mongodb as Database.

This POC uses token authentication.  <br>
Create Abstract user for user model. <br>
Uses Djongo to connect between Django and mongodb.
  
# Prerequisites
You will need the following programmes properly installed on your computer.<br>
Python 3.7+

# Installation and Running

clone the repository
```
git clone https://github.com/ongraphpythondev/DRF_auth_with_mongodb.git
cd DRF_auth_with_mongodb
```
create a vertual environment
```
python -m venv .venv
.venv/bin/activate.bat

install django rest framework
```
pip install djangorestframework
```
install required packages
```
pip install -r requirements.txt
```
running
```
python manage.py runserver
```

# Testing:
registration/authentication : http://localhost:8000/registration <br>
login/authentication : http://localhost:8000/login  <br>
