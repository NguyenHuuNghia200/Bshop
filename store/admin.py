from django.contrib import admin

from  store.models.Products import Product
from store.models.Customer import Customer
from store.models.Category import Category
from store.models.Order import Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
from django.contrib import admin

# Register your models here.
