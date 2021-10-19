from django.shortcuts import render
from random import randint

def cart_detail(request):
    if request.session.get("test") is None:
        request.session["teste"] = randint(1, 1000)
    return render(request, 'cart/cart_detail.html')