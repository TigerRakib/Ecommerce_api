from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Product
from .serializers import Productserializer
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def get_products(request):
    all_products=Product.objects.all()
    serializer=Productserializer(all_products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_product(request,pk):
    product= get_object_or_404(Product,id=pk)
    serializer=Productserializer(product, many=False)
    return Response(serializer.data)