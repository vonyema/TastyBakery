from django.db import models
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
    additonal=models.CharField(max_length=100)

    
class Baked_Goods(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    ingredients= models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to='bakedgoods', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name
    def bakedgoods(instance,filename):
        return 'user_{0}/{1}'.format(instance.user.id,filename)
class Order(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.EmailField(max_length=70)
    phone = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now = True)
    baked_goods = models.ForeignKey(Baked_Goods,on_delete = models.CASCADE)
    status = models.CharField(max_length=30, default='Pending')
    order_status = models.CharField(max_length=30, default='True')

    def __str__(self):
        return self.name


