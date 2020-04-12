# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Salesreport(models.Model):
    salespersonid = models.IntegerField(db_column='SalesPersonID', blank=True, null=True)  # Field name made lowercase.
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
