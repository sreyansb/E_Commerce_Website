from django.db import models

# Create your models here.
class Products(models.Model):
    product_ID=models.AutoField#no parentheses
    product_name=models.CharField(max_length=100)
    desc=models.CharField(max_length=300)#could be a TextField also
    pub_date=models.DateField()
    price=models.FloatField(default=0.0)
    image=models.ImageField(upload_to="shop/images",default="")
    category=models.CharField(default="",max_length=50)
    subcategory=models.CharField(default="",max_length=50)

    def __str__(self):
        return self.product_name#admin website mein kaisa dikhega->what should be the name of an object of the model-> woh bataane ke liye we use self.product_name

class Contact(models.Model):
    msg_ID=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300,default="")#could be a TextField also
    phone=models.CharField(max_length=12,default="")
    email=models.CharField(max_length=70,default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_ID=models.AutoField(primary_key=True)
    amount=models.IntegerField(default=0)
    items_json=models.CharField(max_length=5000)#to store the items bought by the customer->It is a JSON
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=11,default="")
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=8)
    def __str__(self):
        return str(self.order_ID)

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default=0)
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateTimeField(auto_now_add=True)#to update date and time when a new record is added 

    def __str__(self):
        return self.update_desc[0:7]+"..."

