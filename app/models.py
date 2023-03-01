from django.db import models

# Create your models here.
class student(models.Model):
    st_id=models.IntegerField(primary_key=True)
    st_name=models.CharField(max_length=100)
    st_age=models.IntegerField()
class poultryform(models.Model):
    S_no=models.IntegerField(primary_key=True)
    Big_chiken=models.IntegerField()
    small_chiken=models.IntegerField()
    total_cost=models.IntegerField()
