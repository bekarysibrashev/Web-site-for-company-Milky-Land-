from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *
from django.http import Http404


class HomeView(View):
    def get(self, request):
        info = Info.objects.all()
        news = News.objects.all()
        carusel = ImagesOfCarusel.objects.all()
        return render(request, 'MyApp/index.html', context={
            'info': info, 'carusel': carusel, 'news': news
        })


class ProductsView(View):
    def get(self, request):
        products = Products.objects.all()
        category = Categories.objects.all()

   
        if 'Milk' in request.GET:
            
            products = Products.objects.filter(category=1)
            return render(request, 'MyApp/product_line.html', context={
            'products':products
            })  

        elif 'all' in request.GET:
            products = Products.objects.all()
            category = Categories.objects.all()
            return render(request, 'MyApp/product_line.html', context={
            'products':products
            })

        elif 'Kefir' in request.GET:
        
            products = Products.objects.filter(category=5)
            return render(request, 'MyApp/product_line.html', context={
            'products':products
            })  

        elif 'Cmetana' in request.GET:
        
            products = Products.objects.filter(category=2)
            return render(request, 'MyApp/product_line.html', context={
            'products':products
            })  
        
        elif 'Tvorog' in request.GET:
        
            products = Products.objects.filter(category=10)
            return render(request, 'MyApp/product_line.html', context={
            'products':products
            })  

        elif 'Kyrt' in request.GET:
        
            products = Products.objects.filter(category=7)
            return render(request, 'MyApp/product_line.html', context={
            'products':products
            })  

        # elif 'Macca' in request.GET:
        
        #     products = Products.objects.filter(category=8)
        #     return render(request, 'MyApp/product_line.html', context={
        #     'products':products
        #     })  


        elif 'Maclo' in request.GET:
        
            products = Products.objects.filter(category=9)
            return render(request, 'MyApp/product_line.html', context={
            'products':products
            })  


        elif 'Uogyrt' in request.GET:
    
            products = Products.objects.filter(category=4)
            return render(request, 'MyApp/product_line.html', context={
            'products':products
            })  


        else:
            return render(request, 'MyApp/product_line.html', context={
                'products':products
            })  




""" НА СЛУЧАЙ ЕСЛИ НАДО БУДЕТ ДОБАВИТЬ ОПИСАНИЕ КАЖДОГО ТОВАРА ПО ОТДЕЛЬНОСТИ """     


# class ChosenProductView(View):
#     def get(self, request, slug):
#         chosenproduct = get_object_or_404(Products, url=slug)
#         try:
#             all_products = Products.objects.all()
#             chosenproduct = Products.objects.get(url=slug)   
#         except Products.DoesNotExist:
#             raise Http404   
#         return render(request, 'MyApp/details.html', context={
#             'all_products': all_products, 'chosenproduct': chosenproduct
#         })


class AboutUsView(View):
    def get(self, request):
        return render(request, 'MyApp/about_us.html')


class OurLocationView(View):
    def get(self, request):
        return render(request, 'MyApp/our_location.html')


class DiscountView(View):
    def get(self, request):
        return render(request, 'MyApp/discount.html')

        
class ClubView(View):
    def get(self, request):
        return render(request, 'MyApp/club.html')

        