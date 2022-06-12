from django.contrib import admin
from .models import Group, Warehouse, Product, ProductInstance
# Register your models here.

class ProductInstanceInline(admin.TabularInline):
    model=ProductInstance

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','group')
    list_filter=['group']
    inlines=[ProductInstanceInline]


class WarehouseAdmin(admin.ModelAdmin):
    list_display=('name','location')
    list_filter=['location']

class ProductInstanceAdmin(admin.ModelAdmin):
    list_display=('product','quantity','warehouse')
    list_filter=['warehouse','product']
    fieldsets=(
        ('Product Details',{'fields':['product','quantity']}),
        ('Warehouse Details',{'fields':['warehouse']})
    )


admin.site.register(Group)
admin.site.register(Warehouse,WarehouseAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductInstance,ProductInstanceAdmin)
