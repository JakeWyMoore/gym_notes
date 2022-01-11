from django.db import models

from sre_constants import GROUPREF, error
from django.db import models

import bcrypt
import re

class UserManager(models.Manager):

    # REGISTER VALIDATIONS
    def register_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 1:
            errors['first_name'] = "Must enter first name."
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Must enter last name."

        email_regex = re.compile(r'^[a-zA-Z0-9.=_-]+@[a-zA-Z0-9.=_-]+\.[a-zA-Z]+$')

        if len(postData['email']) == 0:
            errors['email'] = "Must enter email."
        elif not email_regex.match(postData['email']):
            errors['email'] = "Must be valid email."

    #LOGIN VALIDATIONS
    def login_validator(self, postData):
        errors = {}

        existing_user = User.objects.filter(email = postData['email'])
        if len(existing_user) != 1:
            errors['email'] = "User does not exist"
        if len(postData['email']) == 0:
            errors['email'] = "No email entered"

        if len(postData['password']) < 8:
            errors ['password'] = "Password must be at least 8 characters"
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['mismatch'] = "Email and password do not match"

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Workout(models.Model):
    group = models.CharField(max_length=50)

    sets = models.CharField(max_length=50)
    reps = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)