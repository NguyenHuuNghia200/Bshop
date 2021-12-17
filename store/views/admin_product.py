from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.Customer import Customer
from store.models.Products import Product
from store.models.Category import Category
from django.views import  View
from django.core.paginator import Paginator
class admin_product(View):
    def get(self,request):
        m = request.session.get('customer')
        if Customer.objects.filter(id=m):
            customer = Customer.objects.get(id=m)
            if customer.isadmin :
                product=Product.objects.all()
                paginator = Paginator(product, 5)
                print(product)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                category=Category.objects.all()
                print(category)
                return render(request,'store/asd.html',{'page' : page_obj,'category':category})
            else:
                return redirect('store:home')
        else:
            return redirect('store:home')
class product_edit(View):
    def get(self,request):
        name=request.GET.get('name1')
        print('sadsafb!!!',name)
        product=Product.objects.get(name=name)
        category = Category.objects.exclude(name=product.category)
        return render(request,'store/admin_product_edit.html',{'product':product,'category':category})
    def post(self,request):
        name = request.POST.get('name')
        name1 = request.POST.get('asd')
        print(name,'sd',name1)
        product=Product.objects.get(name=name1)
        print(product,'sds')
        category1 = request.POST.get('category')
        stock = request.POST.get('stock')
        image = request.POST.get('fileInput')
        price = request.POST.get('Price')
        print((category1, price,stock, image, name))
        cate=Category.objects.get(name=category1)
        if image:
            product.image=image
        else:
            image=product.image
        product.name=name
        product.instock=stock
        product.image=image
        product.price=price
        product.category.id=cate.id
        product.save()
        print('name moi',)
        return  redirect('store:home')
class product_add(View):
    def get(self,request):
        m = request.session.get('customer')
        if Customer.objects.filter(id=m):
            customer = Customer.objects.get(id=m)
            if customer.isadmin:
                category=Category.objects.all()
                return  render(request,'store/admin_product_add.html',{'category':category})
            else:
                return redirect('store:home')
        return  redirect('store:home')
    def post(self,request):
        name = request.POST.get('name')
        category1 = request.POST.get('category')
        stock = request.POST.get('stock')
        image = request.POST.get('fileInput')
        price = request.POST.get('Price')
        print((category1, price,stock, image, name))
        cate=Category.objects.get(name=category1)

        product=Product(name=name,instock=stock,image=image,price=price,category=Category(id=cate.id))
        product.save()
        return  redirect('store:home')
def product_delete(request):
    message="Xoa Thanh Cong"
    name = request.GET.get('name')
    print('ten la ',name)
    product = Product.objects.get(name=name)
    product.delete()
    return redirect('store:manage1')