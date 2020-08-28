from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Projeto(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Usuario(PermissionsMixin, AbstractBaseUser):
    name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=40, unique=True, null=True)
    birthdate = models.DateField(blank=True,null=True)
    admission_date = models.DateField(blank=True, null=True)
    job_role = models.CharField(max_length=22, blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    projetos = models.ForeignKey(Projeto, 
        on_delete=models.DO_NOTHING, 
        blank=True, 
        null=True
        )
    objects = EmailUserManager()
    USERNAME_FIELD = 'email'
    