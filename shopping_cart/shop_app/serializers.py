from django.db.models import fields
from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required = False,default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')    # Tells the user to use all the fields with a gurantee that it won't change.