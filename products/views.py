from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from products.models import Product,Review,Cart,ProductTag,FavoriteProduct,ProductImage
from products.serializers import ProductSerializer,ReviewSerializer,CartSerializer,ProductTagSerializer,ProductImageSerializer,FavoriteProductSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class ProductViewSet(GenericAPIView,ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated]
    
    def get(self,request,pk=None,*args,**kwargs):
        if pk:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class ReviewViewSet(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

class CartViewSet(ListModelMixin,CreateModelMixin,GenericAPIView,RetrieveModelMixin):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    permission_clases=[IsAuthenticated]
    
    def get_queryset(self):
        queryset=self.queryset.filter(user=self.request.user)
        return queryset
    
    def get(self,request,pk=None,*args,**kwargs):
        if pk:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class ProductTagListView(ListModelMixin,GenericAPIView):
    queryset=ProductTag.objects.all()
    serializer_class=ProductTagSerializer
    permission_classes=[IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class FavoriteProductViewSet(GenericAPIView,ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=FavoriteProduct.objects.all()
    serializer_class=FavoriteProductSerializer
    permission_clases=[IsAuthenticated]
    
    def get_queryset(self):
        queryset=self.queryset.filter(user=self.request.user)
        return queryset
    
    def get(self,request,pk=None,*args,**kwargs):
        if pk:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class ProductImageViewSet(CreateModelMixin,DestroyModelMixin,ListModelMixin,RetrieveModelMixin,GenericAPIView):
    queryset=ProductImage.objects.all()
    serializer_class=ProductImageSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(product__id=self.kwargs['product_id'])
    
    def get(self,request,pk=None,*args,**kwargs):
        if pk:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)