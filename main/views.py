from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    return render(request, "main/index.html")


def add_order(req):
    form = OrderForm()
    if req.method == "POST":
        form = OrderForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(req, "main/order.html", context={'form': form})


def product_add(req):
    form = ProductForm()
    if req.method == "POST":
        form = ProductForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(req, "main/product.html", context={"form": form})


def contact_add(req):
    form = ContactForm()
    if req.method == "POST":
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(req, "main/contact.html", context={"form": form})


def customer_page(req):
    form = CustomerForm()
    if req.method == "POST":
        form = CustomerForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(req, "main/customer.html", context={"form": form})


def address_page(req):
    form = AddressForm()
    if req.method == "POST":
        form = AddressForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(req, "main/contact.html", context={"form": form})
