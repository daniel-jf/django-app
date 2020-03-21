from django.db import models
from datetime import date
from django.urls import reverse

WHERES = (
    ('T', 'Yes, there'),
    ('NT', 'No, not there'),
    ('WT', 'Was there earlier')
)
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('locations_detail', kwargs={'pk': self.id})

class Homie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    age = models.IntegerField()
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.name
    
    def saw_today(self):
        return self.saw_set.filter(date=date.today()).count() >= len(WHERES)

class Saw(models.Model):
    date = models.DateField('Date Seen')
    where = models.CharField(
        max_length=2,
        choices=WHERES,
        default=WHERES[0][0]
    )
    homie = models.ForeignKey(Homie, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.get_where_display()} on {self.date}'

    class Meta:
        ordering = ['-date']