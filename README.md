# namedctr
Named counter app, a Django based web app.

# Description

* Initial load of home page is via GET request and all the operations are via POST request.
* Counter(s) list is sorted based on the name.
* It is assumed that the counter(s) value should contain only natural numbers. Therefore, the initial value of a counter is set to zero and cannot be decremented below zero.
* It is assumed that the counter(s) data should be persistent until Django server is up.

# Screenshot

![Screenshot](https://github.com/rambee/namedctr/blob/master/named_ctr_app_screenshot.png)

# Functionalities

* Create or add a new named counter
* Decrement a named counter
* Increment a named counter
* Delete a named counter
* Presents the total value of the available named counter(s)

# Installing the prerequisites (Development)

## Python > 3

$ brew install python3

## pip

$ brew postinstall python3

## Django

$ pip3 install django

# Execution

$ cd namedctr

$ python manage.py runserver

Open http://127.0.0.1:8000/ in the web browser

# Testing - Unit, Functional, and Coverage

$ pip install django-nose

$ cd namedctr

$ python manage.py test
```
nosetests --with-coverage --cover-package=nmdctr --verbosity=1
Creating test database for alias 'default'...
..
Name                            Stmts   Miss  Cover
---------------------------------------------------
nmdctr/__init__.py                  0      0   100%
nmdctr/admin.py                     1      1     0%
nmdctr/apps.py                      3      3     0%
nmdctr/forms.py                     9      4    56%
nmdctr/migrations/__init__.py       0      0   100%
nmdctr/models.py                    1      1     0%
nmdctr/urls.py                      3      0   100%
nmdctr/views.py                    31     15    52%
---------------------------------------------------
TOTAL                              48     24    50%
----------------------------------------------------------------------
Ran 2 tests in 0.057s

OK
Destroying test database for alias 'default'...
```

# TODO

* Handle form resubmission.
* Pagination for the list of available counters if the list grows beyond the page.
