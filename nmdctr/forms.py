#############################################################
#        Name: forms.py
# Description: Definition of the app form.
#      Author: Ramprasad Beerappa <r.beerappa@stud.uis.no>
#  Created on: 20.05.2018
#  Amended on: 22.05.2018
#############################################################

from django import forms
import re


# Named counter form class
class NamedCtrForm(forms.Form):
    # Define input field in the form
    new_ctr_name = forms.CharField(label='Name', max_length=10, required=True,
                                   widget=forms.TextInput(attrs={'autofocus': 'autofocus', 'placeholder': 'E.g. Bob'}))

    # Validate the new counter name to accept only characters
    def validate_ctr_name(self):
        data = self.cleaned_data['new_ctr_name']

        reg = re.compile('^[a-zA-Z]+$')

        if (0 < len(data) >= 10) or not reg.match(data):
            return 1
