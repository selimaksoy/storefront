from django.contrib import admin

from .models import *

from .Person import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Person)