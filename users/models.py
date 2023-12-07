"""
user model
"""
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin, BaseUserManager)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        create user
        """

        if not email:
            raise ValueError('Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, username
        and password.
        """
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    

class UserModel(AbstractBaseUser):
    """
    User model
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self) -> str:
        return self.first_name + self.last_name
    

    class Meta:
        db_table = 'users'

