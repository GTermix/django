from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT


@api_view(http_method_names=['GET', 'POST'])
def main(req: Request):
    if req.method == 'POST':
        return Response(data={'hello': 'world'}, status=HTTP_201_CREATED)
    return JsonResponse(data={'salom': 'dunyo'})
