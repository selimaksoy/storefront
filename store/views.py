from django.http import HttpResponse
from django.template import loader

from .models import *
from .Person import *

def index(request):
    template = loader.get_template('index.html')
    context = {
        'categories': Category.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def product(request, id):
    ##pass
    template = loader.get_template('product.html')
    context = {
        'product': Product.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))

def person(request):
    ##pass
    template = loader.get_template('person.html')
    context = {
        'people': Person.objects.all(),
    }
    return HttpResponse(template.render(context, request))