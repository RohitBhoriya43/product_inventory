from django.shortcuts import render
from rest_framework import status

from product_curd.serializers import ProductSerializer
from .utils import set_response
from rest_framework.views import APIView
from .models import Products


class ProductCurd(APIView):
    authentication_classes=()
    permission_classes=()

    def get(self,request,*args,**kwargs):
        try:
            product_id = kwargs.get("product_id")
            print(product_id)
            if product_id is None:
                product_obj = Products.objects.all()
                print(product_obj)
                if product_obj.count() > 0:
                    product_serializer = ProductSerializer(product_obj,many=True)
                else:
                    return set_response(False,{},"Firstly product will be created",status.HTTP_400_BAD_REQUEST)  
            else:
                product_obj = Products.objects.filter(id = int(product_id))
                if product_obj.exists():
                    product_serializer = ProductSerializer(product_obj.first())
                else:
                    return set_response(False,{},"Product Not Found",status.HTTP_400_BAD_REQUEST)

            return set_response(True,product_serializer.data,"",status.HTTP_200_OK)   
        except Exception as e:

            return set_response(False,{},str(e),status.HTTP_400_BAD_REQUEST)

    def put(self,request,*args,**kwargs):
        try:
            data = request.data
            product_id = kwargs.get("product_id")
            if product_id is None:
                return set_response(False,{},"Please Provide the product id",status.HTTP_400_BAD_REQUEST)
            product_obj = Products.objects.filter(id=int(product_id))
            if not product_obj.exists():
                return set_response(False,{},"Product does not exists",status.HTTP_400_BAD_REQUEST)
            return self.check_data(data,product_obj.first())
        except Exception as e:

            return set_response(False,{},str(e),status.HTTP_400_BAD_REQUEST)
    


    def delete(self,request,*args,**kwargs):
        try:
            product_id = kwargs.get("product_id")
            if product_id is None:
                product_obj = Products.objects.filter(id= int(product_id))
                if product_obj.count() >0:
                    product_obj = product_obj.first()
                    product_obj.delete()
                else:
                    return set_response(False,{},"Product Not Found",status.HTTP_400_BAD_REQUEST)

            return set_response(True,{},f"product will be deleted as a product id {product_id}",status.HTTP_200_OK)   
        except Exception as e:

            return set_response(False,{},str(e),status.HTTP_400_BAD_REQUEST)
        

    def check_data(self,data,product_obj):
        name = data.get("name",None)
        category = data.get("category",None)
        price = data.get("price",0.0)

        if name is not None and name != "":
            product_obj.name = name
        
        if category is not None and category != "":
            product_obj.category = category
        
        if price is not None and price != 0.0:
            product_obj.price = price

        
        product_obj.save()
        product_serializer = ProductSerializer(product_obj)
        return set_response(True,product_serializer.data,"product is updated",status.HTTP_200_OK)
        