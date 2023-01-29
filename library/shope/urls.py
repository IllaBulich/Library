
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('<id>/<slug>/', views.product_detail, name='product_detail'), 
    path('', views.product_list, name='product_list'),
]
