from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=20)
    rank = models.IntegerField(default=0)

    def __str__ (self):
        return self.country_name


class Player(models.Model):
    country = models.ForeignKey(Country)
    sur_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    clubname = models.CharField(max_length=200)
    position = models.CharField(max_length=64)
    birth_date = models.DateField()

    def __str__ (self):
        return self.full_name

class Match(models.Model):
    country_A = models.ForeignKey(Country, related_name='country_A')
    country_B = models.ForeignKey(Country, related_name='country_B')
    score = models.CharField(max_length=64)

    def __str__ (self):
        return country_A + " " + country_B + " " + score
