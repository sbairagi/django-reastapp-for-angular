from rest_framework import serializers
from .models import Product, Contact, Orders , Orderupdate

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','product_name','category','subcategory','price','desc','pub_date','image','image1','image2','image3')


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('msg_id','name','email','phone','desc')



class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('order_id','items_json','amount','name','email','address','city','state','zip_code','phone')


class OrdersupdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orderupdate
        fields = ('update_id','order_id','update_desc','timestamp')
