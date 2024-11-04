from django.contrib import admin
from .models import TeamMember


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('name',)  # Fields to search in the admin
    ordering = ('created_at',)  # Default ordering of the list view
    list_filter = ('created_at',)  # Fields to filter the list view


admin.site.register(TeamMember, TeamMemberAdmin)

