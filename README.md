# namedctr
Named counter app, a Django based web app.

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

Type http://127.0.0.1:8000/ in the web browser

# TODO

* Handle form resubmission.
* Pagination for the list of available counters if the list grows beyond the page.
