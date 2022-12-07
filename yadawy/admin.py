from django.contrib import admin
from .models import User, Category, Product, Order

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone']
    search_fields = ['username', 'email']
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'qty', 'old_price', 'new_price']
    search_fields = ['product_name']
    
    
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)