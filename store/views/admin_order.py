from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.Customer import Customer
from store.models.Products import Product
from store.models.Order import Order
from django.views import  View
from django.core.paginator import Paginator
class admin_orders(View):

    def get(self,request):
        m = request.session.get('customer')

        if Customer.objects.filter(id=m):
            print('co pha la admin', )
            customer = Customer.objects.get(id=m)
            if customer.isadmin :
                array = []
                orders = Order.objects.filter(status=False).order_by('date')
                orders1 = Order.objects.filter(status=True).order_by('date')
                for i in orders:
                    array.append(i)
                for i in orders1:
                    array.append(i)
                paginator = Paginator(array, 2)
                print(array)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, 'store/admin_orders.html', {'page': page_obj})
            else:
                return redirect('store:home')
        else:
            return redirect('store:home')
    def post(self,request):
        status=request.POST.get('status')
        product = request.POST.get('productid')
        customer = request.POST.get('customer')
        print('hello')
        print(status)
        print(product)
        print(customer)
        print('-------------------')
        customer_order=Customer.objects.get(email=customer)
        product_id=Product.objects.get(name=product)
        order=Order.objects.filter(customer=customer_order,product=product_id).update(status=True)
        print(customer_order.id)



        return redirect('store:manage')