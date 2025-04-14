from django.contrib import admin
from .models import ContactUs

# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    search_fields = ('name', 'email', 'subject')

admin.site.site_header = "ZAM Group Admin"
admin.site.site_title = "ZAM Portal"
admin.site.index_title = "Welcome to ZAM Group's Admin"
