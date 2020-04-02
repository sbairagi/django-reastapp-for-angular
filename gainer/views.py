from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer,ContactSerializers,OrdersSerializers
from .models import Product,Orderupdate
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        obj = Product.objects.all()
        serializer = ProductSerializer(obj , many=True)
        return Response(serializer.data)

@api_view(['GET'])
def prodview(request,myid):
    try:
        obj = Product.objects.get(id=myid)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializers = ProductSerializer(obj)
        return Response(serializers.data)

@api_view(['POST'])
def contact_us(request):
    if request.method == 'POST':
        serializers = ContactSerializers(data=request.data)
        if serializers.is_valid():
            print(serializers)
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def checkout(request):
    if request.method == 'POST':
        serializers = OrdersSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def orderupdate(request):
    if request.method == 'GET':
        obj = Orderupdate.objects.all()
        serializer = OrdersSerializers(obj , many=True)
        return Response(serializer.data)
