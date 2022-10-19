from django.contrib import admin
from information.models import Information

class InformationAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'company_name', 'product_category', 'product_description', 'product_cost', 'manu_date', 'exp_date', 'qr_code')

admin.site.register(Information, InformationAdmin)

# Register your models here.
