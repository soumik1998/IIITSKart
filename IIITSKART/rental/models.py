from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cart.models import customer

# Create your models here.


class item_type(models.Model):
    type = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.type


class items(models.Model):
    title = models.CharField(max_length=60, null=False)
    description = models.CharField(max_length=60, null=False)
    type_id = models.ForeignKey(item_type, on_delete=models.CASCADE)
    rental_price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    rate=models.FloatField(default=0)
    days=models.FloatField(default=1)
    pro_pic = models.ImageField(storage='/media/product', default='product/product_default.png')
    sold_by = models.ForeignKey(customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class rent_details(models.Model):
    c_id = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='RentedBy')
    rented_by = models.ForeignKey(customer, on_delete=models.CASCADE, related_name="Rented")
    item_pro = models.ForeignKey(item, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    rented_on = models.DateTimeField(default=datetime.now(), blank=False)
    return_date = models.DateTimeField(default=datetime.now(), blank=False)

    created_on = models.DateTimeField(default=datetime.now(), blank=False)
    created_by = models.CharField(default="User", max_length=20, blank=False)
    modified_by = models.CharField(default="User Modified", max_length=20, blank=False)
    modified_on = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.DoesNotExist

