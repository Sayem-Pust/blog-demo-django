from re import I
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer
from .models import Blog


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
