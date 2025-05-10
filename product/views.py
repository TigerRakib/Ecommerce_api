from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Product
from .serializers import Productserializer
from rest_framework.response import Response
from .filters import ProductsFilter
# Create your views here.
@api_view(['GET'])
def get_products(request):
    all_products=Product.objects.all()
    filterset= ProductsFilter(request.GET, queryset=all_products.order_by('id'))
    serializer=Productserializer(filterset.qs, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_product(request,pk):
    product= get_object_or_404(Product,id=pk)
    serializer=Productserializer(product, many=False)
    return Response(serializer.data)