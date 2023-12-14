from django.shortcuts import render,redirect
from store.models.customer import Customer
from store.models.products import Products
from django.views import View
from django.contrib.auth.hashers import check_password

class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Products.get_products_by_id(ids)
        print(products)
        return render(request,'cart.html',{"products":products})
