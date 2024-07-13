from django.contrib import admin

# Register your models here.
from .models import user_login,customer_details
from .models import category_master,book_master
from .models import shopping_cart,payment_master,bill_details,bill_master

admin.site.register(user_login)
admin.site.register(customer_details)
admin.site.register(category_master)
admin.site.register(book_master)
admin.site.register(shopping_cart)
admin.site.register(payment_master)
admin.site.register(bill_details)
admin.site.register(bill_master)