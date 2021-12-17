from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.Customer import Customer
from django.views import View

from store.models.Products import Product
from store.models.Order import Order


class checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.objects.filter(id__in =list(cart.keys()))
        print(address, phone, customer, cart, products)
        customerId=Customer.objects.get(id=customer)
        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            product.instock=product.instock-cart.get(str(product.id))
            product.save()
            print(product.instock)
        request.session['cart'] = {}

        return redirect('store:cart')
