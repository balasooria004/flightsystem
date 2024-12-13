from django.db import models

# Create your models here.
class FLIGHT(models.Model):
    flt_id = models.AutoField(primary_key=True)
    flt_name = models.CharField(max_length=20)
    flt_from = models.CharField(max_length=20)
    flt_to = models.CharField(max_length=20)
    flt_duration = models.IntegerField()
    