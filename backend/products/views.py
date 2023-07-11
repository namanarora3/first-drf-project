from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

# Detail OF A PRODUCT
class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

get_prod = ProductDetailAPI.as_view()

# List or Create
class ProductListCreateAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

list_create_prod = ProductListCreateAPI.as_view()

#delete
class ProductRemoveAPI(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

del_prod = ProductRemoveAPI.as_view()

#update
class ProductUpdateAPI(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    # def perform_update(self, serializer):
    #     return super().perform_update(serializer)

update_prod = ProductUpdateAPI.as_view()

# list vew
# class ProductListAPI(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = "id"

# list_prod = ProductListAPI.as_view()