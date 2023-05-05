from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


def index(request):
    return render(request, "main/index.html")


def products(req, cat_slug=None):
    cats = Category.objects.all()
    if cat_slug:
        cat = get_object_or_404(Category, slug=cat_slug)
        pr = Product.objects.filter(category=cat)
    else:
        pr = Product.objects.all()
    return render(req, "main/products.html", context={"products": pr, "kats": cats})


def product_details(req, pk):
    product = get_object_or_404(Product, id=pk)
    return render(req, "main/product_info.html", {"product": product})


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
        form = ProductForm(req.POST, req.FILES)
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
