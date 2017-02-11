## added 201 02 11

from datetime import date
from django.core.mail import send_mail

from store.models import Product
from django.db import models


class Person(models.Model):
    given_name = models.CharField(max_length=32)
    given_surname = models.CharField(max_length=32)
    email = models.TextField()
    dob = models.DateField()
    product = models.ForeignKey(Product)

    def get_full_name(self):
        """
        Display full name of Person
        """
        return '%s %s' % (self.given_name, self.family_name)

    def get_age(self):
        """
        Returns Person's age in years as an integer
        """
        today = date.today()
        return today.year - self.dob.year - (
            (today.month, today.day) < (self.dob.month, self.dob.day)
        )
