from django.shortcuts import render
from django.http import HttpRequest
from .forms import RegForm


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


def registration(request):
    form = RegForm()
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    return render(request, "main/reg.html", context={"form": form})
