from django.contrib import admin

# Register your models here.
from .models import items,rent_details,item_type
admin.site.register(item_type)
admin.site.register(items)
admin.site.register(rent_details)
