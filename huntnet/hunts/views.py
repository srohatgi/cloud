from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from hunts.models import Hunt, Business, User
from hunts.serializers import HuntSerializer, BusinessSerializer, UserSerializer


@api_view(['GET', 'POST'])
def hunt_list(request, format=None):
    """
    List all hunts or create a new hunt
    """
    if request.method == 'GET':
        hunts = Hunt.objects.all()
        serializer = HuntSerializer(hunts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HuntSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def hunt_detail(request, pk, format=None):
    """
    Retrieve, update or delete a hunt.
    """
    try:
        hunt = Hunt.objects.get(pk=pk)
    except Hunt.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HuntSerializer(hunt)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HuntSerializer(hunt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hunt.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
