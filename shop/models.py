from django.db import models
# NOTE : models contains essential fields and behoviour of data you are storing.Genrally,each model maps to single
#        database table 
# Create your models here.
class Product(models.Model):# to describe how to store product details.    product_id = models.AutoField # AutoField to genrate automatically.
    product_name = models.CharField(max_length=50)#to set max. length of product name.
    desc = models.CharField(max_length=400) # description of product
    pub_date = models.DateField() # date of adding product.
    price = models.IntegerField(default="0")
    category = models.CharField(max_length=50,default="")
    image = models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name # it will display product name in place of Product(no.)

class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50,default="")
    email= models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    query = models.CharField(max_length=400) 
    
    def __str__(self):
        return self.name 

class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length = 5000)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=5000)
    city = models.CharField(max_length=5000)
    state = models.CharField(max_length=5000)
    pin_code = models.CharField(max_length=5000)

    def __str__(self):
        return self.name + str(self.order_id)

class  OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key = True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=3000)        
    timestamp = models.DateField(auto_now_add = True)

    def __str__(self):
       return f"order_id {self.order_id} "+ self.update_desc[0:20] + "----"