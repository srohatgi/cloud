from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from hunts.models import Hunt, Business, User
from hunts.serializers import HuntSerializer, BusinessSerializer, UserSerializer
from rest_framework.views import APIView


class HuntList(APIView):
    """
    List all hunts or create a new hunt
    """
    def get(self, request, format=None):
        hunts = Hunt.objects.all()
        serializer = HuntSerializer(hunts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HuntSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HuntDetail(APIView):
    """
    Retrieve, update or delete a hunt.
    """
    def get_object(self, pk):
        try:
            hunt = Hunt.objects.get(pk=pk)
        except Hunt.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        hunt = self.get_object(pk)
        serializer = HuntSerializer(hunt)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hunt = self.get_object(pk)
        serializer = HuntSerializer(hunt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hunt = self.get_object(pk)
        hunt.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
