from django.db import models
from config.model_utils.models import TimeStampedModel

class Category(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField('products.Product', related_name='categories')
    
    def __str__(self):
        return f"Category: {self.name}"
    

class CategoryImage(TimeStampedModel, models.Model):
    image = models.ImageField(upload_to='categories/')
    product = models.ForeignKey('categories.Category', related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for category: {self.product.name}"