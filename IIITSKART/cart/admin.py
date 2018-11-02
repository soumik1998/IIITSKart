from django.contrib import admin

from .models import customer, c_review, category, Product , p_review, Order, user_wishlist, seller_report,search_history

admin.site.register(customer)
admin.site.register(c_review)
# admin.site.register(login)
# admin.site.register(super_user)
admin.site.register(category)
admin.site.register(Product)
admin.site.register(p_review)
admin.site.register(Order)
admin.site.register(user_wishlist)
admin.site.register(seller_report)
admin.site.register(search_history)


# Register your models here.
