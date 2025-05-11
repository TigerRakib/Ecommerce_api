from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Product
from .serializers import Productserializer
from rest_framework.response import Response
from .filters import ProductsFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.
@api_view(['GET'])
def get_products(request):
    all_products=Product.objects.all()
    filterset= ProductsFilter(request.GET, queryset=all_products.order_by('id'))
    count=filterset.qs.count()
    #pagination
    resPerPage=1
    paginator=PageNumberPagination()
    paginator.page_size=resPerPage
    query_set= paginator.paginate_queryset(filterset.qs, request)
    serializer=Productserializer(query_set, many=True)
    return Response({
        "count":count,
        "resperpage":resPerPage,
        "products":serializer.data})

@api_view(["GET"])
def get_product(request,pk):
    product= get_object_or_404(Product,id=pk)
    serializer=Productserializer(product, many=False)
    return Response(serializer.data)