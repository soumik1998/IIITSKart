from django.contrib import admin

from .models import customer , c_review , login , super_user , category , product , p_review

admin.site.register(customer)
admin.site.register(c_review)
admin.site.register(login)
admin.site.register(super_user)
admin.site.register(category)
admin.site.register(product)
admin.site.register(p_review)


# Register your models here.
