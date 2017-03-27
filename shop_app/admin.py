from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Order
from django.contrib.auth.admin import UserAdmin

from extuser.models import ExtUser
# Register your models here.


class ExtUserAdmin(admin.ModelAdmin):
    exclude = ('groups',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(ExtUser, ExtUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)

admin.site.unregister(Group)
