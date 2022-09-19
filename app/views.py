from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
# from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views import View
from .models import *

class HomeView(View):

    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        print(laptops, 'laptops::::')
        context = {
            'topwears':topwears,
            'bottomwears': bottomwears,
            'mobiles': mobiles,
            'laptops': laptops
        }
        return render(request, 'app/home.html', context)
# class HomeView(TemplateView):
#     template_name = 'app/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['latest_articles'] = Article.objects.all()[:5]
#         return context


    
# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        context ={
            'product': product
        }
        return render(request, 'app/productdetail.html', context)

        
def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# def mobile(request):
#  return render(request, 'app/mobile.html')

class MobileView(View):
    def get(self, request, data=None):
        if data == None:
            mobiles = Product.objects.filter(category='M')
        elif data == 'Iphone' or data == 'Samsung':
            mobiles = Product.objects.filter(category='M').filter(brand=data)
        context ={
            'mobiles': mobiles
        }
        return render(request, 'app/mobile.html', context)

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
