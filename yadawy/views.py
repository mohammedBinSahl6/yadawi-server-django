from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import User, Category, Product

# Create your views here.


def register(request):
    data = json.loads(request.body)
    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        address=data['address'],
        phone=data['phone'],
    )
    user.save()
    return JsonResponse({"token": user.user_id})


def login(request):
    data = json.loads(request.body)
    result = User.objects.filter(email=data['email'], password=data['password']).all()
    if len(result) == 0:
        return JsonResponse({"error": "wrong email or password"})
    else:
        user = result[0]
        return JsonResponse({"token": user.user_id}, status=422)
        

def home(request):
    products = list(Product.objects.filter(discount__gt=0).all().values())
    return JsonResponse({"most_ordered_products": products})


def categories(request):
    categories = list(Category.objects.all().values())
    return JsonResponse({"categories": categories})


def shop(request):
    # products = Pro
    return JsonResponse({"": ""})


def product_page(request, product_id):
    try:
        product = list(Product.objects.filter(product_id=product_id).values())[0]
        print(product)
        return JsonResponse({"product": product})
    except Exception as e:
        print(e)
        return JsonResponse({"error": "product not found"}, status=422)
        
    