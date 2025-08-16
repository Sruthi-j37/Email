from django.db import models


# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    email=models.EmailField()
