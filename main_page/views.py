from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    products = models.Products.objects.all()
    categories = models.Categories.objects.all()
    sales = models.Sales.objects.all() 

    form = forms.SearchForm()

    if request.method == 'POST':
        pr_name = request.POST.get('search_bar')

        find_produkt = models.Products.objects.get(product_name= pr_name)

        return redirect(f'/product/{find_produkt}')



    return render(request, 'main_page/index.html',{'products':products, 'form':form, 'categories': categories, 'sales': sales})

#Обработак поиск товара
def get_product(request, pk):
    product_info = models.Products.objects.get(product_name=pk)

    # Добовление товаров в корзину
    if request.method == 'POST':
        # Получаем айди юзера
        get_user = User.objects.get(id=request.user.id)

        models.Cart.objects.create(user_id=get_user.id, product_name=product_info, product_count=request.POST.get('counter'))

        return redirect('/')

    return render(request,'main_page/product_info.html', {'product': product_info})
#
def get_category(request, pk):
    products_in_category = models.Products.objects.filter(product_cotegory=pk)

    return render(request, 'main_page/category_all.html', {'products_in_category':products_in_category})

# Вывод карзины по катигориям
def get_user_cart(request,pk):
    user_cart = models.Cart.objects.filter(user_id=pk)
    total = [(i.product_name.product_price * i.product_count) for i in user_cart]

    return render(request, 'main_page/cart.html',{'user_cart':user_cart,'user_total':sum(total)} )

def delete_item(request,pk):
    user_cart = models.Cart.objects.get(id=pk)
    user_cart.delete()
    return redirect('/')

def abut(request):

    return HttpResponse('Abut')

def voyti(request):

    return HttpResponse('Войти')
