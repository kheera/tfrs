import datetime

from django.db import models
from django.utils import timezone



class FuelClass(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
	
    class Meta:
        verbose_name_plural = "fuel classes"

		
class FuelType(models.Model):
    fuel_class = models.ForeignKey(FuelClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class FuelSupplier(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FuelSupply(models.Model):
    fuel_supplier = models.ForeignKey(FuelSupplier, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    supply_year = models.DateField('year')
    last_modified = models.DateField(auto_now=True)

class Province(models.Model):
    name = models.CharField(max_length=300)
    short = models.CharField(max_length=2)
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.name

class TradingPartner(models.Model):
    name = models.CharField(max_length=1000)
    street1 = models.CharField(max_length=300, blank=True)
    street2 = models.CharField(max_length=300, blank=True)
    postal = models.CharField(max_length=6, blank=True)
    city = models.CharField(max_length=300, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class TransactionType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    trader = models.ForeignKey(TradingPartner, related_name="+", on_delete=models.CASCADE) #related_name="+" means TradingPartners table won't be linked back to this one.
    trading_partner = models.ForeignKey(TradingPartner, related_name="+", on_delete=models.CASCADE)
    type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    market_value = models.DecimalField(max_digits=17, decimal_places=2) # Max digits is based on BC GDP (2014) of $237,188,000,000,000.
    compliance_period = models.CharField(max_length=100)
    credit = models.IntegerField()
    status = models.CharField(max_length=100) # should be enum field, values: draft, waiting approval, authorized, approved, rejected, complete
