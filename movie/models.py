from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='movies')
    year_of_production=models.DateField()
