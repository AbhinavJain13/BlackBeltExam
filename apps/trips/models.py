from __future__ import unicode_literals
from ..login.models import User
from django.db import models
import re, bcrypt
import datetime

# Create your models here.
class TripManager(models.Manager):

    def valid_inputs(self, param):
        errors=[]

        if len(param['d_name']) < 0 or len(param['descrip']) < 0:
            errors.append("Destination,Description and Date fields cannot be blank")

        # if  param['f_date'] <= datetime.date.today() or  param['t_date'] <= datetime.date.today():
        #     errors.append("Dates cannot be in the past or today!")

        # if param['f_date']< param['t_date']:
        #     errors.append("Travel date to should not be before TravelDate From")

        return errors

    def valid_add(self, param):
        errors = self.valid_inputs(param)
        if len(errors) > 0:
            return (False, errors)
        trip = self.create(d_name = param['d_name'], descrip= param['descrip'], f_date = param['f_date'],t_date = param['t_date'])
        return (True, trip)

class Trip(models.Model):
    d_name = models.CharField(max_length=255) #unique =True(model validations)
    descrip = models.CharField(max_length=255)
    f_date= models.DateField(blank=True, null=True)
    t_date= models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripManager()
