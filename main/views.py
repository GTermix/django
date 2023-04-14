from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def main_page(request: HttpRequest):
    return HttpResponse(
        """<h1 style="color:grey;text-align:center;">Hello World</h1></br><a style="text-decoration: none;" href="/about/">About Us
        \t</a><a style="text-decoration: none;" href="/contact/">Contact with admin</a>""")


def about_page(request: HttpRequest):
    return HttpResponse("""<h1 style="color:grey;text-align:center;">About Us</h1></br><a style="text-decoration: none;" href="/">Main page 
    \t</a><a style="text-decoration: none;" href="/contact/">Contact with admin</a><p>lorem500</p>""")


def contact_page(request: HttpRequest):
    return HttpResponse("""<h1 style="color:grey;text-align:center;">Contact Us</h1></br><a style="text-decoration: none;" href="/">Main page 
    \t</a><a style="text-decoration: none;" href="/about/">About Us</a></br><a href="https://t.me/yuldashevb_0221">Contact with telegram</a>""")
