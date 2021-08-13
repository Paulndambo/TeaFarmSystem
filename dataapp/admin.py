from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Farmer)
admin.site.register(Staff)
admin.site.register(Delivery)
admin.site.register(PayFarmer)

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ("farmer", "total_quantity_delivered", "total_cumulative_amount", "year")
