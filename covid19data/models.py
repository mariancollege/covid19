from django.db import models

class coviddata(models.Model):
    cid=models.IntegerField(default=0)
    cname=models.CharField(max_length=50,default='US')
    confirmed=models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    active = models.IntegerField(default=0)

class covidalldata(models.Model):
    alldata = models.CharField(max_length=50,  default='US')

