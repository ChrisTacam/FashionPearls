from django.db import models
from provider.models import Provider
from product.models import Product


class Compras(models.Model):
    provider = models.ForeignKey(Provider, null=True)
    invoice = models.CharField('invoice', max_length=10, null=True)
    date = models.DateTimeField('date', auto_now_add=True)
    product = models.ManyToManyField(Product, through='Detalle_Compra')

    def __unicode__(self):
        return self.invoice

class Detalle_Compra(models.Model):
    invoice = models.ForeignKey(Compras)
    product = models.ForeignKey(Product)
    cantidad = models.DecimalField(max_digits = 10 , decimal_places = 2, null=True)
    precio = models.DecimalField(max_digits = 10 , decimal_places = 2, null=True)

    def Sub_Compra(self):
        total = (self.cantidad*self.precio)
        return total


# Create your models here.
