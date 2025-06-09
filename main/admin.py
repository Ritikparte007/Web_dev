from django.contrib import admin
from .models import ContactMessage, QuoteRequest

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'created_at', 'is_replied']
    list_filter = ['is_replied', 'subject', 'created_at']
    search_fields = ['name', 'email', 'phone', 'subject']
    readonly_fields = ['created_at']
    list_editable = ['is_replied']
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'project_type', 'budget_range', 'phone', 'created_at', 'is_processed']
    list_filter = ['project_type', 'budget_range', 'is_processed', 'created_at']
    search_fields = ['name', 'email', 'phone', 'company']
    readonly_fields = ['created_at']
    list_editable = ['is_processed']
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')