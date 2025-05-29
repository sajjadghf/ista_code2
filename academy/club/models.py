from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    birth_date = models.DateField()

    def __str__(self):
        return self.family
