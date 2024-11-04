from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'subject', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'subject')
    ordering = ('-created_at',)
    list_filter = ('created_at',)

    def has_delete_permission(self, request, obj=None):
        # Optionally customize delete permissions
        return True

    def has_change_permission(self, request, obj=None):
        # Optionally customize change permissions
        return True
