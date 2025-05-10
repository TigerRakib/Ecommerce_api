from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from rest_framework import response
# Create your views here.
@api_view(['GET'])
def get_products(request):
    all_products=Product.objects.all()
    print(all_products)
    return response("Hello Rakib")

@api_view(["GET"])
def get_product(request,pk):
    pass