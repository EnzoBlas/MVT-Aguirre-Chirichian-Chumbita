from django.http import HttpResponse
from datetime import datetime
from datetime import date
from django.template import loader

from django.http import HttpResponse
from datetime import datetime
from django.template import loader

from app_family.models import Relative

def new_relative(
    self, name: str='Name', last_name: str='Last_name', date_of_birth: date = 0):
    
    template = loader.get_template('relative.html')

    relative = Relative(name=name, last_name=last_name, date_of_birth=date_of_birth)
    relative.save()

    context_dict = {
        'relative' : relative
        }
    
    render = template.render(context_dict)
    
    return HttpResponse(render)


def my_family(self):

    template = loader.get_template('family.html')

    relative = Relative.objects.all()

    context_dict = {
        'relative': relative
    }

    render = template.render(context_dict)
    return HttpResponse(render)