from django.contrib import admin
from .models import *

# Register your models here.


class cat_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,cat_admin)

class prod_admin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','img']
    list_editable = ['price','stock','img']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(products,prod_admin)