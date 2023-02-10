from django.contrib import admin

# Register your models here.
from .models import Baked_Goods, Ingredient, Order
class bakedAdmin(admin.ModelAdmin):
    list_display=['name','price','image']
# register
admin.site.register(Baked_Goods, bakedAdmin)
admin.site.register(Ingredient)
admin.site.register(Order)
