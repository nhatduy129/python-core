# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Category
from .models import Partnership
from .serializers import CategorySerializer
from .serializers import PartnershipSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.
class CategoryList(APIView):
    def get(self, request):
        res = Category.objects.all()
        serializer = CategorySerializer(res, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class PartnershipList(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        # res = Partnership.objects.all()
        # serializer = PartnershipSerializer(res, many=True)
        # return Response(serializer.data)
        Partnership.objects.prefetch_related(
            'events').all().order_by('-created')

    def post(self):
        pass
