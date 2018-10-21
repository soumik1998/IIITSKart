from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profile/", null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=70)
    blacklist = models.CharField(max_length=10)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()

    def __str__(self):
        return self.user.username


class c_review(models.Model):
    rating = models.IntegerField()
    text = models.TextField()
    c_id = models.ForeignKey(customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    quantity = models.IntegerField(null=False)
    description = models.TextField()
    c_id = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    cat_id = models.ForeignKey(category, on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        return self.title


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(default=datetime.now(), blank=False)
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    total_amount = models.FloatField(null=False)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    unitprice = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return "OrderItem"


class p_review(models.Model):
    rating = models.IntegerField()
    text = models.TextField()
    pro_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
