from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('base', views.base, name='base'),
    #path('items', views.all_items, name='all_items'),
    path('',views.index, name='home'),
    path('size', views.sizes, name='sizes'),
    path('news', views.news, name='news'),
    path('all_furnite', views.all_furnite, name='all_furnite'),
    path('post/<slug:post_slug>', views.show_post, name="post"),
    path('category/<slug:category_slug>', views.show_category, name='category'),
    path('sub_category/<slug:sub_category_slug>', views.show_sub_category, name='sub_category'),
    path('furnite/<slug:furnite_slug>', views.show_furnite, name='furnite'),
    path('furnite_category/<slug:furnite_category_slug>', views.show_furnite_category, name='furnite_category'),
    path('collection/<slug:collection_slug>', views.show_collection, name='collection')
]
