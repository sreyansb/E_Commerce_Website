from django.db import models

# Create your models here.
class Blog(models.Model):
    post_id=models.AutoField(primary_key=True)
    author=models.CharField(max_length=100,default="")
    title=models.CharField(max_length=500,default="")
    head0=models.CharField(max_length=500,default="")
    head1=models.CharField(max_length=500,default="")
    head2=models.CharField(max_length=500,default="")
    head0content=models.CharField(max_length=5000,default="")
    head1content=models.CharField(max_length=5000,default="")
    head2content=models.CharField(max_length=5000,default="")
    published_date=models.DateField()
    thumbnail=models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return str(self.post_id)
    
