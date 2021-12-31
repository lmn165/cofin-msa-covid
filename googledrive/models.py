from django.db import models
from django.utils import timezone




class drive(models.Model):
    date = models.DateTimeField()
    confirmed = models.TextField()

    def __str__(self):
        return f'{self.confirmed}'
    class Meta:
        db_table = 'confirmed'

