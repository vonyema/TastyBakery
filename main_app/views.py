from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
import json
from django.http import JsonResponse
from .models import *
from .forms import OrderForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')
def index(request):
    bakedgoods=Baked_Goods.objects.all()
    return render(request,'bakedgoods/index.html', {'bakedgoods':bakedgoods} )
def bakedgood_detail(request, bakedgood_id):
    order_form=OrderForm()
    bakedgood= Baked_Goods.objects.get(id=bakedgood_id)
    return render(request, 'bakedgoods/detail.html',{
        'bakedgood':bakedgood,
        'order_form':order_form
    })
def add_order(request, bakedgood_id):
  # capture submitted form inputs
  form = OrderForm(request.POST)
  # validate form inputs
  if form.is_valid():
  # save a temp copy of a new feeding using the form submission
    new_order = form.save(commit=False)
  # associate the new feeding to the cat using the corresponding cat id
    new_order.bakedgood_id = bakedgood_id
  # save the new feeding to the database
    new_order.save()
  # return with a response to redirect
  # NOTE: we need to import the built-in redirect function/method
  return redirect('detail', bakedgood_id=bakedgood_id)

class OrderCreate(CreateView):
  model = Ingredient
  fields = '__all__'

def shoppingcart(request):


    if request.user.is_authenticated:
        customer=request.user.customer
        order, created= Order.objects.get_or_create(customer=customer, order_status=False )
        items= order.orderitem_set.all()
        cartItems=order.get_shoppingcart_items
    else:
        items=[]
        order={'get_shoppingcart_total':0, 'get_shoppingcart_items':0}
        cartItems=order['get_shoppingcart_items']
    context={'items': items,'customer':customer,'order':order, 'cartItems':cartItems}
    return render(request, 'bakedgoods/cart.html',context)
def addItem(request):
    data= json.loads(request.body.decode("utf-8"))
    bakedgoodId=data['bakedgoodId']
    action=data['action']
    print('Action:',action)
    print('Product:',bakedgoodId)

    customer= request.user.customer
    bakedgood= Baked_Goods.objects.get(id=bakedgoodId)
    order, created= Order.objects.get_or_create(customer=customer, order_status=False )
    orderItem, created= OrderItem.objects.get_or_create(order=order, bakedgood=bakedgood)

    orderItem.save()
    return JsonResponse('Item was added', safe=False)
class EditCart(UpdateView):
    model=Ingredient
    fields='__all__'
    success_url='/cart/'
def registerPage(request):
    form= RegisterForm()
    if request.method== 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'account/register.html', {
        'form':form
    })
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'account/login.html')
