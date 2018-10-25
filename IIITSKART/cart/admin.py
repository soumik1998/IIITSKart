from django.contrib import admin

from .models import customer, c_review, category, Product , p_review, Order

admin.site.register(customer)
admin.site.register(c_review)
# admin.site.register(login)
# admin.site.register(super_user)
admin.site.register(category)
admin.site.register(Product)
admin.site.register(p_review)
admin.site.register(Order)


# Register your models here.
