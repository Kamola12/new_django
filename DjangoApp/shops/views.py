from django.shortcuts import render
from django.views import View

from shops.models import Products


# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'shops/home.html')

class ProductView(View):
    def get(self, request):
        products=Products.objects.all()
        context = {
            'products':products
        }
        return render(request, 'shops/products.html', context=context)

class ProductDetailView(View):
    def get(self, request, id):
        product=Products.objects.get(id=id)
        context={
            "product":product
        }
        return render(request, 'shops/product_detail.html', context)