from django.shortcuts import render, redirect
from .models import Baked_Goods


def home(request):
    return render(request, 'home.html')
def index(request):
    bakedgoods=Baked_Goods.objects.all()
    return render(request,'bakedgoods/index.html', {'bakedgoods':bakedgoods} )