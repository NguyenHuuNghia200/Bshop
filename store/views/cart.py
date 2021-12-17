from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.Customer import Customer
from store.models.Products import Product
from django.views import  View
from django.contrib.auth.decorators import login_required

class Cart(View):

    def get(self, request):
        if request.session.get('customer'):
            ids = list(request.session.get('cart').keys())
            print('ids',ids)
            products = Product.objects.filter(id__in =ids)
            print(products)
            return render(request, 'store/cart.html', {'products': products})
        else:
            return redirect('store:login')