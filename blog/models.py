from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=75)
    conthead1 =  models.CharField(max_length=1000)
    heading2 = models.CharField(max_length=75)
    conthead2 = models.CharField(max_length=1000)
    heading3 = models.CharField(max_length=75)
    conthead3  = models.CharField(max_length=1000)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=60,default="")
    image = models.ImageField(upload_to="blog/images",default="")
    pub_date = models.DateField()
    publisher = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.publisher + "--" +self.title + "--" + str(self.post_id)