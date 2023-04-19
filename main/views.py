from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def main_page(request: HttpRequest):
    return render(request, "main/index.html")


def about_page(request: HttpRequest):
    return render(request, "main/about.html")


def contact_page(request: HttpRequest):
    return render(request, "main/contact.html")


def registration_page(request: HttpRequest):
    return render(request, "main/registration.html")
