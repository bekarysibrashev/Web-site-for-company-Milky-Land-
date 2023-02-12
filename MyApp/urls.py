from django.urls import path
from .views import HomeView, OurLocationView, ProductsView, AboutUsView, DiscountView, ClubView  #ChosenProductView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product_line', ProductsView.as_view(), name='product_line'),
    path('about_us', AboutUsView.as_view(), name='about_us'),
    path('category', ProductsView.as_view(), name='category'),
    path('locations', OurLocationView.as_view(), name='our_location'),
    path('discount', DiscountView.as_view(), name='discount'),
    path('club', ClubView.as_view(), name='club'),
    # path('<slug>', ChosenProductView.as_view(), name='product'),
]