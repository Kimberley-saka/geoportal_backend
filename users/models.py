from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User model
    """
    firstname = models.CharField(max_length=250, null=False)
    lastname = models.CharField(max_length=250, null=False)
    email = models.EmailField(max_length=250, null=False, unique=True)
    password = models.CharField(max_length=250, null=False)


    REQUIRED_FIELDS = ['email', 'password']

    class Meta:
        """meta data"""

        db_table = 'users'



