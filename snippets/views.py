# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import detail_route
from snippets.permissions import IsOwnerOrReadOnly

class SnippetViewSet(viewsets.ModelViewSet):
    """
    viewset自动提供了`list`, `create`, `retrieve`,
    `update` 和 `destroy` 动作.

    同时我们手动增加一个额外的'highlight'动作用于查看高亮的代码段
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    viewset自动提供了list和detail动作
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
