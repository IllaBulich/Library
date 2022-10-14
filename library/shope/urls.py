
from django.urls import path,re_path
from . import views

urlpatterns = [
    # re_path(r'^$', views.index , name="main"),
    path('create/', views.create, name="create"),
    
    re_path(r'^$', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'), 
]
