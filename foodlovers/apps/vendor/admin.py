from django.contrib import admin
from .models import Address, Vendor, OpeningHour

admin.site.register(Address)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('user','vendor_name','image', 'address','is_approved', 'created_at')
    list_display_links = ('user', 'vendor_name')
    list_editable = ('is_approved',)


class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'day', 'from_hour', 'to_hour')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(OpeningHour, OpeningHourAdmin)