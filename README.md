# Little Lemon API

# Setup
## Step 1 - Install Python 3.10.5 on your system
```
https://www.python.org/downloads/
```
## Step 2 - Install pipenv
```
https://pipenv.pypa.io/en/latest/
```
## Step 3 - activate virtual environment
```
pipenv shell
```
## Step 4 - Install dependencies
```
pipenv install
```
## Final Step - Start the server
```
python manage.py runserver
```

# Endpoints
## Booking
```
/restaurant/menu
/restaurant/menu/{pk}
/restaurant/booking/
```

## Users list and Registration
```
/auth/users/
/auth/users/me
```
## User Login
```
auth/token/login
```