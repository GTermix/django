from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from .models import *
from .serializers import *


class CatsViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryClass(viewsets.ViewSet):
    def list(self, req):
        cats = Category.objects.all()
        ser = CategorySerializers(cats, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def retrieve(self, req, pk):
        user = get_object_or_404(Category, pk=pk)
        ser = CategorySerializers(user)
        return Response(ser.data)

    def create(self, request):
        ser = CategorySerializers(data=req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status.HTTP_201_CREATED)

    def update(self, req, pk=None):
        instance = get_object_or_404(Category, pk=pk)
        ser = CategorySerializers(instance, req.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def partial_update(self, req, pk=None):
        instance = get_object_or_404(Category, pk=pk)
        ser = CategorySerializers(instance, req.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def destroy(self, req, pk=None):
        ins = get_object_or_404(Category, pk=pk)
        ins.delete()
        return Response({})


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


class RegisterUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, req):
        ser = RegisterUserSerializer(data=req.data)
        ser.is_valid(raise_exception=True)
        token = ser.save_user(ser.validated_data)
        return Response({}, status=status.HTTP_201_CREATED)
