from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    return render(request, "main/index.html")


def add_order(req):
    form = OrderForm()
    return render(req, "main/order.html", context={'form': form})

# def registration_page(request):
#     form = MainForm()
#     if request.method == "POST":
#         form = MainForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#         else:
#             print(form.errors)
#     return render(request, "main/sign.html", context={"form": form})
#
#
# def watch_menu(req):
#     infos = Registration.objects.all()
#     return render(req, "main/check_menu.html", context={"infos": infos})
#
#
# def delete_info(req, pk):
#     info = Registration.objects.filter(id=pk)
#     info.delete()
#     return redirect("index")
