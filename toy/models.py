from django.db import models


# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=10)
    textfield1 = models.TextField()
    datetimefield1 = models.DateField()

    def __str__(self):
        return self.name
