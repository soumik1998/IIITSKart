from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=70,blank=False, null= True, unique= True)
    phone = models.IntegerField()
    address = models.TextField(max_length=70)
    blacklist = models.CharField(max_length=10)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.email


class c_review(models.Model):
    rating=models.IntegerField()
    text=models.TextField()
    c_id = models.ForeignKey(customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.text    


class login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=70,blank=True, null= True, unique= True)
    created=models.DateTimeField('date published',null=True)
    modified=models.DateTimeField('date published',null=True)
    
    c_id=models.ForeignKey(customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username


class super_user(models.Model):
    username=models.CharField(max_length=20)
    a_id=models.ForeignKey(login, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class product(models.Model):
    p_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    quantity=models.IntegerField()
    description=models.TextField()
    c_id=models.ForeignKey(customer, on_delete=models.CASCADE,null=True)
    cat_id=models.ForeignKey(category, on_delete=models.CASCADE,null=True, related_name='+')

    def __str__(self):
        return self.title

class p_review(models.Model):
    rating=models.IntegerField()
    text=models.TextField()
    pro_id=models.ForeignKey(product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    
    

    
    
    
    
    
    
    
    
