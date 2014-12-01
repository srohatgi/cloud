__author__ = 'sumeetrohatgi'

from rest_framework import serializers
from hunts.models import Hunt, Business, User


class HuntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hunt
        fields = ('huntId', 'businessId', 'category', 'description',
                  'price', 'currency', 'minimum', 'committed',
                  'createdBy', 'updatedBy', 'createdOn', 'updatedOn',)


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('businessId', 'name', 'mobile',
                  'addressLine1', 'addressLine2', 'state', 'city', 'zip',
                  'contact', 'email', 'website', 'ownerId',
                  'createdBy', 'updatedBy', 'createdOn', 'updatedOn',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'name', 'email',
                  'login', 'password',
                  'createdBy', 'updatedBy', 'createdOn', 'updatedOn',)

