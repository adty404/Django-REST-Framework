from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # Custom fields to display additional information
    my_discount = serializers.SerializerMethodField(read_only=True)  # Calculate and show the product's discount
    sale_price = serializers.SerializerMethodField(read_only=True)  # Display the product's sale price

    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'my_discount']

    # Method to calculate the product's discount
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id') or not isinstance(obj, Product):
            return None  # Unable to calculate discount
        return obj.get_discount()

    # Method to provide the product's sale price
    def get_sale_price(self, obj):
        if not hasattr(obj, 'id') or not isinstance(obj, Product):
            return None  # Unable to determine sale price
        return obj.sale_price
