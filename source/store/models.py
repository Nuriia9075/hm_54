from django.core import validators
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=70, verbose_name= 'Category_name', unique=True, null=False, blank=False)
    description = models.TextField(verbose_name= 'Category_description', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=70, verbose_name='Product_name', null=False, blank=False)
    description = models.TextField(verbose_name='Product_description', blank=True, null=True)
    create_date = models.DateTimeField(null=False, auto_now_add= True, verbose_name = 'Product_create_date')
    up_date = models.DateTimeField(auto_now= True, verbose_name = 'Product_up_date')
    price = models.DecimalField(null=False, verbose_name='Price', max_digits=7, decimal_places=2)
    product_img = models.URLField(verbose_name='Product_img', max_length=255, null=False)
    quantity = models.IntegerField(verbose_name='Product_quantity', null= False, blank = False, validators= [MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Product_category', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Product'