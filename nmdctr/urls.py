#############################################################
#        Name: urls.py
# Description: Definition of the urls.
#      Author: Ramprasad Beerappa <r.beerappa@stud.uis.no>
#  Created on: 20.05.2018
#  Amended on: 22.05.2018
#############################################################

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]
