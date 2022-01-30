from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'), #views
    path('item/<slug:slug>/', views.product_detail, name='product_detail'), # dattype: ver(slug-url)
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),   #search/shirts -- show all shirtrs in the category
]