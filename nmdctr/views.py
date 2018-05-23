#############################################################
#        Name: views.py
# Description: Definition of the app view.
#      Author: Ramprasad Beerappa <r.beerappa@stud.uis.no>
#  Created on: 20.05.2018
#  Amended on: 23.05.2018
#############################################################

from django.shortcuts import render
from .forms import NamedCtrForm

# Create your views here.

# Global dictionary for caching named counter(s)
counter_dict = {}


# Function to process request from index page
def index(request):
    """
    View function for home page of site.
    """

    home_page = 'index.html'
    global counter_dict

    if request.method == 'POST':
        # Handle new named counter action
        if 'add' in request.POST:
            form = NamedCtrForm(request.POST)
            if form.is_valid() and form.cleaned_data['new_ctr_name']:
                ctr_name = form.cleaned_data['new_ctr_name']
                if not form.validate_ctr_name():
                    counter_dict[ctr_name] = 0
                    counter_dict = {k: v for k, v in sorted(counter_dict.items())}

        # Handle decrement a named counter action
        elif 'decrement' in request.POST:
            ctr_name = request.POST['decrement']
            if counter_dict[ctr_name] > 0:
                counter_dict[ctr_name] -= 1

        # Handle increment a named counter action
        elif 'increment' in request.POST:
            ctr_name = request.POST['increment']
            counter_dict[ctr_name] += 1

        # Handle delete a named counter action
        elif 'delete' in request.POST:
            ctr_name = request.POST['delete']
            del counter_dict[ctr_name]

    context = prepare_response()
    # Render the prepared response in the browser
    return render(request, home_page, context)


# Prepare response to be served to user
def prepare_response():
    nmd_ctr_total = 0

    # Compute the total value of counter(s)
    for _, v in counter_dict.items():
        nmd_ctr_total += v

    # Formulate the data to be sent to browser
    form = NamedCtrForm()
    return {'form': form, 'ctr': counter_dict, 'nmd_ctr_total': nmd_ctr_total}
