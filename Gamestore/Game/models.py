from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):

    type= (('Action','Action'),('Adventure','Adventure'),('Sport','Sport'),('Racing','Racing'),('Survival','Survival'),('Platform','Platform'))    #PREdefined categories which we gone used in below cat model. key can be differnt if we want like ('1','Action') 


    productName = models.CharField(max_length = 50)
    description = models.CharField(max_length =200)
    manufacturer = models.CharField(max_length=50)
    cat = models.CharField(max_length = 50 , choices=type)  # we add choices from type
    price = models.IntegerField()
    is_available = models.BooleanField(default = True)
    image = models.ImageField(upload_to="images") 

    def __str__(self):
        return self.productName
    
class Cart(models.Model):

    user=models.ForeignKey(User, on_delete = models.CASCADE)
    prod =models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity=models.IntegerField(default = 1)
    total_price = models.FloatField(default=0.00)
    is_order = models.BooleanField(default= False) 

class Reviews(models.Model):

    rate = ((1,1),(2,2),(3,3),(4,4),(5,5))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    review= models.CharField(max_length=200)
    image = models.FileField(max_length=200,upload_to='image/reviewImage')
    rating = models.IntegerField(choices=rate)


class Orders(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prod = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)