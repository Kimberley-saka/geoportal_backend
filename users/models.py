from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    """
    User
    """
    password = models.CharField(max_length=250, null=False)


    REQUIRED_FIELDS = ['email', 'password']
    USERNAME_FIELD = 'email'

    class Meta:
        """meta data"""

        db_table = 'users'



