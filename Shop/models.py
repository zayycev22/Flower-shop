from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from PIL import Image

class CustomAccountManager(BaseUserManager):

    def createUser(self, email, name, surname, password):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **otherfields):
        otherfields.setdefault('is_staff', True)
        otherfields.setdefault('is_superuser', True)
        otherfields.setdefault('is_active', True)
        if otherfields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if otherfields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        email = self.normalize_email(email)
        super_user = self.model(email=email, password=password, **otherfields)
        super_user.set_password(password)
        super_user.save()

        return super_user


class Discount(models.Model):
    discount = models.FloatField()


class ExUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=192)
    surname = models.CharField(max_length=192)
    password = models.CharField(max_length=192)
    dicount = models.ForeignKey(Discount, models.SET_NULL, blank=True, null=True)
    date_of_birth = models.DateField(auto_now=False, blank=True, null=True)
    start_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]


class Flower(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(blank=True, upload_to='images')
    articul = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.resize((150, 200))
        img.save(self.image.path)
# Create your models here.
