from django.db import models
from django.utils import timezone




class Today(models.Model):
    death = models.TextField()
    serious = models.TextField()
    new_hospitalization = models.TextField()
    confirmed = models.TextField()
    update_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.confirmed}'
    class Meta:
        db_table = 'today'

class Week_avg(models.Model):
    death = models.TextField()
    serious = models.TextField()
    new_hospitalization = models.TextField()
    confirmed = models.TextField()
    update_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.confirmed}'
    class Meta:
        db_table = 'week'

