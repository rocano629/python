from django.db import models

# Create your models here.

class Salesreport(models.Model):
    salespersonid = models.IntegerField(db_column='SalesPersonID', blank=True, primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=152, blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=50)  # Field name made lowercase.
    salesterritory = models.CharField(db_column='SalesTerritory', max_length=50)  # Field name made lowercase.
    number_2011 = models.DecimalField(db_column='2011', max_digits=19, decimal_places=4, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2012 = models.DecimalField(db_column='2012', max_digits=19, decimal_places=4, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2013 = models.DecimalField(db_column='2013', max_digits=19, decimal_places=4, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2014 = models.DecimalField(db_column='2014', max_digits=19, decimal_places=4, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'SalesReport'