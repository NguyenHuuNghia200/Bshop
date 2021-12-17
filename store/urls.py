from django.urls import path
from store.views.store import home,Index1
from store.views.login import Login,logout
from store.views.signup import Signup
from store.views.cart import Cart
from store.views.orders import OrderView
from store.views.checkout import checkout
from store.views.admin_order import admin_orders
from store.views.admin_product import admin_product,product_edit,product_delete,product_add
app_name='store'
urlpatterns = [
    path('', Index1.as_view(), name='homepage'),
    path('home/',home.as_view(),name='home'),
    path('login/',Login.as_view(),name='login'),
    path('signup/',Signup.as_view(),name='signup'),
    path('logout/',logout,name='logout'),
    path('check-out', checkout.as_view() , name='checkout'),
    path('cart/',Cart.as_view(),name='cart'),
    path('orders', (OrderView.as_view()), name='orders'),
    path('manage_order/', (admin_orders.as_view()), name='manage'),
    path('manage_product/', (admin_product.as_view()), name='manage1'),
    path('product_edit/',product_edit.as_view(),name='order_edit'),
    path('product_add/',product_add.as_view(),name='product_add'),
    path('product_delete/',product_delete,name='product_add')
]