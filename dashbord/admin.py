from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Product, Order

# Register your models here.
#admin.site.register(Product)
#admin.site.register(Order)
# admin.site.unregister(Group)

class AdminProduct(admin.ModelAdmin): 
    list_display = ("product","quantity","category")
    list_filter = ["category"]

class AdminOrder(admin.ModelAdmin): 
    list_display = ("name","staff","order_quantity")

admin.site.register(Product,AdminProduct)
admin.site.register(Order,AdminOrder)
