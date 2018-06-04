# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users': reverse('user-list',request=request,format=format),
        'snippets': reverse('snippet-list',request=request,format=format)
    })

class SnippetList(generics.ListCreateAPIView):

    """
    List all code snippets, or create a new snippet.
    列出所有已经存在的snippet或者创建一个新的snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrieve, update or delete a code snippet.
    检索查看、更新或者删除一个snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self,request,*args,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

class UserList(generics.ListAPIView):

    """
    List all users.
    列出所有已经存在的User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):

    """
    Retrieve a User.
    检索查看一个User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
