from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    name=models.CharField(max_length=150)
    desc=models.TextField()
    category=models.CharField(max_length=100)
    price_before=models.DecimalField(max_digits=10,decimal_places=2,null=True,default="")
    price=models.DecimalField(max_digits=10,decimal_places=2)
    added_date=models.DateField()
    image=models.ImageField(upload_to='shop/products_images')

    def __str__(self):
        return self.name

class customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class order(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    date_of_order=models.DateField()
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return self.product.name

    @property
    def total(self):
        total=self.quantity * self.product.price
        return total
        

