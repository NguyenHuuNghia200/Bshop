from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import  check_password,get_hasher
from store.models.Customer import Customer
from store.models.Products import Product
from django.views import  View


class Login(View):
    return_url = None
    def get(self , request):
        print('asasa')
        Login.return_url = request.GET.get('return_url')
        return render(request , 'store/login.html')

    def post(self , request):
        email1 = request.POST.get('email')
        print(email1)
        password = request.POST.get('password')
        print(password)
        customer=Customer.objects.filter(email=email1)

        error_message = None

        if customer:
            customer1=Customer.objects.get(email=email1)
            print(customer1.password)
            flag=check_password(password,customer1.password)
            print(flag)
            if flag:
                print('ok')
                request.session['customer'] = customer1.id
                request.session['customer_isadmin']=customer1.isadmin
                return redirect('store:home')
            else:
                print('1')
                error_message='Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email1, password)
        return render(request, 'store/login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('store:home')
