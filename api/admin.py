from django.contrib import admin
from .models import Product, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
#     list_display = ('order', 'product', 'quantity', 'item_subtotal')
#     search_fields = ('order__order_id', 'product__name')
#     list_filter = ('order', 'product')

# admin.site.register(OrderItem, OrderItemAdminInline)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'stock', 'in_stock')
#     search_fields = ('name', 'description')
#     list_filter = ('stock',)    
    
# admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    # list_display = ('order_id', 'user', 'status', 'total_items', 'created_at')
    # list_filter = ('status', 'created_at')
    # search_fields = ('order_id', 'user__username')
    inlines = [OrderItemInline]
    
admin.site.register(Order, OrderAdmin)
