from django.db import models

class Person(models.Model):
    ism=models.CharField(max_length=35)
    age=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism

