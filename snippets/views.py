# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):

    """
    List all code snippets, or create a new snippet.
    列出所有已经存在的snippet或者创建一个新的snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrieve, update or delete a code snippet.
    检索查看、更新或者删除一个snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
