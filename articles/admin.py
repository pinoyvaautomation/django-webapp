from django.contrib import admin # type: ignore
from .models import Article, Category, Tag

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ArticleAdmin(admin.ModelAdmin):
    # Display all relevant fields in the list view
    list_display = ('title', 'category', 'created_at', 'updated_at')
    
    # Allow searching by title and content
    search_fields = ('title', 'content')

    # Add filters for easy navigation
    list_filter = ('category', 'tags')

    # Enable display of tags in the list view
    filter_horizontal = ('tags',)

    # Organize fields in a fieldset for a cleaner layout in the detail view
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'content', 'category', 'tags')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Collapsible section for optional organization
        }),
    )

    # Make 'created_at' and 'updated_at' read-only to prevent manual changes
    readonly_fields = ('created_at', 'updated_at')

class CustomUserAdmin(UserAdmin):
    def get_fieldsets(self, request, obj=None):
        """
        Customize the fieldsets to replace the hashed password with asterisks.
        """
        fieldsets = super().get_fieldsets(request, obj)
        new_fieldsets = []

        for name, section in fieldsets:
            if 'password' in section.get('fields', ()):
                # Replace the 'password' field display with asterisks
                fields = tuple(
                    'password_display' if field == 'password' else field
                    for field in section['fields']
                )
                section['fields'] = fields
            new_fieldsets.append((name, section))

        return new_fieldsets

    def password_display(self, obj):
        """
        Return asterisks for the password display field.
        """
        return "********"

    password_display.short_description = "Password"

    readonly_fields = ('password_display',)  # Ensure it's read-only

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Unregister the default UserAdmin
admin.site.unregister(User)

# Register the custom UserAdmin
admin.site.register(User, CustomUserAdmin)    

# Register ArticleAdmin with the Article model
admin.site.register(Article, ArticleAdmin)
#admin.site.register(Category)
admin.site.register(Tag)