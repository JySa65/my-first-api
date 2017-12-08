from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as apodo
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('User Must Have a Valid Username')
        account = self.model(
            username=self.model.normalize_username(username)
        )
        account.set_password(password)
        account.save()
        return account
    def create_superuser(self, username, password, **kwargs):
        account = self.create_user(username, password, **kwargs)
        account.is_superuser = True
        account.is_staff = True
        account.save()
        return account

class Account(AbstractBaseUser, PermissionsMixin):
    ci = models.IntegerField(apodo('cedula'), null=True, blank=True)
    name = models.CharField(apodo('nombre'), max_length=50, null=True, blank=True)
    last_name = models.CharField(apodo('apellido'), max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(apodo('Fecha de Naciemiento'), null=True, blank=True)
    email = models.EmailField(apodo('correo electronico'), null=True, blank=True)
    username = models.CharField(apodo('username'),
    	max_length=40, primary_key=True, null=False, unique=True, blank=False)
    is_active = models.BooleanField(apodo('active'), default=True)
    is_staff = models.BooleanField(apodo('staff status'), default=False)
    is_superuser = models.BooleanField(apodo('superuser status'), default=False)
    date_joined = models.DateTimeField(apodo('date joined'), default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.username)

    def get_full_name(self):
        return ' '.join([str(self.name), ' ', str(self.last_name)])
    
    def get_short_name(self):
        return str(self.username)
    