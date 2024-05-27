from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES=(
    ('Toys1','Toys1'),
    ('Toys2','Toys2'),
    ('Toys3','Toys3'),
    ('Toys4','Toys4')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    product_image = models.ImageField(upload_to='product')
    quantity=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.title

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fnmae=models.CharField(max_length=20,null=False)
    lnmae=models.CharField(max_length=20,null=False)
    email=models.EmailField()
    phone=models.CharField(max_length=20,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=20,null=False)
    state=models.CharField(max_length=20,null=False)
    country=models.CharField(max_length=20,null=False)
    pincode=models.CharField(max_length=20,null=False)
    total_price=models.FloatField(max_length=150,null=False)

    def __int__(self):
        return self.id

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __int__(self):
        return self.order.id

    




