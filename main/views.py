from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import RegForm, MainForm
from .models import Registration


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


def registration_page(request):
    form = MainForm()
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            print(form.errors)
    return render(request, "main/sign.html", context={"form": form})


def watch_menu(req):
    infos = Registration.objects.all()
    return render(req, "main/check_menu.html", context={"infos": infos})


def delete_info(req, pk):
    info = Registration.objects.filter(id=pk)
    info.delete()
    return redirect("index")


def edit_info(req):
    pass
