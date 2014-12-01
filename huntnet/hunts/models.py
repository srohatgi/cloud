# Create your models here.
from django.db import models


class Hunt(models.Model):
    huntId = models.CharField(max_length=37, primary_key=True)
    businessId = models.ForeignKey('Business')
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    currency = models.CharField(max_length=3, default='USD')
    minimum = models.IntegerField()
    committed = models.IntegerField()

    createdBy = models.ForeignKey('User', related_name='+')
    updatedBy = models.ForeignKey('User', related_name='+')
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('createdOn',)


class Business(models.Model):
    businessId = models.CharField(max_length=37, primary_key=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=32)
    addressLine1 = models.CharField(max_length=255)
    addressLine2 = models.CharField(max_length=255)
    state = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    zip = models.CharField(max_length=32)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    ownerId = models.ForeignKey('User')

    createdBy = models.ForeignKey('self', related_name='+')
    updatedBy = models.ForeignKey('self', related_name='+')
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('createdOn',)


class User(models.Model):
    userId = models.CharField(max_length=37,  primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    createdBy = models.ForeignKey('User', related_name='+')
    updatedBy = models.ForeignKey('User', related_name='+')
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('createdOn',)
