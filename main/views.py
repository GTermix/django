from django.shortcuts import render
from django.http import HttpRequest


def main_page(request: HttpRequest):
    return render(request, "main/index.html")


def furniture_page(request: HttpRequest):
    return render(request, "main/furniture.html")


def about_page(request: HttpRequest):
    return render(request, "main/about.html")


def contact_page(request: HttpRequest):
    return render(request, "main/contact.html")


def shop_page(request: HttpRequest):
    return render(request, "main/shop.html")
