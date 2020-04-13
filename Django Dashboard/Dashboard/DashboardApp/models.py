from django.db import models

# Create your models here.

class SalesReport(models.Model):
    salespersonid = models.IntegerField(blank=True,null=True)  # Field name made lowercase.
    fullname = models.CharField( max_length=152, blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField( max_length=50,null=True)  # Field name made lowercase.
    salesterritory = models.CharField( max_length=50,null=True)  # Field name made lowercase.
    number_2011 = models.DecimalField( max_digits=19, decimal_places=4, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2012 = models.DecimalField( max_digits=19, decimal_places=4, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2013 = models.DecimalField( max_digits=19, decimal_places=4, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2014 = models.DecimalField( max_digits=19, decimal_places=4, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.


    def __str__(self):
        return self.fullname

    # class Meta:
    #     managed = False
    #     db_table = 'SalesReport'
    class Meta:
        ordering = ['fullname']