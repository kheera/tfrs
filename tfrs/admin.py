from django.contrib import admin

from .models import FuelSupplier, FuelClass, FuelType, Province, TradingPartner, Transaction, TransactionType



admin.site.register(FuelSupplier)
admin.site.register(FuelClass)
admin.site.register(FuelType)
admin.site.register(Province)
admin.site.register(TradingPartner)
admin.site.register(Transaction)
admin.site.register(TransactionType)