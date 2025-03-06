from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView,ListAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
<<<<<<< HEAD
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Product,Review,Cart,ProductTag,FavoriteProduct,ProductImage,CartItem
from products.filters import ProductFilter,ReviewFilter
from products.serializers import ProductSerializer,ReviewSerializer,CartSerializer,ProductTagSerializer,ProductImageSerializer,FavoriteProductSerializer,CartItemSerializer
=======
from django_filters.rest_framework import DjangoFilterBackend
from products.pagination import ProductPagination
from products.models import Product,Review,Cart,ProductTag,FavoriteProduct,ProductImage
from products.serializers import ProductSerializer,ReviewSerializer,CartSerializer,ProductTagSerializer,ProductImageSerializer,FavoriteProductSerializer
>>>>>>> 7c517b880f18da7c84a2037757f647ac331ab7a1
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class ProductViewSet(ListModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated]
<<<<<<< HEAD
    filterset_class=ProductFilter
    filter_backends=[DjangoFilterBackend,SearchFilter]
    search_fields=['name','desciption']
=======
    filter_backends=[DjangoFilterBackend,SearchFilter]
    pagination_class=ProductPagination
    filterset_fields=['price','categories']
    search_fields=['name','description']
    
   
>>>>>>> 7c517b880f18da7c84a2037757f647ac331ab7a1
    
class ReviewViewSet(ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]
<<<<<<< HEAD
    filterset_class=ReviewFilter
    filter_backends=[DjangoFilterBackend]
    
    def get_queryset(self):
        return self.queryset.filter(product_id=self.kwargs['product_pk'])
    
    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied('You cant delete this review')
        instance.delete()
        
    def perform_update(self,serializer):
        instance=self.get_object()
        if instance.user!=self.request.user:
            raise PermissionDenied("You cant change this review")
        serializer.save()
=======
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['rating']
    
    def get_queryset(self):
        queryset=self.queryset.filter(user=self.request.user)
        return queryset
>>>>>>> 7c517b880f18da7c84a2037757f647ac331ab7a1

class CartViewSet(ListModelMixin,CreateModelMixin,GenericViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    permission_clases=[IsAuthenticated]
    
    def get_queryset(self):
        queryset=self.queryset.filter(user=self.request.user)
        return queryset
    
class CartItemViewSet(ModelViewSet):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)
    
    def perform_destroy(self, instance):
        if instance.cart.user!=self.request.user:
            raise PermissionDenied("You do not have permission to delete this item.")
        instance.delete()

    def perform_update(self, serializer):
        instance=self.get_object()
        if instance.cart.user!=self.request.user:
            raise PermissionDenied("You do not have permission to update this item.")
        serializer.save()
    
class ProductTagListViewSet(ListModelMixin,GenericViewSet):
    queryset=ProductTag.objects.all()
    serializer_class=ProductTagSerializer
    permission_classes=[IsAuthenticated]
    
class FavoriteProductViewSet(ListModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin,GenericViewSet):
    queryset=FavoriteProduct.objects.all()
    serializer_class=FavoriteProductSerializer
    permission_clases=[IsAuthenticated]
    
    def get_queryset(self):
        queryset=self.queryset.filter(user=self.request.user)
        return queryset
    
class ProductImageViewSet(ListModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin,GenericViewSet):
    queryset=ProductImage.objects.all()
    serializer_class=ProductImageSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(product__id=self.kwargs['product_pk'])