from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=False)
    position = models.IntegerField()

    def __str__(self):
        return self.name
