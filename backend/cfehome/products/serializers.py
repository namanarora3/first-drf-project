from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_cost = serializers.SerializerMethodField(read_only = True) #how to impliment a field with a different name in the model serializer
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_cost'
        ]

    def get_my_cost(self,obj): # we can call the object of the instance, thats the specal feature
        return obj.cost()
    
    # we can have multiple serializers for the same model