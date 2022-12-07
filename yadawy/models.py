import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    
    
    
    
    
class Category(models.Model):
    category_id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=100)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
class Product(models.Model):
    product_id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=100)
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    qty = models.IntegerField()
    discount = models.IntegerField()
    old_price = models.FloatField()
    new_price = models.FloatField()
    main_image = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    
    

    
    
order_status = (('pending', 'pending'), ('preparing', 'preparing'), ('shipping', 'shipping'), ('delivered', 'delivered'), ('cancelled', 'cancelled'))
    
class Order(models.Model):
    order_id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.ManyToManyField(Product, related_name='details', through='OrderDetail')
    status = models.CharField(max_length=100, choices=order_status)
    date = models.DateField()
    
    
    
class OrderDetail(models.Model):
    detail_id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    
