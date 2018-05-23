#############################################################
#        Name: tests.py
# Description: Definition of the test cases for the app.
#      Author: Ramprasad Beerappa <r.beerappa@stud.uis.no>
#  Created on: 22.05.2018
#  Amended on: 23.05.2018
#############################################################

from django.test import Client
import django
from django.test import TestCase

# Create your tests here.


class TestNmdCtr(TestCase):
    django.setup()

    def test_get_home(self):
        self.c = Client()
        self.response = self.c.get('/nmdctr/')
        print("GET app home page content: {}\n".format(self.response.content))
        print("GET app home page status: {}\n".format(self.response.status_code))

    def test_add_counter(self):
        self.c = Client()
        response = self.c.post('/nmdctr/', {'add': 'Bob'})
        self.assertEqual(response.status_code, 200)
