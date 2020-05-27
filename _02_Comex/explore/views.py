# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import category
from . serializers import categorySerializer

# Create your views here.
class categoryList(APIView):
    def get(self, request):
        employees1 = category.objects.all()
        serializer = categorySerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
