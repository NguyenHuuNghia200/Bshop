from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.Customer import Customer
from django.views import View

from store.models.Products import Product
from store.models.Order import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):
    def get(self , request ):
        if request.session.get('customer'):
            customer = request.session.get('customer')
            orders = Order.get_orders_by_customer(customer)
            print(orders)
            print(orders)
            return render(request , 'store/orders.html'  , {'orders' : orders})
        else:
            return redirect('store:login')