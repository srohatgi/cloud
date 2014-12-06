from hunts.models import Hunt, Business, Follow, Comment
from hunts.serializers import HuntSerializer, BusinessSerializer, FollowSerializer, CommentSerializer
from rest_framework import generics


class HuntList(generics.ListCreateAPIView):
    """
    List all hunts or create a new hunt
    """
    queryset = Hunt.objects.all()
    serializer_class = HuntSerializer


class HuntDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a hunt.
    """
    queryset = Hunt.objects.all()
    serializer_class = HuntSerializer


class BusinessList(generics.ListCreateAPIView):
    """
    List all businesses or create a new business
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a business
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class FollowList(generics.ListCreateAPIView):
    """
    List all businesses or create a new business
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class FollowDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a business
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List all businesses or create a new business
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a business
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
