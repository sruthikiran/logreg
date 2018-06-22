from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

import re
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['firstName']) < 1:
            errors["firstname"] = "First Name cannot be empty"
        elif len(postData['firstName']) < 2:
            errors["firstname"] = "First Name should be atleast 2 characters"
        elif not postData['firstName'].isalpha():
            errors["firstname"] = "First Name should contain only letters"

        if len(postData['lastName']) < 1:
            errors["lastname"] = "Last Name cannot be empty"
        elif len(postData['lastName']) < 2:
            errors["lastname"] = "Last Name should be atleast 2 characters"
        elif not postData['lastName'].isalpha():
            errors["lastname"] = "Last Name should contain only letters"

        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty"
        elif not EMAIL_REGEX.match(postData['email']):
                errors["email"] = "Not a Valid Email"

        if len(postData['pwd']) < 1:
            errors["pwd"] = "Password cannot be empty"
        elif len(postData['pwd']) < 8:
            errors["pwd"]= "Password must be more than 8 characters"
        elif len(postData['confpwd']) < 1:
            errors["pwd"] = "Field cannot be empty"
        elif len(postData['confpwd']) < 8:
            errors["confpwd"]= "Password must be more than 8 characters"
        elif not(postData['pwd'] == postData['confpwd']):
            errors["pwd"] = "Passwords don't match! Please enter again"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(max_length=255,unique=True,blank=False)
    pwdhash = models.CharField(max_length=255,blank=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
