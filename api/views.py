import json
import logging

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from main.models import Product, Category
from django.forms import model_to_dict
from .serializers import CategorySerializer
from rest_framework.generics import GenericAPIView


@api_view(http_method_names=['GET'])
def main(req: Request):
    products = Product.objects.all().values()
    return Response(data=list(products))


class CatDetailCreateView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def post(self, req):
        serializer = self.get_serializer_class()(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, req):
        serializer = self.get_serializer_class()(Category.objects.all(), many=True)
        return Response(data=serializer.data)


class CatDeleteEditView(GenericAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, req, pk):
        cat = get_object_or_404(Category, pk=pk)
        serializer = self.get_serializer_class()(cat)
        return Response(data=serializer.data)

    def patch(self, req, pk):
        cat = get_object_or_404(Category, pk=pk)
        serializer = self.get_serializer_class()(cat, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(cat, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, req, pk):
        cat = get_object_or_404(Category, pk=pk)
        serializer = self.get_serializer_class()(cat, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(cat, serializer.validated_data)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, req, pk):
        cat = get_object_or_404(Category, pk=pk)
        cat.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)
