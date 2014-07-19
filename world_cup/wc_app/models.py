from django.db import models


    # -------------
    # Country_model
    # -------------

class Country(models.Model):
    """
    The model contains a country name, the country code and the rank of the country.
    The __str__ method is used to return the name of the country as string.
    """

    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=20)
    rank = models.IntegerField(default=0)
    flag = models.CharField(max_length=500)
    symbol_flag = models.CharField(max_length=500)
    map_url = models.CharField(max_length=500)

    def __str__ (self):
        return self.country_name


    # ------------
    # Player_model
    # ------------

class Player(models.Model):
    """
    The model contains a country name (which is foreign key that comes from the country model), player surname, full name,
    club the player plays for, the position the player plays and his date of birth_date.
    The __str__ method is used to return the name of the player.
    """

    country = models.ForeignKey(Country)
    sur_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    clubname = models.CharField(max_length=200)
    position = models.CharField(max_length=64)
    shirt_number = models.IntegerField(default=0)
    birth_date = models.DateField()
    player_image = models.CharField(max_length=500)


    def __str__ (self):
        return self.full_name

    # ------------
    # Match_model
    # ------------

class Match(models.Model):
    """
    The model contains a match number, the two countries that are facing each other (both of the countries are foreign keys), the winner of the match, 
    the score of the match, the location of the match and the date when the match was held.
    The __str__ method is used to return the two countries facing each other and the score. 
    """

    match_num = models.IntegerField(default=0)
    # country_AB = models.CharField(max_length=200)
    country_A = models.ForeignKey(Country, related_name='country_A')
    country_B = models.ForeignKey(Country, related_name='country_B')
    winner = models.CharField(max_length=200)
    score = models.CharField(max_length=64)
    location = models.CharField(max_length=200)
    match_date = models.DateField()
    merge_flag = models.CharField(max_length=500)
    versus_flag = models.CharField(max_length=500)
    map_location = models.CharField(max_length=500)
    highlight_url = models.CharField(max_length=500)

    def __str__ (self):
        return self.country_A.country_name + " " + self.country_B.country_name + " " + self.score
