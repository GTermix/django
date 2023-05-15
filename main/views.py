from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *
from .models import *

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.views import View
from django.views.generic import ListView


class password_reset_request(View):
    def post(self, request):
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'gtermix7@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("main:homepage")
            messages.error(request, 'An invalid email has been entered.')

    def get(self, request):
        password_reset_form = PasswordResetForm()
        return render(request=request, template_name="password/password_reset.html",
                      context={"password_reset_form": password_reset_form})


def reg_form(req):
    form = NewCreationForm()
    if req.method == "POST":
        form = NewCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            messages.success(req, "reg seccs")
            return redirect("index")
        messages.error(req, "err")
    return render(req, 'main/regs.html', {'form': form})


def login_(req):
    if req.method == "POST":
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pas = form.cleaned_data.get('password')
            ise = authenticate(request='req', password=pas, username=user)
            if user:
                login(req, ise)
                messages.success(req, "reg seccs")
                return redirect("index")
            else:
                messages.error(req, "err")
        messages.error(req, "err")
    form = AuthenticationForm()
    return render(request=req, template_name="main/regs.html", context={"form": form})


def logout_(req):
    logout(req)
    messages.info(req, "You have successfully logged out.")
    return redirect('index')


def index(request):
    return render(request, "main/index1.html")


class Products(ListView):
    paginate_by = 3

    def get(self, req, cat_slug=None):
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
