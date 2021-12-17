from cv2.cv2 import cuda_BufferPool
from django.shortcuts import render,HttpResponse ,redirect,HttpResponseRedirect
from store.models.Products import Product
from store.models.Category import Category
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your viewsasas here.
#@login_required
class Index1(View):
    def post(self , request):
        if request.session.get('customer'):
            product = request.POST.get('product')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            mess=''
            if cart:
                quantity = cart.get(product)
                product1=Product.objects.get(id=product)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        if cart[product] >product1.instock :
                            mess='out in stock'
                            print(mess)
                        else:
                            cart[product] = quantity + 1
                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1
            request.session['cart'] = cart
            if mess:
                request.session['mess']=mess
            print(mess,'asdsd')
            print('cart', request.session['cart'])
            redirect('store:login')
            return redirect('store:homepage')
        else:
            return redirect('store:login')

    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/home{request.get_full_path()[1:]}')


class Index(View):
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        customer=request.session.get('customer')
        print(customer,'asdas')

        if customer:
            redirect('store:login')
        else:
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        cart[product] = quantity + 1
                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1
            request.session['cart'] = cart

            print('cart1', request.session['cart'])
            for i in cart:
                print('idsgdsfsd',i,cart[i])
        return redirect('store:homepage')
    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/home{request.get_full_path()[1:]}')

class home(View):
    def get(self,request):
        cart=request.session.get('cart')
        print('a',cart)
        mess=" "
        mess_id=0
        if cart:
            for i in cart:
                product=Product.objects.get(id=i)
                if cart[i]>product.instock:
                    mess="out in stock"
                    mess_id=i
                print('asddsa',cart[i])
        if not cart:
            request.session['cart'] = {}
        categoryID=request.GET.get('category')
        print(categoryID)
        if categoryID:
            listproduct=Product.objects.filter(category=categoryID)
        else:
            listproduct=Product.objects.all()

        listcategory= Category.objects.all()
        print(listproduct)
        print("mess",mess,mess_id)
        print(request.session.get('customer'))
        return render(request,"store/index.html",{'products':listproduct,'category':listcategory,'mess_id':mess_id,'mess':mess})


