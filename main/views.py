from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from .models import *
from .serializers import *


class CategoryListCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, req):
        cats = Category.objects.all()
        ser = CategorySerializers(instance=cats, many=True)
        return Response(ser.data)

    def post(self, req):
        ser = CategorySerializers(data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_201_CREATED)


class CategoryDetailUpdateDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, req, pk):
        instance = get_object_or_404(Category, pk=pk)
        ser = CategorySerializers(instance)
        return Response(ser.data)

    def patch(self, req, pk):
        instance = get_object_or_404(Category, pk=pk)
        ser = CategorySerializers(instance, req.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def put(self, req, pk):
        instance = get_object_or_404(Category, pk=pk)
        ser = CategorySerializers(instance, req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def delete(self, req, pk):
        ins = get_object_or_404(Category, pk=pk)
        ins.delete()
        return Response({})
