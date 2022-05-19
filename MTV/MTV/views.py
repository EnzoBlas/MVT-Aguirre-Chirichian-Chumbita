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
    
    if (str(date.today())[5:]) > date_of_birth[5:]:
        age = int(str(date.today())[:4]) - int(date_of_birth[:4])
    else:
        age = int(str(date.today())[:4]) - int(date_of_birth[:4]) - 1

    relative = Relative(name=name, last_name=last_name, date_of_birth=date_of_birth, age=age)
    relative.save()

    context_dict = {
        'relative' : relative,
        'age' : age
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

def index(self):

    template = loader.get_template('index.html')

    context_dict = {}

    render = template.render(context_dict)
    return HttpResponse(render)