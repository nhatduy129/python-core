# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, viewsets
from .models import Category
from .models import Partnership
from .serializers import CategorySerializer
from .serializers import PartnershipSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()


class PartnershipViewSet(viewsets.ModelViewSet):
    serializer_class = PartnershipSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        category_id = self.request.query_params.get('category', None)
        if category_id:
            return Partnership.objects.filter(category=category_id)
        return Partnership.objects.all()
