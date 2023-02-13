from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import *
from .forms import OrderForm



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
    else:
        items=[]
        order={'get_shoppingcart_total':0}
    context={'items': items,'customer':customer,'order':order}
    return render(request, 'bakedgoods/cart.html',context)