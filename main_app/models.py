from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
SERVING=[
    ('6/2','6 inch 2 layers/ serves 8-12 '),
    ('6/3', '6 inch 3 layers/ serves 12-15'),
    ('8/2', '8 inch 2 layers/ serves 14-20'),
    ('8/3', '8 inch 3 layers/ serves 18-20'),

    ('10/2', '10 inch 2 layers/ serves 20-32'),
    ('10/3', '10 inch 3 layers/ serves 20-32'),
]
FILLINGS=[
    ('FROSTING','Frosting'),
    ('MOOSE', 'Moose'),
    ('OREO', 'Oreo Crumbles'),
    ('FRUIT','Fruit'),
]
FROSTING=[
    ('BUTTERCREAM','Buttercream'),
    ('CREAM CHEESE','Cream Cheese'),
    ('WHIPPED','Whipped Cream'),
]
ADD_ONS=[
    ('DRIP','Drip Cake'),
    ('CHOCOSTRAW', 'Chocolate Covered Strawberries'),
    ('SPRINKLES','Sprinkles'),
    ('SUPRISE','Suprise Inside',)
]

class Ingredient(models.Model):
    serving_size= models.CharField(
        max_length=20,
        choices=SERVING,
        default=SERVING[0][0],
        verbose_name='Serving Size',
        )
    filling= models.CharField(
        max_length=20,
        choices=FILLINGS,
        default=FILLINGS[0][0],
        verbose_name='Filling',
        )
    frosting= models.CharField(
        max_length=20,
        choices=FROSTING,
        default=FROSTING[0][0],
        verbose_name='Frosting',
        )
    addons= models.CharField(
        max_length=20,
        choices=ADD_ONS,
        default=ADD_ONS[0][0],
        verbose_name='Add Ons',
        )
    additional=models.CharField(max_length=100)

    
class Baked_Goods(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    ingredients= models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to='bakedgoods', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("detail", kwargs={'bakedgood_id': self.id})
    
    def bakedgoods(instance,filename):
        return 'user_{0}/{1}'.format(instance.user.id,filename)
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True, related_name='customer')
    email=models.EmailField(max_length=70)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True, null=True)
    date = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=30, default='Pending')
    order_status = models.BooleanField(null=True, blank=False, default=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_shoppingcart_total(self):
        orderitems=self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems])
        return total

class OrderItem(models.Model):
    item=models.ForeignKey(Baked_Goods,on_delete=models.SET_NULL,blank=True, null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
    date=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total= self.item.price
        return total

