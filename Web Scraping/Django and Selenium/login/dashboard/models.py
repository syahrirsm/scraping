from django.db import models
from django.db import connections

class EmployeeDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    link = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    class Meta:
        db_table="tb_link"
# Create your models here.
