from django.contrib import admin
from totales.models import Compras,Detalle_Compra



class DetalleAdmin(admin.ModelAdmin):
    model = Detalle_Compra
    list_display = ['Sub_Compra', 'get_name']

    def get_name(self, obj):
        return obj.invoice.provider
    get_name.admin_order_field  = 'author'  #Allows column order sorting
    get_name.short_description = 'Author Name'  #Renames column head

admin.site.register(Detalle_Compra, DetalleAdmin)

class ComprasAdmin(admin.ModelAdmin):
    list_display = ('provider','invoice','date')

admin.site.register(Compras,ComprasAdmin)
# Register your models here.
