from django.contrib import admin
from shopping.models import Buy, Purchase_Detail


class Purchase_Online(admin.TabularInline):
    model = Purchase_Detail
    extra = 1


class PurchaseAdmin(admin.ModelAdmin):
    model = Purchase_Detail
    list_display = ('invoice',)
    inlines = (Purchase_Online,)
    raw_id_fields = ('provider',)

admin.site.register(Buy, PurchaseAdmin)
admin.site.register(Purchase_Detail)

# Register your models here.
