from django.contrib import admin # type: ignore
from .models import Category, Computer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display category name

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'category', 'purchase_date', 'support_expiration_date', 'is_support_active')
    list_filter = ('category', 'support_expiration_date')  # Add filters for categories and expiration dates
    search_fields = ('name', 'client__name')  # Search by computer name and client name
    ordering = ('support_expiration_date',)  # Order by expiration date
    
    # Adding a method to display if support is active
    @admin.display(boolean=True, description='Support Active')
    def is_support_active(self, obj):
        return obj.is_support_active()
# Register your models here.
