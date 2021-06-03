from django.contrib.auth import SESSION_KEY
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .forms import OrderForm

# Create your views here.



def base(request):      #   Base template / Базовый шаблон 

    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    sub_category_navbar = sub_category.objects.all
    catigories_navbar = category.objects.all
    form = OrderForm()

    context = {
        'sub_category_navbar' : sub_category_navbar,
        'catigories_navbar' : catigories_navbar,
        'form': form,
        'error': error,
    }

    return render(request, 'main/base.html', context = context)




def index(request):     #   main template / Домашняя страница
    sub_category_navbar = sub_category.objects.all
    catalog_mainpage = catalog.objects.order_by('-id')[:8]
    furnite_mainpage = Furnite.objects.order_by('-id')[:8]
    catigories_navbar = category.objects.all
    furnite_navbar = Furnite_category.objects.all
    furnite_sub_category_navbar = Furnite_sub_category.objects.all
    news = News.objects.order_by('-id')[:2]

    context = {
        'sub_category_navbar':sub_category_navbar,
        'catalog_mainpage':catalog_mainpage,
        'furnite_mainpage':furnite_mainpage,
        'catigories_navbar':catigories_navbar,
        'news':news,
    }

    return render(request, 'main/index.html', context=context)




def order(request):     #   size template / Страница оформления замеров

    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    sub_category_navbar = sub_category.objects.all
    catigories_navbar = category.objects.all
    cart_catalog = catalog.objects.order_by('-id')
    form = OrderForm()

    context = {
        'sub_category_navbar' : sub_category_navbar,
        'catigories_navbar' : catigories_navbar,
        'catalog': cart_catalog,
        'form': form,
        'error' : error,
    }

    return render(request, 'main/order.html', context = context)



def news(request):

    sub_category_navbar = sub_category.objects.all
    catigories_navbar = category.objects.all
    news = News.objects.order_by('-id')

    context = {
        'sub_category_navbar' : sub_category_navbar,
        'catigories_navbar' : catigories_navbar,
        'news' : news,
    }

    return render(request, 'main/news.html', context = context)



def show_post(request, post_slug):      #   door post template / Страница товара (дверь)

    post = get_object_or_404(catalog, slug=post_slug)
    catalog_post = catalog.objects.all
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)

    context = {
        'post' : post,
        'catalog_post' : catalog_post,
        'catigories_navbar' : catigories_navbar,
        'sub_category_navbar' : sub_category_navbar,
    }

    return render(request, 'main/post.html', context=context)




def show_furnite(request, furnite_slug):        #   furnite post template / Страница товара (фурнитура)

    furnite = get_object_or_404(Furnite, slug=furnite_slug)
    furnite_post = Furnite.objects.all
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all

    context = {
        'furnite' : furnite,
        'furnite_post' : furnite_post,
        'catigories_navbar' : catigories_navbar,
        'sub_category_navbar' : sub_category_navbar,
    }

    return render(request, 'main/furnite.html', context = context)




def show_category(request, category_slug):      #   category list / Список товара одной категории (двери)

    incategory = get_object_or_404(category, slug=category_slug)
    category_catalog = catalog.objects.filter(category_id = incategory.id).order_by('-id')

    paginator = Paginator(category_catalog, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all

    context = {
        'page_obj' : page_obj,
        'incategory' : incategory,
        'category_catalog' : category_catalog,
        'catigories_navbar' : catigories_navbar,
        'sub_category_navbar' : sub_category_navbar,
    }

    return render(request, 'main/category.html', context = context)



def show_furnite_category(request, furnite_category_slug):      #   furnite category list / список товара одной категории (фурнитура)

    incategory = get_object_or_404(Furnite_category, slug=furnite_category_slug)
    furnite = Furnite.objects.filter(category_id = incategory.id)
    category_catalog = catalog.objects.order_by('-id')
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all
    furnite_navbar = Furnite_category.objects.all
    furnite_sub_category_navbar = Furnite_sub_category.objects.all

    paginator = Paginator(furnite, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    

    context = {
        'page_obj' : page_obj,
        'incategory' : incategory,
        'furnite' : furnite,
        'category_catalog' : category_catalog,
        'catigories_navbar' : catigories_navbar,
        'sub_category_navbar' : sub_category_navbar,
        'furnite_navbar' : furnite_navbar,
        'furnite_sub_category_navbar' : furnite_sub_category_navbar
    }

    return render(request, 'main/furnite_category.html', context = context)




def show_sub_category(request, sub_category_slug):      #   sub_category list / Список товара одной подкатегории (двери)

    subcategory = get_object_or_404(sub_category, slug=sub_category_slug)
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all
    subcategory_catalog = catalog.objects.filter(sub_category_id = subcategory.id)
    collections = collection.objects.all
    
    paginator = Paginator(subcategory_catalog, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'subcategory' : subcategory,
        'catigories_navbar' : catigories_navbar,
        'sub_category_navbar' : sub_category_navbar,
        'subcategory_catalog' : subcategory_catalog,
        'collections' : collections,
    }

    return render(request, 'main/subcategory.html', context = context)



def show_collection(request, collection_slug):

    incollections = get_object_or_404(collection, slug=collection_slug)
    subcategory = sub_category.objects.all
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all
    collections = collection.objects.all
    collections_catalog = catalog.objects.filter(collection_id = incollections.id)
    

    paginator = Paginator(collections_catalog, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'incollections' : incollections,
        'subcategory' : subcategory,
        'catigories_navbar' : catigories_navbar,
        'sub_category_navbar' : sub_category_navbar,
        'collections_catalog' : collections_catalog,
        'collections' : collections,
    }

    return render(request, 'main/collection.html', context = context)



def show_furnite_subcategory(request, furnite_subcategory_slug):

    subcategory = get_object_or_404(Furnite_sub_category, slug=furnite_subcategory_slug)
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all
    furnite_navbar = Furnite_category.objects.all
    furnite_sub_category_navbar = Furnite_sub_category.objects.all
    subcategory_catalog = catalog.objects.order_by('-id')
    furnite = Furnite.objects.filter(sub_category_id = subcategory.id)
    
    paginator = Paginator(furnite, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'subcategory' : subcategory,
        'catigories_navbar' : catigories_navbar,
        'sub_category_navbar' : sub_category_navbar,
        'subcategory_catalog' : subcategory_catalog,
        'subcategory_catalog' : subcategory_catalog
    }

    return render(request, 'main/furnite_subcategory.html', context = context)




def all_furnite(request):

    sub_category_navbar = sub_category.objects.all
    furnite_allpage = Furnite.objects.order_by('-id')
    catigories_navbar = category.objects.all
    furnite_navbar = Furnite_category.objects.all
    furnite_sub_category_navbar = Furnite_sub_category.objects.all

    paginator = Paginator(furnite_allpage, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'sub_category_navbar':sub_category_navbar,
        'furnite_allpage':furnite_allpage,
        'catigories_navbar':catigories_navbar,
        'furnite_navbar':furnite_navbar,
        'furnite_sub_category_navbar':furnite_sub_category_navbar
    }

    return render(request, 'main/all_furnite.html', context = context)