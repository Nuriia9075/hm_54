from django.contrib import admin

# Register your models here.
from store.models import Product, Category

admin.site.register(Product, admin.ModelAdmin)
admin.site.register(Category, admin.ModelAdmin)


