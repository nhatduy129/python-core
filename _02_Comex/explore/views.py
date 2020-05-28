# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .models import Partnership
from .serializers import CategorySerializer
from .serializers import PartnershipSerializer


# Create your views here.
class CategoryList(APIView):
    def get(self, request):
        res = Category.objects.all()
        serializer = CategorySerializer(res, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class PartnershipList(APIView):
    def get(self, request):
        res = Partnership.objects.all()
        serializer = PartnershipSerializer(res, many=True)
        return Response(serializer.data)

    def post(self):
        pass
