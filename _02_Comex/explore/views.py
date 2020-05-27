# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Category
from . serializers import CategorySerializer
from . serializers import PartnershipSerializer

# Create your views here.
class CategoryList(APIView):
    def get(self, request):
        employees1 = Category.objects.all()
        serializer = CategorySerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class PartnershipSerializer(APIView):
    def get(self, request):
