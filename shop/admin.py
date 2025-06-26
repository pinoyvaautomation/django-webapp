from django.contrib import admin
from .models import Product, Order, OrderItem

#admin.site.register(Product)
#admin.site.register(Order)
#admin.site.register(OrderItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'quantity', 'get_total']
    readonly_fields = ['get_total']  # Display total price for each item

    def get_total(self, obj):
        return obj.get_total()
    get_total.short_description = 'Total Price'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at', 'complete', 'product_names']
    inlines = [OrderItemInline]  # Add OrderItem inline

    def product_names(self, obj):
        return ", ".join([item.product.name for item in obj.orderitem_set.all()])
    product_names.short_description = 'Products'


admin.site.register(Order, OrderAdmin)
admin.site.register(Product)


