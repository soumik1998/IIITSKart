from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(storage='/media/profile', default='profile/default-user.png')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=70)
    report_count = models.IntegerField(default=0)
    blacklist = models.BooleanField(default=False)

    created_on = models.DateTimeField(default=datetime.now(), blank=False)
    created_by = models.CharField(default="User", max_length=20, blank=False)
    modified_by = models.CharField(default="User Modified", max_length=20, blank=False)
    modified_on = models.DateTimeField(default=datetime.now(), blank=False)

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
    rating = models.IntegerField(default=0)
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
    price = models.FloatField()
    pro_pic = models.ImageField(storage='/media/product', default='product/product_default.png')
    c_id = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    cat_id = models.ForeignKey(category, on_delete=models.CASCADE, null=True)

    created_on = models.DateTimeField(default=datetime.now(), blank=False)
    created_by = models.CharField(default="User", max_length=20, blank=False)
    modified_by = models.CharField(default="User Modified", max_length=20, blank=False)
    modified_on = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.title


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(default=datetime.now(), blank=False)
    customer_id = models.ForeignKey(customer, related_name='customer', on_delete=models.CASCADE, null=True)
    seller_id = models.ForeignKey(customer, related_name='seller', on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, null=True)
    unitprice = models.FloatField(null=True, default=0)
    quantity = models.IntegerField(null=True, default=0)
    total_amount = models.FloatField(null=True, default=0)
    status = models.IntegerField(default=-1, null=False)

    created_on = models.DateTimeField(default=datetime.now(), blank=False)
    created_by = models.CharField(default="User", max_length=20, blank=False)
    modified_by = models.CharField(default="User Modified", max_length=20, blank=False)
    modified_on = models.DateTimeField(default=datetime.now(), blank=False)
    var = "Order"

    def __str__(self):
        return self.var


class p_review(models.Model):
    rating = models.IntegerField(default=0)
    text = models.TextField()
    pro_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class profile_history(models.Model):
    c_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class search_history(models.Model):
    c_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    searchtext = models.CharField(max_length=20)

    def __str__(self):
        return self.searchtext


class user_wishlist(models.Model):
    c_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    wish = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    var = "wishlist"

    def __str__(self):
        return self.var


