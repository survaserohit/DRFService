from functools import partial
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartItemSerializer
from rest_framework import serializers, status
from .models import CartItem
# Create your views here.
class CartItemViews(APIView):
    #Persists data sent using request body
    def post(self,request):
        serializer = CartItemSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({"Status":"Success","data":serializer.data},status= status.HTTP_200_OK)
        else:
            return Response({"Status":"Error","data":serializer.errors},status= status.HTTP_400_BAD_REQUEST)
    
    #retrives a single item or data according to id or all data
    def get(self,request,id = None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status":"Success","data":serializer.data},status= status.HTTP_200_OK)
        items = CartItem.objects.all() 
        serializer = CartItemSerializer(items, many=True)
        return Response({"status":"Success","data":serializer.data},status = status.HTTP_200_OK)      
    
    #Updates the data
    def patch(self,request,id = None):
        item = CartItem.objects.get(id = id)
        serializer = CartItemSerializer(item,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Success","data":serializer.data},status = status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors})
        
    #Delete a item in persistance by using delete()
    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
