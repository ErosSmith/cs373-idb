# Create your tests here.
import os
import sys
import json
from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse
from django.core.management import call_command

#New Imports
from django.utils import unittest
from django.test import TestCase
from django.http import HttpResponse

from json import dumps, loads


from django.test import TestCase
from wc_app.models import *

try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import *

from tastypie.test import ResourceTestCase

import json
import watson
#end New Imports

    # -----------
    # TestModels
    # -----------

class ModelTestCase(TestCase):
    # -------------
    # country_model
    # -------------

    def test_country_model1(self):
        #Dictionary Key: Country Name
        #Dictionary Value: [Country_code, country_rank]
        country_test_dict1 = {"Brazil": ["BRA", 3,"https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png","https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg","https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ"]}

        Country.objects.create(country_name="Brazil", country_code=country_test_dict1["Brazil"][0], rank = country_test_dict1["Brazil"][1], flag = "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png", symbol_flag = "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg", map_url = "https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ" )
 
        Country_Brazil = Country.objects.get(country_name="Brazil")
        self.assertEqual(Country_Brazil.country_name, "Brazil")
        self.assertEqual(Country_Brazil.country_code, "BRA")
        self.assertEqual(Country_Brazil.rank, 3)
        self.assertEqual(Country_Brazil.flag, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png")
        self.assertEqual(Country_Brazil.symbol_flag, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg")
        self.assertEqual(Country_Brazil.map_url, "https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ")

    def test_country_model2(self):
        #Dictionary Key: Country Name
        #Dictionary Value: [Country_code, country_rank]
        country_test_dict2 = {"Brazil": ["BRA", 3,"https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png","https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg","https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ"], "Italy": ["ITA", 9,"https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/italy.png","https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/italy.jpg","https://www.google.com/maps/embed/v1/place?q=Italy&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ"]}

        Country.objects.create(country_name="Brazil", country_code=country_test_dict2["Brazil"][0], rank = country_test_dict2["Brazil"][1], flag = country_test_dict2["Brazil"][2], symbol_flag = country_test_dict2["Brazil"][3], map_url = country_test_dict2["Brazil"][4])
        Country.objects.create(country_name="Italy", country_code=country_test_dict2["Italy"][0], rank = country_test_dict2["Italy"][1], flag = country_test_dict2["Italy"][2], symbol_flag = country_test_dict2["Italy"][3], map_url = country_test_dict2["Italy"][4])

        #Brazil check      
        Country_Brazil = Country.objects.get(country_name="Brazil")
        self.assertEqual(Country_Brazil.country_name, "Brazil")
        self.assertEqual(Country_Brazil.country_code, "BRA")
        self.assertEqual(Country_Brazil.rank, 3)
        self.assertEqual(Country_Brazil.flag, country_test_dict2["Brazil"][2])
        self.assertEqual(Country_Brazil.symbol_flag, country_test_dict2["Brazil"][3])
        self.assertEqual(Country_Brazil.map_url, country_test_dict2["Brazil"][4])

        #Italy check       
        Country_Brazil = Country.objects.get(country_name="Italy")
        self.assertEqual(Country_Brazil.country_name, "Italy")
        self.assertEqual(Country_Brazil.country_code, 'ITA')
        self.assertEqual(Country_Brazil.rank, 9)
        self.assertEqual(Country_Brazil.flag, country_test_dict2["Italy"][2])
        self.assertEqual(Country_Brazil.symbol_flag, country_test_dict2["Italy"][3])
        self.assertEqual(Country_Brazil.map_url, country_test_dict2["Italy"][4])


    def test_country_model3(self):
        ########################################
        #Kim change the file location to your computer thanks
        #########################################
         s = open("wc_app/testing_country_date.json")
         country_test_dic = json.load(s)
         s.close()

         for country in country_test_dic.keys():
            Country.objects.create(country_name=country, country_code=country_test_dic[country][0], rank = country_test_dic[country][1], flag = country_test_dic[country][2], symbol_flag = country_test_dic[country][3], map_url = country_test_dic[country][4])

         for current_country in country_test_dic.keys():
            temp = Country.objects.get(country_name=current_country)
            self.assertEqual(temp.country_name, current_country)
            self.assertEqual(temp.country_code, country_test_dic[current_country][0])
            self.assertEqual(temp.rank, country_test_dic[current_country][1])
            self.assertEqual(temp.flag, country_test_dic[current_country][2])
            self.assertEqual(temp.symbol_flag, country_test_dic[current_country][3])
            self.assertEqual(temp.map_url, country_test_dic[current_country][4])
            
            

    # -------------
    # Player_model
    # -------------


    # country = models.ForeignKey(Country)
    # sur_name = models.CharField(max_length=200)
    # full_name = models.CharField(max_length=200)
    # clubname = models.CharField(max_length=200)
    # position = models.CharField(max_length=64)
    # birth_date = models.DateField()

    def test_player_model1(self):
        #Dictionary Key: Player full name
        #Dictionary Value: [sur_name, country,Clubname,Position,Birthdate, something, image, something, first international appearance, something, somethingthing, bio]
        player_test_dict1 = {"Andrea Barzagli": ["Barzagli", "Italy", "Juventus FC", "Defender", "1981-05-08", 15, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Italy/Andrea_BARZAGLI.png", 50, "Italy - Finland 17 Nov 2004", 0, 186, "Formidable in the air and a fine tackler who gives away very few fouls, centre-back Andrea Barzagli is viewed by Italy coach Cesare Prandelli as a defensive stand-in of the highest quality. Since joining Juventus in 2011, he has played regularly alongside Giorgio Chiellini and Leonardo Bonucci in a three-man back line, and the trio have developed an understanding crucial to their performances with "]}

        Country.objects.create(country_name = player_test_dict1["Andrea Barzagli"][1])
        c1 = Country.objects.create(country_name = player_test_dict1["Andrea Barzagli"][1])

        Player.objects.create(country=c1, sur_name= player_test_dict1["Andrea Barzagli"][0],full_name = "Andrea Barzagli" ,clubname = player_test_dict1["Andrea Barzagli"][2], position = player_test_dict1["Andrea Barzagli"][3], birth_date =player_test_dict1["Andrea Barzagli"][4], player_image = player_test_dict1["Andrea Barzagli"][6], international_caps = player_test_dict1["Andrea Barzagli"][5], goals = player_test_dict1["Andrea Barzagli"][5], height = player_test_dict1["Andrea Barzagli"][5], first_international_appearance = player_test_dict1["Andrea Barzagli"][8], biography = player_test_dict1["Andrea Barzagli"][11])
        
        player_get = Player.objects.get(full_name = "Andrea Barzagli")
        self.assertEqual(player_get.country.__str__(), player_test_dict1["Andrea Barzagli"][1])
        self.assertEqual(player_get.sur_name, player_test_dict1["Andrea Barzagli"][0])
        self.assertEqual(player_get.full_name, "Andrea Barzagli")
        self.assertEqual(player_get.clubname, player_test_dict1["Andrea Barzagli"][2])
        self.assertEqual(player_get.position, player_test_dict1["Andrea Barzagli"][3])
        self.assertEqual(player_get.birth_date.__str__(), player_test_dict1["Andrea Barzagli"][4])
        self.assertEqual(player_get.player_image, player_test_dict1["Andrea Barzagli"][6]) #string
        self.assertEqual(player_get.international_caps, player_test_dict1["Andrea Barzagli"][5]) #int
        self.assertEqual(player_get.goals, player_test_dict1["Andrea Barzagli"][5]) #int
        self.assertEqual(player_get.height, player_test_dict1["Andrea Barzagli"][5]) #int
        self.assertEqual(player_get.first_international_appearance, player_test_dict1["Andrea Barzagli"][8]) #string
        self.assertEqual(player_get.biography, player_test_dict1["Andrea Barzagli"][11]) #string




    def test_player_model2(self):
        #Dictionary Key: Player full name
        #Dictionary Value: [sur_name, country,Clubname,Position,Birthdate, something, image, something, first international appearance, something, somethingthing, bio]
        player_test_dict1 = {"Andrea Barzagli": ["Barzagli", "Italy", "Juventus FC", "Defender", "1981-05-08", 15, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Italy/Andrea_BARZAGLI.png", 50, "Italy - Finland 17 Nov 2004", 0, 186, "Formidable in the air and a fine tackler who gives away very few fouls, centre-back Andrea Barzagli is viewed by Italy coach Cesare Prandelli as a defensive stand-in of the highest quality. Since joining Juventus in 2011, he has played regularly alongside Giorgio Chiellini and Leonardo Bonucci in a three-man back line, and the trio have developed an understanding crucial to their performances with "],
        "Yoshito Okubo": ["Okubo", "Japan", "Kawasaki Frontale", "Forward", "1982-06-09", 13, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Japan/Yoshito_OKUBO.png", 60, "Japan - Korea Republic 31 May 2003", 6, 170, "After winning the J.League golden boot in 2013, striker Yoshito Okubo will be brimming with confidence as he appears at his second FIFA World Cup. Even so, the inclusion of the seasoned Kawasaki Frontale forward for Brazil 2014 was something of a surprise, as his last game for the Samurai Blue came more than two years ago. "]}

        Country.objects.create(country_name = player_test_dict1["Andrea Barzagli"][1])
        Country.objects.create(country_name = player_test_dict1["Yoshito Okubo"][1])

        c1 = Country.objects.get(country_name = player_test_dict1["Andrea Barzagli"][1])
        c2 = Country.objects.get(country_name = player_test_dict1["Yoshito Okubo"][1])

        player1_name= "Andrea Barzagli"
        player2_name= "Yoshito Okubo"

        Player.objects.create(country=c1, sur_name= player_test_dict1[player1_name][0],full_name = "Andrea Barzagli" ,clubname = player_test_dict1[player1_name][2], position = player_test_dict1[player1_name][3], birth_date =player_test_dict1[player1_name][4], player_image = player_test_dict1[player1_name][6], international_caps = player_test_dict1[player1_name][5], goals = player_test_dict1[player1_name][5], height = player_test_dict1[player1_name][5], first_international_appearance = player_test_dict1[player1_name][8], biography = player_test_dict1[player1_name][11])
        Player.objects.create(country=c2, sur_name= player_test_dict1[player2_name][0],full_name = "Yoshito Okubo" ,clubname = player_test_dict1[player2_name][2], position = player_test_dict1[player2_name][3], birth_date =player_test_dict1[player2_name][4], player_image = player_test_dict1[player2_name][6], international_caps = player_test_dict1[player2_name][5], goals = player_test_dict1[player2_name][5], height = player_test_dict1[player2_name][5], first_international_appearance = player_test_dict1[player2_name][8], biography = player_test_dict1[player2_name][11])
        

        player_get = Player.objects.get(full_name = player1_name)
        self.assertEqual(player_get.country.__str__(), player_test_dict1[player1_name][1])
        self.assertEqual(player_get.sur_name, player_test_dict1[player1_name][0])
        self.assertEqual(player_get.full_name, player1_name)
        self.assertEqual(player_get.clubname, player_test_dict1[player1_name][2])
        self.assertEqual(player_get.position, player_test_dict1[player1_name][3])
        self.assertEqual(player_get.birth_date.__str__(), player_test_dict1[player1_name][4])

        self.assertEqual(player_get.player_image, player_test_dict1[player1_name][6])
        self.assertEqual(player_get.international_caps, player_test_dict1[player1_name][5])
        self.assertEqual(player_get.goals, player_test_dict1[player1_name][5])
        self.assertEqual(player_get.height, player_test_dict1[player1_name][5])
        self.assertEqual(player_get.first_international_appearance, player_test_dict1[player1_name][8])
        self.assertEqual(player_get.biography, player_test_dict1[player1_name][11])

        
        player_get = Player.objects.get(full_name = player2_name)
        self.assertEqual(player_get.country.__str__(), player_test_dict1[player2_name][1])
        self.assertEqual(player_get.sur_name, player_test_dict1[player2_name][0])
        self.assertEqual(player_get.full_name, player2_name)
        self.assertEqual(player_get.clubname, player_test_dict1[player2_name][2])
        self.assertEqual(player_get.position, player_test_dict1[player2_name][3])
        self.assertEqual(player_get.birth_date.__str__(), player_test_dict1[player2_name][4])

        self.assertEqual(player_get.player_image, player_test_dict1[player2_name][6])
        self.assertEqual(player_get.international_caps, player_test_dict1[player2_name][5])
        self.assertEqual(player_get.goals, player_test_dict1[player2_name][5])
        self.assertEqual(player_get.height, player_test_dict1[player2_name][5])
        self.assertEqual(player_get.first_international_appearance, player_test_dict1[player2_name][8])
        self.assertEqual(player_get.biography, player_test_dict1[player2_name][11])

    def test_player_model3(self):
        #Dictionary Key: Player full name
        #Dictionary Value: [sur_name, country,Clubname,Position,Birthdate, something, image, something, first international appearance, something, somethingthing, bio]

        s = open("wc_app/testing_player_data.json")
        player_test_diction = json.load(s)
        s.close()

        s = open("wc_app/testing_country_date.json")
        country_test_dic = json.load(s)
        s.close()

        for country_name in country_test_dic.keys():
            Country.objects.create(country_name = country_name)
        
        for player_name in player_test_diction.keys(): 
            c1 = Country.objects.get(country_name = player_test_diction[player_name][1])
            Player.objects.create(country=c1, sur_name= player_test_diction[player_name][0],full_name = player_name ,clubname = player_test_diction[player_name][2], position = player_test_diction[player_name][3], birth_date =player_test_diction[player_name][4], player_image = player_test_diction[player_name][6], international_caps = player_test_diction[player_name][5], goals = player_test_diction[player_name][5], height = player_test_diction[player_name][5], first_international_appearance = player_test_diction[player_name][8], biography = player_test_diction[player_name][11])

        for player_name in player_test_diction.keys():
            player_get = Player.objects.get(full_name = player_name)
            self.assertEqual(player_get.country.__str__(), player_test_diction[player_name][1])
            self.assertEqual(player_get.sur_name, player_test_diction[player_name][0])
            self.assertEqual(player_get.full_name, player_name)
            self.assertEqual(player_get.clubname, player_test_diction[player_name][2])
            self.assertEqual(player_get.position, player_test_diction[player_name][3])
            self.assertEqual(player_get.birth_date.__str__(), player_test_diction[player_name][4])

            self.assertEqual(player_get.player_image, player_test_diction[player_name][6])
            self.assertEqual(player_get.international_caps, player_test_diction[player_name][5])
            self.assertEqual(player_get.goals, player_test_diction[player_name][5])
            self.assertEqual(player_get.height, player_test_diction[player_name][5])
            self.assertEqual(player_get.first_international_appearance, player_test_diction[player_name][8])
            self.assertEqual(player_get.biography, player_test_diction[player_name][11])


    # -------------
    # Match_model
    # -------------

    # match_num = models.IntegerField(default=0)
    # country_A = models.ForeignKey(Country, related_name='country_A')
    # country_B = models.ForeignKey(Country, related_name='country_B')
    # winner = models.CharField(max_length=200)
    # score = models.CharField(max_length=64)
    # location = models.CharField(max_length=200)
    # match_date = models.DateField()


    def test_match_model1(self):
        #Dictionary Key: HomeTeam vs AwayTeam
        #Dictionary Value: [Match_Number, HomeTeam, HomeTeamScore,AwayTeam, AwayTeamScore, Winner, Location, date, merged flag, maps location, hightlights]
        match_test_dict1 = { "Ivory Coast-Japan" : [ 6, "Ivory Coast", 2, "Japan", 1, "Ivory Coast", "Arena Pernambuco", "2014-06-14", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/civ_jpn.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1881469" ]}

        score_cat = str(match_test_dict1["Ivory Coast-Japan"][2]) + "-" + str(match_test_dict1["Ivory Coast-Japan"][4])
                
        Country.objects.create(country_name = "Ivory Coast")
        Country.objects.create(country_name = "Japan")
        
        Match.objects.create(match_num = match_test_dict1["Ivory Coast-Japan"][0], country_A = Country.objects.get(country_name = match_test_dict1["Ivory Coast-Japan"][1]), country_B = Country.objects.get(country_name = match_test_dict1["Ivory Coast-Japan"][3]), winner = match_test_dict1["Ivory Coast-Japan"][5], score = score_cat, location = match_test_dict1["Ivory Coast-Japan"][6], match_date = match_test_dict1["Ivory Coast-Japan"][7], merge_flag = match_test_dict1["Ivory Coast-Japan"][8], map_location = match_test_dict1["Ivory Coast-Japan"][9], highlight_url = match_test_dict1["Ivory Coast-Japan"][10])

        #need to create country objects and add __str__ methods assert equals
        match_get = Match.objects.get(match_num = match_test_dict1["Ivory Coast-Japan"][0])
        self.assertEqual(match_get.match_num, match_test_dict1["Ivory Coast-Japan"][0])
        self.assertEqual(match_get.country_A.country_name, match_test_dict1["Ivory Coast-Japan"][1])
        self.assertEqual(match_get.country_B.country_name, match_test_dict1["Ivory Coast-Japan"][3])
        self.assertEqual(match_get.winner, match_test_dict1["Ivory Coast-Japan"][5])
        self.assertEqual(match_get.score, score_cat)
        self.assertEqual(match_get.location, match_test_dict1["Ivory Coast-Japan"][6])
        self.assertEqual(match_get.match_date.__str__(), match_test_dict1["Ivory Coast-Japan"][7])
        self.assertEqual(match_get.merge_flag, match_test_dict1["Ivory Coast-Japan"][8])
        self.assertEqual(match_get.map_location, match_test_dict1["Ivory Coast-Japan"][9])
        self.assertEqual(match_get.highlight_url, match_test_dict1["Ivory Coast-Japan"][10])

    def test_match_model2(self):
        #Dictionary Key: HomeTeam vs AwayTeam
        #Dictionary Value: [Match_Number, HomeTeam, HomeTeamScore,AwayTeam, AwayTeamScore, Winner, Location, date]
        match_test_dict1 ={ "Ivory Coast-Japan" : [ 6, "Ivory Coast", 2, "Japan", 1, "Ivory Coast", "Arena Pernambuco", "2014-06-14", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/civ_jpn.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1881469" ] , "Cameroon-Croatia" : [ 18, "Cameroon", 0, "Croatia", 4, "Croatia", "Arena Amazonia", "2014-06-18", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/cmr_cro.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Amazonia+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1891625 " ]}

        Country.objects.create(country_name = "Ivory Coast")
        Country.objects.create(country_name = "Japan")
        Country.objects.create(country_name = "Cameroon")
        Country.objects.create(country_name = "Croatia")

        score_cat = str(match_test_dict1["Ivory Coast-Japan"][2]) + "-" + str(match_test_dict1["Ivory Coast-Japan"][4])
        Match.objects.create(match_num = match_test_dict1["Ivory Coast-Japan"][0],
                             country_A = Country.objects.get(country_name = match_test_dict1["Ivory Coast-Japan"][1]),
                             country_B = Country.objects.get(country_name = match_test_dict1["Ivory Coast-Japan"][3]),
                             winner = match_test_dict1["Ivory Coast-Japan"][5], score = score_cat,
                             location = match_test_dict1["Ivory Coast-Japan"][6],
                             match_date = match_test_dict1["Ivory Coast-Japan"][7],
                             merge_flag = match_test_dict1["Ivory Coast-Japan"][8],
                             map_location = match_test_dict1["Ivory Coast-Japan"][9],
                             highlight_url = match_test_dict1["Ivory Coast-Japan"][10])
        
        score_cat2 = str(match_test_dict1["Cameroon-Croatia"][2]) + "-" + str(match_test_dict1["Cameroon-Croatia"][4])
        Match.objects.create(match_num = match_test_dict1["Cameroon-Croatia"][0], country_A = Country.objects.get(country_name = match_test_dict1["Cameroon-Croatia"][1]), country_B = Country.objects.get(country_name = match_test_dict1["Cameroon-Croatia"][3]), winner = match_test_dict1["Cameroon-Croatia"][5], score = score_cat2, location = match_test_dict1["Cameroon-Croatia"][6], match_date = match_test_dict1["Cameroon-Croatia"][7], merge_flag = match_test_dict1["Cameroon-Croatia"][8], map_location = match_test_dict1["Cameroon-Croatia"][9], highlight_url = match_test_dict1["Cameroon-Croatia"][10])

        match_get = Match.objects.get(match_num = match_test_dict1["Ivory Coast-Japan"][0])
        self.assertEqual(match_get.match_num, match_test_dict1["Ivory Coast-Japan"][0])
        self.assertEqual(match_get.country_A.country_name, match_test_dict1["Ivory Coast-Japan"][1])
        self.assertEqual(match_get.country_B.country_name, match_test_dict1["Ivory Coast-Japan"][3])
        self.assertEqual(match_get.winner, match_test_dict1["Ivory Coast-Japan"][5])
        self.assertEqual(match_get.score, score_cat)
        self.assertEqual(match_get.location, match_test_dict1["Ivory Coast-Japan"][6])
        self.assertEqual(match_get.match_date.__str__(), match_test_dict1["Ivory Coast-Japan"][7])

        self.assertEqual(match_get.merge_flag, match_test_dict1["Ivory Coast-Japan"][8])
        self.assertEqual(match_get.map_location, match_test_dict1["Ivory Coast-Japan"][9])
        self.assertEqual(match_get.highlight_url, match_test_dict1["Ivory Coast-Japan"][10])



        match_get = Match.objects.get(match_num = match_test_dict1["Cameroon-Croatia"][0])
        self.assertEqual(match_get.match_num, match_test_dict1["Cameroon-Croatia"][0])
        self.assertEqual(match_get.country_A.country_name, match_test_dict1["Cameroon-Croatia"][1])
        self.assertEqual(match_get.country_B.country_name, match_test_dict1["Cameroon-Croatia"][3])
        self.assertEqual(match_get.winner, match_test_dict1["Cameroon-Croatia"][5])
        self.assertEqual(match_get.score, score_cat2)
        self.assertEqual(match_get.location, match_test_dict1["Cameroon-Croatia"][6])
        self.assertEqual(match_get.match_date.__str__(), match_test_dict1["Cameroon-Croatia"][7])

        self.assertEqual(match_get.merge_flag, match_test_dict1["Cameroon-Croatia"][8])
        self.assertEqual(match_get.map_location, match_test_dict1["Cameroon-Croatia"][9])
        self.assertEqual(match_get.highlight_url, match_test_dict1["Cameroon-Croatia"][10])


    def test_match_model3(self):
        #Dictionary Key: HomeTeam vs AwayTeam
        #Dictionary Value: [Match_Number, HomeTeam, HomeTeamScore,AwayTeam, AwayTeamScore, Winner, Location, date]
        s = open("wc_app/testing_match_data.json")
        match_test_diction = json.load(s)
        s.close()

        s = open("wc_app/testing_country_date.json")
        country_test_dic = json.load(s)
        s.close()

        for country_name in country_test_dic.keys():
            Country.objects.create(country_name = country_name)
        
        for match_vs in match_test_diction:
            score_cat = str(match_test_diction[match_vs][2]) + "-" + str(match_test_diction[match_vs][4])
            Match.objects.create(match_num = match_test_diction[match_vs][0], country_A = Country.objects.get(country_name = match_test_diction[match_vs][1]), country_B = Country.objects.get(country_name = match_test_diction[match_vs][3]), winner = match_test_diction[match_vs][5], score = score_cat, location = match_test_diction[match_vs][6], match_date = match_test_diction[match_vs][7], merge_flag = match_test_diction[match_vs][8], map_location = match_test_diction[match_vs][9], highlight_url = match_test_diction[match_vs][10])
            
        for match_vs in match_test_diction:    
            match_get = Match.objects.get(match_num = match_test_diction[match_vs][0])
            self.assertEqual(match_get.match_num, match_test_diction[match_vs][0])
            self.assertEqual(match_get.country_A.country_name, match_test_diction[match_vs][1])
            self.assertEqual(match_get.country_B.country_name, match_test_diction[match_vs][3])
            self.assertEqual(match_get.winner, match_test_diction[match_vs][5])
            self.assertEqual(match_get.score, str(match_test_diction[match_vs][2]) + "-" + str(match_test_diction[match_vs][4]))
            self.assertEqual(match_get.location, match_test_diction[match_vs][6])
            self.assertEqual(match_get.match_date.__str__(), match_test_diction[match_vs][7])
            self.assertEqual(match_get.merge_flag, match_test_diction[match_vs][8])
            self.assertEqual(match_get.map_location, match_test_diction[match_vs][9])
            self.assertEqual(match_get.highlight_url, match_test_diction[match_vs][10])

# Have to setup the data first
# Running as localhost
# or change to pythonanywhere url and it should works
class APItests(unittest.TestCase) :
    url = "http://127.0.0.1:8000/"

    #Countries

    def test_get_all_countries(self) :
        request = Request(self.url+"api/countries/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        response_objects = response_data["objects"]
        expected_response =[    {
      "article": " Drawn in perhaps the most open group in Africa, alongside Libya, Congo DR and Togo, Cameroon survived the challenge with the help of an overturned loss because of Togo's fielding of an ineligible player. Ultimately the Lions did enough anyway with a 1-0 defeat of the pace-setting Libyans in their final match that saw them finish with 13 points from six matches. Once in the final play-off round, they handled a tough task against Tunisia with aplomb. A scoreless draw on the road gave way to a 4-1 home win that has Volker Finke's side feeling confident about their trip to Brazil.  Perhaps no team has done more to shake up perceptions of African football. The Indomitable Lions exited Spain 1982 at the group stage, but they ended their maiden excursion undefeated, having drawn 0-0 with both Peru and Poland and 1-1 with eventual winners Italy. Eight years later, they wrote themselves into the annals of the game by beating holders Argentina in the Opening Match and becoming the first African side to reach the quarter-finals, powered by the goals of evergreen striker Roger Milla. That breakthrough performance remains their finest showing, group-stage exits having followed in 1994, 1998, 2002 and 2010.  Samuel Eto'o remains the world-class threat up front, although the charismatic figure, who still serves as captain, has gone in and out of the team. But even without the Chelsea veteran, the side if loaded with experience and high-level talent. Nicolas N'Koulou, Benoit Assou-Ekotto and Aurelien Chedjou remain vital at the back, while the midfield is even more loaded with Alex Song, Jean Makoun and Stephane Mbia at the heart of the team.Volker FinkeFIFA World Cup Italy 1990 (Quarter-finals), Men’s Olympic Football Tournament Sydney 2000 (Winners)Roger Milla, Marc-Vivien Foe, Rigobert Song",
      "att_attempts": "40",
      "att_crosses": "49",
      "att_crosses_completed": "15",
      "att_crosses_completed_ta": "9.9",
      "att_crosses_ta": "41",
      "att_deliveries_penalty_area": "5",
      "att_deliveries_penalty_area_ta": "1.9",
      "att_dribble_penalty_area": "6",
      "att_dribble_penalty_area_ta": "6.4",
      "att_goals_scored": "2",
      "att_offsides": "4",
      "att_offsides_ta": "4.9",
      "att_shots_blocked": "1",
      "att_shots_saved": "14",
      "attempts_off_target": "23",
      "attempts_on_target": "17",
      "continent": "Africa",
      "country_code": "CMR",
      "country_name": "Cameroon",
      "def_attempted_clearances": "41",
      "def_attempted_clearances_ta": "29.4",
      "def_blocks": "13",
      "def_completed_clearances": "36",
      "def_completed_clearances_ta": "24.5",
      "def_offsides_given": "12",
      "def_offsides_given_ta": "4.9",
      "def_recovered_balls": "108",
      "def_recovered_balls_ta": "88.8",
      "def_saves": "15",
      "def_saves_ta": "7.3",
      "def_tackles": "38",
      "def_tackles_lost": "25",
      "def_tackles_lost_ta": "21.8",
      "def_tackles_tol": "38",
      "def_tackles_tol_ta": "36.7",
      "def_tackles_won": "8",
      "def_tackles_won_ta": "9.3",
      "def_total_defense": "66",
      "distance_covered": "292.0",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/cameroon.png",
      "goals_scored": "1",
      "id": 1,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Cameroon&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "40",
      "one_g_freq_min": "270",
      "open_play_goals": "1",
      "pass_crosses": "49",
      "pass_crosses_ta": "41",
      "pass_long_passes_complete": "94",
      "pass_medium_passes_complete": "544",
      "pass_short_passes_complete": "240",
      "pass_ta": "868",
      "pass_throw_ins": "90",
      "pass_throw_ins_ta": "70.5",
      "pass_total": "878",
      "rank": 52,
      "resource_uri": "/api/countries/Cameroon/",
      "scoring_method_total": "1",
      "set_piece_goals": "0",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/cameroon.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/cmr.gif",
      "team_video_url": "//www.youtube.com/embed/ygntRxCUqrQ",
      "tournament_average": "28.7"
    },
    {
      "article": " Bosnia-Herzegovina had an outstanding campaign, winning eight of their ten matches, drawing and losing just once. A ruthless attack and resilient rearguard were the cornerstones of the side’s success, with the 30 goals scored representing the fourth-highest tally in European zone qualifying. Equally impressive was a defence that was breached just six times. Bosnia-Herzegovina’s notable goal difference proved crucial too, edging them past a Greece side that finished level on points, to secure direct passage to Brazil 2014 and a first appearance at a FIFA World Cup™. After starting with a string of victories combined with a goalless draw in Greece, coach Safet Susic’s team’s campaign initially went according to plan. However, a 1-0 defeat at home to Slovakia in September 2013 set up a nail-biting finale for Bosnia-Herzegovina, before they pipped Greece to the post on the final matchday.  Bosnia-Herzegovina have a core of talented players capable of changing games in an instant, ranging from the likes of Edin Dzeko and Vedad Ibisevic up front, through midfielders Miralem Pjanic and Zvjezdan Misimovic, all the way back to defensive rock Emir Spahic and goalkeeper Asmir Begovic. The majority of the squad regularly showcase their talents in Europe’s biggest leagues, giving them the experience necessary to shine on the biggest stage of them all.  Safet Susic None Vahid Halilhodic, Hasan Salihamidzic, Safet Susic",
      "att_attempts": "46",
      "att_crosses": "72",
      "att_crosses_completed": "19",
      "att_crosses_completed_ta": "11.8",
      "att_crosses_ta": "49.7",
      "att_deliveries_penalty_area": "1",
      "att_deliveries_penalty_area_ta": "2.3",
      "att_dribble_penalty_area": "6",
      "att_dribble_penalty_area_ta": "7.8",
      "att_goals_scored": "10",
      "att_offsides": "6",
      "att_offsides_ta": "5.7",
      "att_shots_blocked": "4",
      "att_shots_saved": "15",
      "attempts_off_target": "17",
      "attempts_on_target": "30",
      "continent": "Europe",
      "country_code": "BIH",
      "country_name": "Bosnia and Herzegovina",
      "def_attempted_clearances": "39",
      "def_attempted_clearances_ta": "34.6",
      "def_blocks": "7",
      "def_completed_clearances": "28",
      "def_completed_clearances_ta": "28.9",
      "def_offsides_given": "11",
      "def_offsides_given_ta": "5.8",
      "def_recovered_balls": "135",
      "def_recovered_balls_ta": "110",
      "def_saves": "13",
      "def_saves_ta": "9",
      "def_tackles": "60",
      "def_tackles_lost": "38",
      "def_tackles_lost_ta": "27.6",
      "def_tackles_tol": "60",
      "def_tackles_tol_ta": "45.2",
      "def_tackles_won": "20",
      "def_tackles_won_ta": "12.1",
      "def_total_defense": "80",
      "distance_covered": "337.8",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/bosnia_and_herzegovina.png",
      "goals_scored": "4",
      "id": 2,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=BosniaandHerzegovina&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "11.8",
      "one_g_freq_min": "68",
      "open_play_goals": "4",
      "pass_crosses": "72",
      "pass_crosses_ta": "49.7",
      "pass_long_passes_complete": "136",
      "pass_medium_passes_complete": "926",
      "pass_short_passes_complete": "350",
      "pass_ta": "1053",
      "pass_throw_ins": "77",
      "pass_throw_ins_ta": "84.9",
      "pass_total": "1412",
      "rank": 21,
      "resource_uri": "/api/countries/Bosnia%20and%20Herzegovina/",
      "scoring_method_total": "4",
      "set_piece_goals": "0",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/bosnia_and_herzegovina.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/bih.gif",
      "team_video_url": "//www.youtube.com/embed/aXp0uMQ9eI4",
      "tournament_average": "35.2"
    },
    {
      "article": " Côte d’Ivoire breezed through their opening qualifying group with four wins from their six matches. They scored 15 goals to five conceded, and their only dropped points came from two draws against their biggest rivals Morocco. Their home-and-away play-off was much trickier however as a resurgent Senegal stood in their way. For the final quarter of an hour of the second leg, the Senegalese were one goal away from knocking out the Elephants on away goals at 3-2 aggregate, but Salomon Kalou's late goal settled the tie and sent the Ivorians into their third consecutive World Cup finals. Côte d’Ivoire have never made it past the group stage of a FIFA World Cup finals, but it is perhaps worth pointing out that the draw has never been particularly kind to them. For their debut appearance in 2006, the Elephants shared Group C with Argentina, Netherlands and Serbia and Montenegro. They finished third in the pool, just as they did in South Africa four years later, when they were drawn alongside Brazil, Portugal and Korea DPR.  Côte d’Ivoire boast some of the greatest individual talents in Africa. Forwards Didier Drogba and Salomon Kalou are a formidable front pair, while midfield duo Cheick Tiote and Yaya Toure perform key ball-winning duties in the middle of the park. Explosive winger Gervinho supplies service from both flanks, with Didier Zokora and Kolo Toure providing a wealth of experience at the back.  Sabri LamouchiFIFA World Cup Germany 2006, South Africa 2010 (Group stages), FIFA U-17 World Cup Canada 1987 (Third place), FIFA Confederations Cup Saudi Arabia 1992 (Fourth place) Laurent Pokou Youssouf Fofana, Joel Tiehi ",
      "att_attempts": "47",
      "att_crosses": "62",
      "att_crosses_completed": "12",
      "att_crosses_completed_ta": "10.5",
      "att_crosses_ta": "44.9",
      "att_deliveries_penalty_area": "3",
      "att_deliveries_penalty_area_ta": "2.2",
      "att_dribble_penalty_area": "18",
      "att_dribble_penalty_area_ta": "7.1",
      "att_goals_scored": "11",
      "att_offsides": "6",
      "att_offsides_ta": "5.3",
      "att_shots_blocked": "4",
      "att_shots_saved": "15",
      "attempts_off_target": "17",
      "attempts_on_target": "30",
      "continent": "Africa",
      "country_code": "CIV",
      "country_name": "Ivory Coast",
      "def_attempted_clearances": "51",
      "def_attempted_clearances_ta": "31.8",
      "def_blocks": "4",
      "def_completed_clearances": "43",
      "def_completed_clearances_ta": "26.4",
      "def_offsides_given": "5",
      "def_offsides_given_ta": "5.3",
      "def_recovered_balls": "107",
      "def_recovered_balls_ta": "99.8",
      "def_saves": "8",
      "def_saves_ta": "7.9",
      "def_tackles": "60",
      "def_tackles_lost": "33",
      "def_tackles_lost_ta": "24.6",
      "def_tackles_tol": "60",
      "def_tackles_tol_ta": "40.7",
      "def_tackles_won": "16",
      "def_tackles_won_ta": "10.5",
      "def_total_defense": "72",
      "distance_covered": "287.4",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ivory_coast.png",
      "goals_scored": "4",
      "id": 3,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=IvoryCoast&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "11.8",
      "one_g_freq_min": "68",
      "open_play_goals": "4",
      "pass_crosses": "62",
      "pass_crosses_ta": "44.9",
      "pass_long_passes_complete": "111",
      "pass_medium_passes_complete": "839",
      "pass_short_passes_complete": "265",
      "pass_ta": "956",
      "pass_throw_ins": "91",
      "pass_throw_ins_ta": "77.9",
      "pass_total": "1215",
      "rank": 23,
      "resource_uri": "/api/countries/Ivory%20Coast/",
      "scoring_method_total": "4",
      "set_piece_goals": "0",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ivory_coast.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/civ.gif",
      "team_video_url": "//www.youtube.com/embed/4mop073orrI",
      "tournament_average": "31.8"
    },
    {
      "article": " Ecuador were plagued by inconsistency during their qualifying campaign. While went undefeated at home, beating every opponent in Quito except Argentina, with whom they drew, the side was unable to reproduce that form on the road, failing to win at all and drawing just three times. Nevertheless, one such stalemate – against Uruguay in Montevideo – proved decisive as Ecuador finished level on points with  but grabbed the last automatic qualifying spot thanks to their superior goal difference (four compared to Uruguay’s zero).  With a team that was among the top four in the standings on 14 of the 16 matchdays and that had to overcome the tragic death of Cristian Benitez, coach Reinaldo Rueda became the third Colombian to guide Ecuador to FIFA World Cup™ qualification.  While Ecuador failed to extricate themselves from a tough group at Korea/Japan 2002, their first-ever appearance at the final stages of a FIFA World Cup, the story was quite different at Germany 2006, where the South Americans got as far as the last 16, having surprisingly finished second in their pool behind the host nation. Unfortunately for the CONMEBOL representatives, England would prove a hurdle too far; the Three Lions triumphed 1-0 to move on to the quarter-finals.  Wingers Antonio Valencia and Cristhian Noboa, as well as forwards Felipe Caicedo and Jefferson Montero, represent an exciting new wave for Ecuadorian football, but they are also ably assisted by evergreen stalwarts with European experience in Edison Mendez and Walter Ayovi. Reinaldo RuedaFIFA World Cup Germany2006 (Round of 16) Ulises de la Cruz, Agustin Delgado, Jose Francisco Cevallos",
      "att_attempts": "29",
      "att_crosses": "46",
      "att_crosses_completed": "7",
      "att_crosses_completed_ta": "11.8",
      "att_crosses_ta": "49.7",
      "att_deliveries_penalty_area": "3",
      "att_deliveries_penalty_area_ta": "2.3",
      "att_dribble_penalty_area": "10",
      "att_dribble_penalty_area_ta": "7.8",
      "att_goals_scored": "7",
      "att_offsides": "6",
      "att_offsides_ta": "5.7",
      "att_shots_blocked": "3",
      "att_shots_saved": "8",
      "attempts_off_target": "11",
      "attempts_on_target": "18",
      "continent": "South America",
      "country_code": "ECU",
      "country_name": "Ecuador",
      "def_attempted_clearances": "37",
      "def_attempted_clearances_ta": "34.6",
      "def_blocks": "15",
      "def_completed_clearances": "34",
      "def_completed_clearances_ta": "28.9",
      "def_offsides_given": "3",
      "def_offsides_given_ta": "5.8",
      "def_recovered_balls": "125",
      "def_recovered_balls_ta": "110",
      "def_saves": "18",
      "def_saves_ta": "9",
      "def_tackles": "44",
      "def_tackles_lost": "24",
      "def_tackles_lost_ta": "27.6",
      "def_tackles_tol": "44",
      "def_tackles_tol_ta": "45.2",
      "def_tackles_won": "13",
      "def_tackles_won_ta": "12.1",
      "def_total_defense": "77",
      "distance_covered": "296.3",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ecuador.png",
      "goals_scored": "3",
      "id": 4,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Ecuador&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "9.7",
      "one_g_freq_min": "90",
      "open_play_goals": "2",
      "pass_crosses": "46",
      "pass_crosses_ta": "49.7",
      "pass_long_passes_complete": "110",
      "pass_medium_passes_complete": "504",
      "pass_short_passes_complete": "185",
      "pass_ta": "1053",
      "pass_throw_ins": "111",
      "pass_throw_ins_ta": "84.9",
      "pass_total": "799",
      "rank": 26,
      "resource_uri": "/api/countries/Ecuador/",
      "scoring_method_total": "3",
      "set_piece_goals": "1",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ecuador.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/ecu.gif",
      "team_video_url": "//www.youtube.com/embed/TClfl0PoTzQ",
      "tournament_average": "35.2"
    },
    {
      "article": "Having looked to be building towards something special for a number of years, Belgium finally made the breakthrough many expected, with a golden generation seemingly capable of challenging the best. (Red Devils) proved that on the road to Brazil 2014, topping Group A ahead of the likes of Croatia, Serbia and Scotland after an almost faultless campaign. The Belgians only dropped points in an early draw against Croatia and a second stalemate in their final outing, when their finals place was already assured. They sealed their progress in their penultimate encounter, an excellent 2-1 victory in Zagreb that owed much to a double from Romelu Lukaku, one of several talents who have added a new dimension to their game since moving to the English Premier League. Founding members of FIFA, Belgium have taken part in 11 FIFA World Cup™ final tournaments and were an ever-present force between 1982 and 2002. In 1998, the side coached by Georges Leekens in his first spell at the helm came third in their group and made an early exit, while in 2002 Robert Waseige’s men fell in the last 16 to eventual winners Brazil. Neither of those teams came anywhere close to matching the generation that sparkled during Mexico 1986, when they reached the semi-finals before succumbing to Argentina. On paper, Belgium can call upon an armada of stars, all plying their trade in Europe’s most prestigious championships. The depth of their talent pool is striking, with Nacer Chadli threatening to eclipse crowd favourite Eden Hazard before the latter has approached anything near his peak. Romelu Lukaku, Kevin de Bruyne, Thibaut Courtois and Toby Alderweireld are the latest stars to emerge, while the likes of Vincent Kompany, Thomas Vermaelen, Axel Witsel, Marouane Fellaini and Steven Defour have already established themselves as senior figures. Marc Wilmots FIFA World Cup Mexico 1986 (Fourth place), Men’s Olympic Football Tournament Antwerp 1920 (Winners) Enzo Scifo, Jean-Marie Pfaff, Marc Wilmots",
      "att_attempts": "91",
      "att_crosses": "125",
      "att_crosses_completed": "26",
      "att_crosses_completed_ta": "17",
      "att_crosses_ta": "72.4",
      "att_deliveries_penalty_area": "4",
      "att_deliveries_penalty_area_ta": "3",
      "att_dribble_penalty_area": "24",
      "att_dribble_penalty_area_ta": "10.6",
      "att_goals_scored": "22",
      "att_offsides": "22",
      "att_offsides_ta": "8",
      "att_shots_blocked": "6",
      "att_shots_saved": "30",
      "attempts_off_target": "33",
      "attempts_on_target": "58",
      "continent": "Europe",
      "country_code": "BEL",
      "country_name": "Belgium",
      "def_attempted_clearances": "59",
      "def_attempted_clearances_ta": "50.9",
      "def_blocks": "13",
      "def_completed_clearances": "56",
      "def_completed_clearances_ta": "42.2",
      "def_offsides_given": "2",
      "def_offsides_given_ta": "8",
      "def_recovered_balls": "211",
      "def_recovered_balls_ta": "154",
      "def_saves": "13",
      "def_saves_ta": "13",
      "def_tackles": "61",
      "def_tackles_lost": "36",
      "def_tackles_lost_ta": "40.9",
      "def_tackles_tol": "61",
      "def_tackles_tol_ta": "63.8",
      "def_tackles_won": "15",
      "def_tackles_won_ta": "17.3",
      "def_total_defense": "93",
      "distance_covered": "576.9",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/belgium.png",
      "goals_scored": "6",
      "id": 5,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Belgium&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "5",
      "one_g_freq_attempts": "15.2",
      "one_g_freq_min": "80",
      "open_play_goals": "6",
      "pass_crosses": "125",
      "pass_crosses_ta": "72.4",
      "pass_long_passes_complete": "259",
      "pass_medium_passes_complete": "1261",
      "pass_short_passes_complete": "472",
      "pass_ta": "1427",
      "pass_throw_ins": "196",
      "pass_throw_ins_ta": "120",
      "pass_total": "1992",
      "rank": 11,
      "resource_uri": "/api/countries/Belgium/",
      "scoring_method_total": "6",
      "set_piece_goals": "0",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/belgium.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/bel.gif",
      "team_video_url": "//www.youtube.com/embed/4iBEwofrgLY",
      "tournament_average": "49.1"
    },
    {
      "article": " The Americans had an ominous start to their final round of qualifying in the CONCACAF zone, losing out 2-1 on the road in Honduras. The result had many in the US media questioning Jurgen Klinsmann’s approach and tactics. All that suspicion quickly melted away, however, as the German proved totally up to the task, guiding the  deftly to a first-place finish in the six-team Hexagonal. He experimented with old players in new positions, new players throughout the squad, changed formations freely and generally created a new atmosphere of confidence and competition in the team. They won an astounding seven of their ten games, scoring a Hexagonal-high 15 goals, conceding only eight, losing only once, and finishing four full points above runners-up Costa Rica in the final standings. If the trajectory continues for Klinsmann’s rampaging side, the sky might just be the limit in Brazil. The first US team to turn up at a FIFA world finals earned the dubious nickname of the ‘shot-putters’ for their muscular and burly nature, but 3-0 wins over Paraguay and Belgium in 1930 was enough for a third-place finish, to this day the best placing for any team outside of Europe or South America. Four years later the Americans went out in the first round, but they caused a grand sensation in Brazil in 1950 when, led by outstanding goalkeeper Frank Borghi, they managed to beat mighty England in Belo Horizante in an upsets for the ages. Another first-round exit came in 1990, but as hosts in 1994 they managed to reach the knockout rounds, a result that paved the way to more consistency. And after a last-place finish at France 1998, they beat Portugal and Mexico in Korea/Japan 2002 and only just missed out on a semi-final place after losing to Germany. In 2006 they went out in the first round again, this time in Germany before reaching the Round of 16 in South Africa in 2010.  Jozy Altidore, of English Premier League outfit Sunderland, emerged as the complete package during the final qualifying competition. Left out of the team due to poor form and attitude in the semi-final round,  Klinsmann reconsidered and wasn’t let down by his burly striker, who scored goals for fun and was the perfect partner for Clint Dempsey in attack. Toronto FC's Michael Bradley is the complete midfield player for USA, linking the backline with the attack. With Tim Howard still a dominant presence between the sticks, the Americans are loaded with ability wherever you look. Jurgen Klinsmann FIFA World Cup Uruguay 1930 (Third place), FIFA Confederations Cup Saudi Arabia 1992, Mexico 1999 (Third place), FIFA U-20 World Cup Saudi Arabia 1989 (Fourth place), FIFA U-17 World Cup New Zealand 1999 (Fourth place), FIFA Confederations Cup South Africa 2009 (Second place) John Harkes, Claudio Reyna, Brian McBride",
      "att_attempts": "41",
      "att_crosses": "64",
      "att_crosses_completed": "13",
      "att_crosses_completed_ta": "16.7",
      "att_crosses_ta": "71.3",
      "att_deliveries_penalty_area": "2",
      "att_deliveries_penalty_area_ta": "3",
      "att_dribble_penalty_area": "8",
      "att_dribble_penalty_area_ta": "10.4",
      "att_goals_scored": "10",
      "att_offsides": "4",
      "att_offsides_ta": "7.8",
      "att_shots_blocked": "5",
      "att_shots_saved": "12",
      "attempts_off_target": "14",
      "attempts_on_target": "27",
      "continent": "North, Central America and Caribbean",
      "country_code": "USA",
      "country_name": "USA",
      "def_attempted_clearances": "69",
      "def_attempted_clearances_ta": "49.8",
      "def_blocks": "19",
      "def_completed_clearances": "53",
      "def_completed_clearances_ta": "41.1",
      "def_offsides_given": "18",
      "def_offsides_given_ta": "7.8",
      "def_recovered_balls": "146",
      "def_recovered_balls_ta": "151",
      "def_saves": "27",
      "def_saves_ta": "12.9",
      "def_tackles": "82",
      "def_tackles_lost": "61",
      "def_tackles_lost_ta": "40.2",
      "def_tackles_tol": "82",
      "def_tackles_tol_ta": "62.9",
      "def_tackles_won": "21",
      "def_tackles_won_ta": "17.1",
      "def_total_defense": "128",
      "distance_covered": "496.8",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/usa.png",
      "goals_scored": "5",
      "id": 6,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=USA&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "4",
      "one_g_freq_attempts": "8.2",
      "one_g_freq_min": "78",
      "open_play_goals": "4",
      "pass_crosses": "64",
      "pass_crosses_ta": "71.3",
      "pass_long_passes_complete": "169",
      "pass_medium_passes_complete": "1034",
      "pass_short_passes_complete": "473",
      "pass_ta": "1406",
      "pass_throw_ins": "150",
      "pass_throw_ins_ta": "117",
      "pass_total": "1676",
      "rank": 13,
      "resource_uri": "/api/countries/USA/",
      "scoring_method_total": "5",
      "set_piece_goals": "1",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/usa.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/usa.gif",
      "team_video_url": "//www.youtube.com/embed/YJty7rg3eds",
      "tournament_average": "48.5"
    },
    {
      "article": "Spain will head to Brazil as defending champions. Remaining loyal to the style and players that have allowed them to dominate the global and European scenes over the last five years,  won the only qualification pool (aside from the South American group) to contain two world champions. In what was the smallest section in Europe with only five teams, the Spanish led the way from France thanks to a record of six wins and two draws, conceded to the French and Finland. In topping the group they let in a mere three goals, fewer than any other side in the European preliminaries. At the other end of the pitch, however, Spain enjoyed one of their less prolific campaigns, scoring only 14 times. Prior to lifting the coveted Trophy in South Africa, so frequent were their exits at the last eight of the finals that Spain were said to be suffering from a ‘quarter-final jinx’. Brazil 2014 will be 's tenth consecutive world finals appearance, and 14th in all, with their best performance before last year’s success coming at Brazil 1950. Having topped their first-round section, Spain went straight into the decisive four-team final group stage – where they finished fourth behind Uruguay, Brazil and Sweden. Though there is no doubt that Spain’s embarrassment of midfield riches, featuring the likes of Xavi, Andres Iniesta and Xabi Alonso, has been integral to their major trophy triumphs, are strong across the board. The men in red have a phalanx of very reliable keepers to call on, headed by Iker Casillas, while Sergio Ramos and Gerard Pique have consolidated their positions as the leaders of a defence in which left-back Jordi Alba has gone from strength to strength. Ramos and Alba are also a threat in the opposing box, and in recent times have made goalscoring contributions that have been almost as decisive as those of the front men. With both David Villa and Fernando Torres struggling to find their touch, a new star has arisen. After his amazing season with Atletico Madrid, the Brazilian-born Diego Costa is now the new hope in attack for . Vicente del BosqueFIFA World Cup South Africa 2010 (Winners), FIFA U-20 World Cup Nigeria 1999 (Winners), Men’s Olympic Football Tournament Barcelona 1992 (Winners)Luis Suarez, Emilio Butragueno, Fernando Hierro",
      "att_attempts": "35",
      "att_crosses": "45",
      "att_crosses_completed": "13",
      "att_crosses_completed_ta": "9.9",
      "att_crosses_ta": "41",
      "att_deliveries_penalty_area": "5",
      "att_deliveries_penalty_area_ta": "1.9",
      "att_dribble_penalty_area": "11",
      "att_dribble_penalty_area_ta": "6.4",
      "att_goals_scored": "9",
      "att_offsides": "12",
      "att_offsides_ta": "4.9",
      "att_shots_blocked": "4",
      "att_shots_saved": "10",
      "attempts_off_target": "12",
      "attempts_on_target": "23",
      "continent": "Europe",
      "country_code": "ESP",
      "country_name": "Spain",
      "def_attempted_clearances": "29",
      "def_attempted_clearances_ta": "29.4",
      "def_blocks": "1",
      "def_completed_clearances": "25",
      "def_completed_clearances_ta": "24.5",
      "def_offsides_given": "8",
      "def_offsides_given_ta": "4.9",
      "def_recovered_balls": "144",
      "def_recovered_balls_ta": "88.8",
      "def_saves": "7",
      "def_saves_ta": "7.3",
      "def_tackles": "31",
      "def_tackles_lost": "16",
      "def_tackles_lost_ta": "21.8",
      "def_tackles_tol": "31",
      "def_tackles_tol_ta": "36.7",
      "def_tackles_won": "12",
      "def_tackles_won_ta": "9.3",
      "def_total_defense": "39",
      "distance_covered": "325.5",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/Spain.png",
      "goals_scored": "4",
      "id": 7,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Spain&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "8.8",
      "one_g_freq_min": "68",
      "open_play_goals": "3",
      "pass_crosses": "45",
      "pass_crosses_ta": "41",
      "pass_long_passes_complete": "145",
      "pass_medium_passes_complete": "964",
      "pass_short_passes_complete": "594",
      "pass_ta": "868",
      "pass_throw_ins": "93",
      "pass_throw_ins_ta": "70.5",
      "pass_total": "1703",
      "rank": 1,
      "resource_uri": "/api/countries/Spain/",
      "scoring_method_total": "4",
      "set_piece_goals": "1",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/spain.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/esp.gif",
      "team_video_url": "//www.youtube.com/embed/p6CtWn89CgU",
      "tournament_average": "28.7"
    },
    {
      "article": "Germany topped Group C with an unbeaten record, sealing automatic qualification for the 2014 FIFA World Cup™ with nine victories from ten fixtures. Furthermore, coach Joachim Low’s charges hit 36 goals along the way, the most of any side in European zone qualifying. The three-time world champions’ eye-catching attacking displays have thrilled their fans and demonstrated why they are among the favourites to take the title in Brazil. However, there is still plenty of room for improvement. The 4-4 draw with Sweden in Berlin is a painful memory, especially after Germany had led 4-0 lead. “We still have work to do before the World Cup,” commented Low. “I see two main areas to focus on: we need to stabilise both our defence and our play in the final third.” Germany lie third in the all-time world football ranking with three FIFA World Cup triumphs, behind only Brazil on five and Italy on four. The 1954 team won the tournament in Switzerland as rank outsiders, in what became known as the Miracle of Berne. Franz Beckenbauer lifted the trophy on home soil in 1974, and Lothar Matthaus followed suit at Italy 1990.  The Germans have also finished runners-up four times, in 1966, 1982, 1986 and 2002, and came third on four occasions, in 1934 and 1970, and at the last two finals in 2006 and 2010. No other team has played more matches (99) or scored more goals (222) at the FIFA World Cup finals.  Keeper Manuel Neuer is the undisputed No1, while many experts believe he is the real deal, equipped not only to follow in the footsteps of Oliver Kahn and Jens Lehmann, but also to develop into one of the best in the world. Full-back Philipp Lahm and schemer Bastian Schweinsteiger earned their international spurs long ago: each has reached 100 caps but is still at their peak. The next generation appears immensely promising too. Former Real Madrid starlet Mesut Ozil, who now laces his boots at Arsenal was just 21 when he thrilled the crowds at the 2010 FIFA World Cup and is a gifted creative player with passing ability to match the best in the world. Up front, Thomas Muller won the adidas Golden Boot and was named Best Young Player at the 2010 finals, while youngsters Andre Schurrle, Toni Kroos and Mario Gotze keep getting better and better .  Joachim LowFIFA World Cup Switzerland 1954, Germany 1974, Italy 1990 (Winners), FIFA U-20 World Cup Australia 1981 (Winners) Franz Beckenbauer, Gerd Müller, Lothar Matthaus",
      "att_attempts": "97",
      "att_crosses": "148",
      "att_crosses_completed": "40",
      "att_crosses_completed_ta": "18.1",
      "att_crosses_ta": "78.3",
      "att_deliveries_penalty_area": "2",
      "att_deliveries_penalty_area_ta": "3.1",
      "att_dribble_penalty_area": "28",
      "att_dribble_penalty_area_ta": "11.8",
      "att_goals_scored": "23",
      "att_offsides": "17",
      "att_offsides_ta": "9",
      "att_shots_blocked": "18",
      "att_shots_saved": "27",
      "attempts_off_target": "29",
      "attempts_on_target": "71",
      "continent": "Europe",
      "country_code": "GER",
      "country_name": "Germany",
      "def_attempted_clearances": "104",
      "def_attempted_clearances_ta": "55.5",
      "def_blocks": "23",
      "def_completed_clearances": "88",
      "def_completed_clearances_ta": "46.1",
      "def_offsides_given": "20",
      "def_offsides_given_ta": "9.1",
      "def_recovered_balls": "327",
      "def_recovered_balls_ta": "168",
      "def_saves": "24",
      "def_saves_ta": "13.9",
      "def_tackles": "110",
      "def_tackles_lost": "79",
      "def_tackles_lost_ta": "43.7",
      "def_tackles_tol": "110",
      "def_tackles_tol_ta": "67.8",
      "def_tackles_won": "31",
      "def_tackles_won_ta": "18.5",
      "def_total_defense": "157",
      "distance_covered": "846.3",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/germany.png",
      "goals_scored": "18",
      "id": 8,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Germany&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "7",
      "one_g_freq_attempts": "5.4",
      "one_g_freq_min": "38",
      "open_play_goals": "15",
      "pass_crosses": "148",
      "pass_crosses_ta": "78.3",
      "pass_long_passes_complete": "377",
      "pass_medium_passes_complete": "2763",
      "pass_short_passes_complete": "1017",
      "pass_ta": "1583",
      "pass_throw_ins": "221",
      "pass_throw_ins_ta": "130",
      "pass_total": "4157",
      "rank": 2,
      "resource_uri": "/api/countries/Germany/",
      "scoring_method_total": "18",
      "set_piece_goals": "3",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/germany.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/ger.gif",
      "team_video_url": "//www.youtube.com/embed/RoSOGoolFGs",
      "tournament_average": "52.6"
    },
    {
      "article": "  Drawn into a group that contained not only world and European champions Spain but just five teams overall, France had precious little margin for error when their campaign kicked off. In the end, they made just one slip, losing at home to La Roja¬, but it was a defeat that cost them first place in the section. Didier Deschamps' side rarely sparkled during the group phase except for a fine performance on Spanish soil, where their efforts were finally rewarded with a last-gasp equaliser in a 1-1 draw. Ultimately they were destined for the play-offs, as they had been ahead of South Africa 2010, and their chances of reaching Brazil took a battering in Kiev, where Ukraine's superior desire and team spirit earned them a 2-0 advantage at the halfway stage in the tie. That left  requiring a display of perfection in the second leg, but, with the Stade de France crowd in feverish mood, the 1998 FIFA World Cup™ winners turned things around with a 3-0 win that could prove a turning point for a side containing a number of exciting fresh talents. Mamadou Sakho, Raphael Varane and Paul Pogba are the standard-bearers of the new generation, while the gifted youngsters who led France to FIFA U-20 World Cup glory in 2013 stand waiting in the wings.  France have always commanded respect on the global stage thanks to various legendary players and impressive performances dating back to 1930, but they made the leap to a whole new level in 1998. Whereas Platini, Alain Giresse, Jean Tigana and Co experienced agony at the semi-final stage in 1982 and 1986, the likes of Zinedine Zidane, Laurent Blanc and Didier Deschamps finally took  all the way, lifting the Trophy on home soil. That was followed by a surprise group-stage exit four years later, but they came close to adding a second star to their shirts in 2006, only losing out on penalties to Italy in the Final. Without 'Zizou' in their ranks, France then made a forgettable tilt at South Africa 2010, disappointing their supporters both on and off the pitch.  The French production line continues to turn out some of the most sought-after talents in the world game, but following in the footsteps of the 1998 world champions and 2006 runners-up has proved no easy task. Typically cited as among the favourites ahead of any major tournament,  failed to win a single game at either UEFA EURO 2008 or the 2010 FIFA World Cup, and took a laborious route through to the quarter-finals at EURO 2012. The present generation will undoubtedly be anxious to draw a line under that recent tournament form when they touch down in Brazil.France boast solidity and strength in depth at the back, with a top-drawer goalkeeper in Hugo Lloris and a rearguard bolstered by the European experience of Patrice Evra, Laurent Koscielny and Raphael Varane. In the midfield, Paul Pogba can produce moments of magic. Further forward Karim Benzema and Olivier Giroud both possess a keen eye for goal.Didier DeschampsFIFA World Cup France 1998 (Winners), Men's Olympic Football Tournament Los Angeles 1984 (Winners), FIFA Confederations Cup Korea/Japan 2001, France 2003 (Winners), FIFA U-17 World Cup Trinidad and Tobago 2001 (Winners), and FIFA Beach Soccer World Cup Rio de Janeiro 2005 (Winners) Just Fontaine, Michel Platini, Zinedine Zidane",
      "att_attempts": "90",
      "att_crosses": "138",
      "att_crosses_completed": "43",
      "att_crosses_completed_ta": "16.4",
      "att_crosses_ta": "70.3",
      "att_deliveries_penalty_area": "7",
      "att_deliveries_penalty_area_ta": "2.9",
      "att_dribble_penalty_area": "13",
      "att_dribble_penalty_area_ta": "10.3",
      "att_goals_scored": "21",
      "att_offsides": "10",
      "att_offsides_ta": "7.7",
      "att_shots_blocked": "8",
      "att_shots_saved": "28",
      "attempts_off_target": "33",
      "attempts_on_target": "57",
      "continent": "Europe",
      "country_code": "FRA",
      "country_name": "France",
      "def_attempted_clearances": "50",
      "def_attempted_clearances_ta": "48.4",
      "def_blocks": "10",
      "def_completed_clearances": "41",
      "def_completed_clearances_ta": "40.1",
      "def_offsides_given": "6",
      "def_offsides_given_ta": "7.7",
      "def_recovered_balls": "193",
      "def_recovered_balls_ta": "149",
      "def_saves": "10",
      "def_saves_ta": "12.9",
      "def_tackles": "65",
      "def_tackles_lost": "44",
      "def_tackles_lost_ta": "39.8",
      "def_tackles_tol": "65",
      "def_tackles_tol_ta": "62.3",
      "def_tackles_won": "20",
      "def_tackles_won_ta": "16.8",
      "def_total_defense": "90",
      "distance_covered": "528.4",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/france.png",
      "goals_scored": "8",
      "id": 9,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=France&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "5",
      "one_g_freq_attempts": "9",
      "one_g_freq_min": "45",
      "open_play_goals": "8",
      "pass_crosses": "138",
      "pass_crosses_ta": "70.3",
      "pass_long_passes_complete": "233",
      "pass_medium_passes_complete": "1360",
      "pass_short_passes_complete": "590",
      "pass_ta": "1390",
      "pass_throw_ins": "150",
      "pass_throw_ins_ta": "115",
      "pass_total": "2183",
      "rank": 17,
      "resource_uri": "/api/countries/France/",
      "scoring_method_total": "10",
      "set_piece_goals": "2",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/france.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/fra.gif",
      "team_video_url": "//www.youtube.com/embed/pCEvxlHMcDg",
      "tournament_average": "47.8"
    },
    {
      "article": " Drawn in Group F with Malawi, Kenya and Namibia, the Nigerians were always massive favourites to reach the final play-off round of qualifying, and they did not lose any matches in the group stage. They did draw three times, once against each opponent, with the most worrying result a 1-1 at home to Kenya when only a second half injury time goal by Nnamdi Oduamadi won the point. Once in the two-legged play-off, the Eagles drew the lowest-ranked team in Ethiopia and despite the improvement of the east Africans, Nigeria were seldom threatened in winning away 2-1 and at home 2-0. After impressing on their way to the second round in each of their first two FIFA World Cup appearances, 1994 and 1998, Nigeria have struggled since: going out at the group stage twice while taking just two points from their last six matches in the finals. A muddled South Africa 2010 campaign under Lars Lagerback did little to bolster Nigeria’s reputation, but Brazil 2014 offers another chance for the reigning African champions to soar.  Coach Stephen Keshi has earned a reputation as a no-nonsense boss who is not afraid to choose in-form domestic players at the expense of more well-known stars, and that policy paid handsome dividends as Nigeria won the 2013 edition of the CAF Africa Cup of Nations. Keshi has kept a relatively stable spine of the team since then, with Chelsea's John Obi Mikel leaving his mixed past with the Eagles behind to become the lynchpin of the side. In goal, Vincent Enyeama is an important veteran, while Victor Moses, Ahmed Musa and Emmanuel Emenike are key parts of a deep attack.  Stephen Keshi FIFA World Cup USA 1994, France 1998 (Round of 16), FIFA U-17 World Cup China 1985, Japan 1993, Korea Republic 2007 (Winners), Olympic Football Tournament Atlanta 1996 (Winners), FIFA U-20 World Cup Saudi Arabia 1989, Netherlands 2005 (Runners-up), FIFA U-17 World Cup UAE 2013 (Winners)Jay Jay Okocha, Nwankwo Kanu, Rashidi Yekini",
      "att_attempts": "50",
      "att_crosses": "87",
      "att_crosses_completed": "14",
      "att_crosses_completed_ta": "14.5",
      "att_crosses_ta": "62.6",
      "att_deliveries_penalty_area": "2",
      "att_deliveries_penalty_area_ta": "2.7",
      "att_dribble_penalty_area": "17",
      "att_dribble_penalty_area_ta": "9.1",
      "att_goals_scored": "13",
      "att_offsides": "6",
      "att_offsides_ta": "7.2",
      "att_shots_blocked": "3",
      "att_shots_saved": "16",
      "attempts_off_target": "18",
      "attempts_on_target": "32",
      "continent": "Africa",
      "country_code": "NGA",
      "country_name": "Nigeria",
      "def_attempted_clearances": "74",
      "def_attempted_clearances_ta": "43.1",
      "def_blocks": "10",
      "def_completed_clearances": "66",
      "def_completed_clearances_ta": "35.9",
      "def_offsides_given": "7",
      "def_offsides_given_ta": "7.3",
      "def_recovered_balls": "168",
      "def_recovered_balls_ta": "135",
      "def_saves": "21",
      "def_saves_ta": "11.2",
      "def_tackles": "83",
      "def_tackles_lost": "52",
      "def_tackles_lost_ta": "36.1",
      "def_tackles_tol": "83",
      "def_tackles_tol_ta": "57",
      "def_tackles_won": "22",
      "def_tackles_won_ta": "15.3",
      "def_total_defense": "114",
      "distance_covered": "402.1",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/nigeria.png",
      "goals_scored": "3",
      "id": 10,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Nigeria&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "4",
      "one_g_freq_attempts": "16.7",
      "one_g_freq_min": "120",
      "open_play_goals": "3",
      "pass_crosses": "87",
      "pass_crosses_ta": "62.6",
      "pass_long_passes_complete": "164",
      "pass_medium_passes_complete": "926",
      "pass_short_passes_complete": "296",
      "pass_ta": "1271",
      "pass_throw_ins": "119",
      "pass_throw_ins_ta": "104",
      "pass_total": "1386",
      "rank": 44,
      "resource_uri": "/api/countries/Nigeria/",
      "scoring_method_total": "3",
      "set_piece_goals": "0",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/nigeria.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/nga.gif",
      "team_video_url": "//www.youtube.com/embed/fetWGB62rOI",
      "tournament_average": "42.9"
    },
    {
      "article": "In the wake of  historic Olympic triumph at London 2012, few Mexico fans would have expected their side to struggle en route to Brazil. Yet struggle they did, to such an extent that they came within a whisker of missing out on qualification altogether. Despite their status as regional powerhouses, the Mexicans won just two of their ten matches in the final six-team group phase, with the defeat to Honduras at their Estadio Azteca fortress in September 2013 costing Jose Manuel de la Torre his job as national team coach with three games remaining. With his success at Monterrey still fresh in the memory, the experienced Victor Manuel Vucetich came on board for the final two matches. And though he oversaw a crucial home win over Panama, it was only thanks to the USA’s last-gasp defeat of the Panamanians on the final matchday that the Mexicans were able to scrape into the intercontinental play-off. Fresh from guiding America to the Mexican league title, Miguel Herrera then came in for the two-legged tie against New Zealand and took the radical decision of selecting only home-based players. His strategy paid off as  finally put their shaky form behind them to sweep to a 9-3 aggregate win and qualify for the world finals for the 15th time in all. Mexico have fallen in the Round of 16 on their last five appearances in the finals, with Argentina halting their progress at both Germany 2006 and South Africa 2010. Those defeats proved painful for  legion of fans, who have been waiting a long time to see their side return to last eight. Only twice have the Mexicans made it to the quarters, both time on home soil, in 1970 and 1986. After an agonising qualifying competition full of setbacks, coaching changes and tactical reshuffles, predicting how the Mexicans will fare at Brazil 2014 is no easy task. While  can count on a band of high-profile overseas-based players, spearheaded by Javier  Hernandez, Andres Guardado and Giovani dos Santos, the last few months have shown that the latest wave of young players also have much to offer, chief among them their London 2012 hero Oribe Peralta, Raul Jimenez and Carlos Pena. Now that they have safely secured their ticket to Brazil, the Mexicans have time to find some stability and build for the future. Miguel HerreraConfederations Cup Mexico 1999 (winners), FIFA U-17 World Cup Peru 2005 (winners) Antonio Carbajal, Hugo Sanchez, Jorge Campos, Cuauhtemoc Blanco",
      "att_attempts": "46",
      "att_crosses": "60",
      "att_crosses_completed": "14",
      "att_crosses_completed_ta": "13.8",
      "att_crosses_ta": "58.4",
      "att_deliveries_penalty_area": "4",
      "att_deliveries_penalty_area_ta": "2.6",
      "att_dribble_penalty_area": "6",
      "att_dribble_penalty_area_ta": "8.9",
      "att_goals_scored": "6",
      "att_offsides": "7",
      "att_offsides_ta": "6.7",
      "att_shots_blocked": "5",
      "att_shots_saved": "11",
      "attempts_off_target": "24",
      "attempts_on_target": "22",
      "continent": "North, Central America and Caribbean",
      "country_code": "MEX",
      "country_name": "Mexico",
      "def_attempted_clearances": "68",
      "def_attempted_clearances_ta": "40.5",
      "def_blocks": "10",
      "def_completed_clearances": "52",
      "def_completed_clearances_ta": "33.8",
      "def_offsides_given": "10",
      "def_offsides_given_ta": "6.8",
      "def_recovered_balls": "158",
      "def_recovered_balls_ta": "129",
      "def_saves": "10",
      "def_saves_ta": "10.8",
      "def_tackles": "68",
      "def_tackles_lost": "49",
      "def_tackles_lost_ta": "34.3",
      "def_tackles_tol": "68",
      "def_tackles_tol_ta": "54.1",
      "def_tackles_won": "18",
      "def_tackles_won_ta": "14.2",
      "def_total_defense": "90",
      "distance_covered": "425.3",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/mexico.png",
      "goals_scored": "5",
      "id": 11,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Mexico&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "4",
      "one_g_freq_attempts": "9.2",
      "one_g_freq_min": "72",
      "open_play_goals": "4",
      "pass_crosses": "60",
      "pass_crosses_ta": "58.4",
      "pass_long_passes_complete": "162",
      "pass_medium_passes_complete": "888",
      "pass_short_passes_complete": "343",
      "pass_ta": "1224",
      "pass_throw_ins": "118",
      "pass_throw_ins_ta": "100",
      "pass_total": "1393",
      "rank": 20,
      "resource_uri": "/api/countries/Mexico/",
      "scoring_method_total": "5",
      "set_piece_goals": "1",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/mexico.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/mex.gif",
      "team_video_url": "//www.youtube.com/embed/wK2CcP5rSNo",
      "tournament_average": "41.2"
    },
    {
      "article": "Under former Portugal coach Carlos Queiroz’s watch, Iran opened the preliminary competition brightly, scoring five unanswered goals past Maldives to progress. And Team Melli were met with little challenge in the next phase, maintaining their undefeated run as they finished section winners with three wins and three draws.  However, despite logging an average of nearly three goals per match in the previous round,the fourth round proved to be more difficult for the strongly favoured Iranians. They found the net just twice in the opening five matches during which they lost twice and drew once to see their campaign in jeopardy. With so much at stake, Queiroz’s side rose to the occasion to see off both Qatar and Lebanon, before overcoming hosts Korea Republic 1-0 in the round’s final match to seal their return to the FIFA World Cup.  Despite their presence within Asia, Iran have so far been unable to progress beyond the group phase at the FIFA World Cup. They finished their debut campaign with a point, courtesy of a 1-1 draw against Scotland. But their first win came in the second appearance when a golden generation, boasting the likes of Ali Daei, Karim Bagheri and Mehdi Mahdavikia, came up with a memorable 2-1 defeat of USA. Their last participation at Germany 2006 saw them head home with a point after a 1-1 draw against debutants Angola. Filling the void left by Mahdavikia is captain Javad Nekounam, who has quickly established his place as the team's talisman. Aside from providing leadership, the skipper provides creativity alongside former Osasuna team-mate Masoud Shojaei. Belgium-based striker Reza Ghoochannejhad stands out among the emerging generation, while Fulham man Ashkan Dejagah shores up the midfield alongside Andranik Teymourian. Carlos Queiroz  FIFA World Cup Argentina 1978, France 1998, Germany 2006 (Group stages), Men's Olympic Football Tournament Montreal 1976 (Quarter-finals)  Ali Daei, Khodadad Azizi, Karim Bagheri",
      "att_attempts": "22",
      "att_crosses": "60",
      "att_crosses_completed": "17",
      "att_crosses_completed_ta": "11.8",
      "att_crosses_ta": "49.7",
      "att_deliveries_penalty_area": "2",
      "att_deliveries_penalty_area_ta": "2.3",
      "att_dribble_penalty_area": "2",
      "att_dribble_penalty_area_ta": "7.8",
      "att_goals_scored": "5",
      "att_offsides": "10",
      "att_offsides_ta": "5.7",
      "att_shots_blocked": "1",
      "att_shots_saved": "6",
      "attempts_off_target": "10",
      "attempts_on_target": "12",
      "continent": "Asia",
      "country_code": "IRN",
      "country_name": "Iran",
      "def_attempted_clearances": "67",
      "def_attempted_clearances_ta": "34.6",
      "def_blocks": "8",
      "def_completed_clearances": "56",
      "def_completed_clearances_ta": "28.9",
      "def_offsides_given": "1",
      "def_offsides_given_ta": "5.8",
      "def_recovered_balls": "121",
      "def_recovered_balls_ta": "110",
      "def_saves": "12",
      "def_saves_ta": "9",
      "def_tackles": "72",
      "def_tackles_lost": "50",
      "def_tackles_lost_ta": "27.6",
      "def_tackles_tol": "72",
      "def_tackles_tol_ta": "45.2",
      "def_tackles_won": "13",
      "def_tackles_won_ta": "12.1",
      "def_total_defense": "92",
      "distance_covered": "323.5",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/iran.png",
      "goals_scored": "1",
      "id": 12,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Iran&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "22",
      "one_g_freq_min": "270",
      "open_play_goals": "1",
      "pass_crosses": "60",
      "pass_crosses_ta": "49.7",
      "pass_long_passes_complete": "86",
      "pass_medium_passes_complete": "363",
      "pass_short_passes_complete": "155",
      "pass_ta": "1053",
      "pass_throw_ins": "104",
      "pass_throw_ins_ta": "84.9",
      "pass_total": "604",
      "rank": 43,
      "resource_uri": "/api/countries/Iran/",
      "scoring_method_total": "1",
      "set_piece_goals": "0",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/iran.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/irn.gif",
      "team_video_url": "//www.youtube.com/embed/8Ia6ea9fSLA",
      "tournament_average": "35.2"
    },
    {
      "article": "After a 4-1 win against Chile to begin their FIFA World Cup™ qualifying campaign, Argentina then stumbled against Venezuela and drew 1-1 at home to Bolivia, which raised doubts as to whether coach Alejandro Sabella, who took over after Copa America 2011, was up to the task. , however,got back on track with 2-1 win over Colombia in Barranquilla, which began Argentina's 14-match unbeaten run through the remainder of qualifying, where they finished atop the South American table. Argentina tallied 35 goals while only surrendering 15 on the way to winning the preliminary competition for the third time. The rest of South America could only chase Argentina throughout the final qualifying fixtures.  Argentina have contested four FIFA World Cup Finals in all, the first of them at the inaugural tournament, Uruguay 1930, when they went down 4-2 to the host nation. Respective contributions from Mario Kempes and Diego Maradona inspired them to the biggest prize in football on home soil in 1978 and again at Mexico 1986, while their last showpiece appearance came at Italy 1990, when they were denied by an Andreas Brehme penalty. Since then they have been unable to progress beyond the quarter-finals. With the landmark achievement of claiming four consecutive FIFA Ballon d'Ors (2009-2012), Lionel Messi in the undisputed leader of the Argentina national team and a multiple-trophy winner with Barcelona. Breaking all kind of goal-records,  is now looking to achieve greatness with his country after failing, somewhat surprisingly, to find the back of the net at South Africa 2010. Supporting him will be an all-star cast featuring Carlos Tevez, Javier Mascherano and Angel Di Maria, all of them on top of their game with some of Europe’s leading clubs. Alejandro Sabella FIFA World Cup Argentina 1978, Mexico 1986 (Winners), FIFA U-20 World Cup Japan 1979, Qatar 1995, Malaysia 1997, Argentina 2001, Netherlands 2005, Canada 2007 (Winners), FIFA Confederations Cup Saudi Arabia 1992 (Winners), Men’s Olympic Football Tournament Athens 2004, Beijing 2008 (Winners)Daniel Passarella, Diego Maradona, Gabriel Batistuta, Mario Kempes",
      "att_attempts": "105",
      "att_crosses": "174",
      "att_crosses_completed": "33",
      "att_crosses_completed_ta": "18.1",
      "att_crosses_ta": "78.3",
      "att_deliveries_penalty_area": "5",
      "att_deliveries_penalty_area_ta": "3.1",
      "att_dribble_penalty_area": "32",
      "att_dribble_penalty_area_ta": "11.8",
      "att_goals_scored": "27",
      "att_offsides": "8",
      "att_offsides_ta": "9",
      "att_shots_blocked": "7",
      "att_shots_saved": "29",
      "attempts_off_target": "42",
      "attempts_on_target": "63",
      "continent": "South America",
      "country_code": "ARG",
      "country_name": "Argentina",
      "def_attempted_clearances": "98",
      "def_attempted_clearances_ta": "55.5",
      "def_blocks": "19",
      "def_completed_clearances": "85",
      "def_completed_clearances_ta": "46.1",
      "def_offsides_given": "19",
      "def_offsides_given_ta": "9.1",
      "def_recovered_balls": "328",
      "def_recovered_balls_ta": "168",
      "def_saves": "19",
      "def_saves_ta": "13.9",
      "def_tackles": "118",
      "def_tackles_lost": "81",
      "def_tackles_lost_ta": "43.7",
      "def_tackles_tol": "118",
      "def_tackles_tol_ta": "67.8",
      "def_tackles_won": "35",
      "def_tackles_won_ta": "18.5",
      "def_total_defense": "157",
      "distance_covered": "821.9",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/argentina.png",
      "goals_scored": "7",
      "id": 13,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Argentina&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "7",
      "one_g_freq_attempts": "13.1",
      "one_g_freq_min": "90",
      "open_play_goals": "7",
      "pass_crosses": "174",
      "pass_crosses_ta": "78.3",
      "pass_long_passes_complete": "349",
      "pass_medium_passes_complete": "2232",
      "pass_short_passes_complete": "763",
      "pass_ta": "1583",
      "pass_throw_ins": "260",
      "pass_throw_ins_ta": "130",
      "pass_total": "3344",
      "rank": 5,
      "resource_uri": "/api/countries/Argentina/",
      "scoring_method_total": "8",
      "set_piece_goals": "1",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/argentina.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/arg.gif",
      "team_video_url": "//www.youtube.com/embed/MsNLpGHC6MM",
      "tournament_average": "52.6"
    },
    {
      "article": " The arrival of the Colombian Jorge Luis Pinto as national team coach has ushered in a new era for Costa Rica. Joining the CONCACAF preliminaries in Round 3,  finished second behind Mexico in their group to advance to the final six-team phase, where they sealed their ticket to Brazil 2014 with two games to spare, eventually finishing second behind USA. Their successful campaign was based on two key factors. The first was their solidity at the back, with Pinto’s side conceding only seven goals in the final round, fewer than any other team. The second was their formidable home record of five wins in five games in the final phase. Costa Rica played their first game as a national team in 1921, a 7-0 win over Central American neighbours El Salvador. As they developed as a side, things weren’t always quite so easy, but after many years of manful efforts they finally managed to reach the world’s biggest football tournament in 1990, taking full advantage of Mexico’s suspension to reach the finals in Italy. Once there, they beat Sweden and Scotland to reach the knockout rounds in an impressive debut under the care of wily boss Bora Milutinovic, where they lost to Czechoslovakia. They returned to the world stage in 2002 after narrowly failing to reach USA 1994 and France 1998. Drawn into a tricky group alongside eventual champions Brazil and semi-finalists Turkey, the valiant went out at the first hurdle, the same stage where they would make their exit in a significantly poorer showing four years later in Germany. Costa Rica’s fortunes lie at the skilful feet of one Bryan Ruiz. Called “a truly special player” by former coach Rodrigo Kenton, Ruiz established himself at club side Twente in the Netherlands before moving on to Fulham in England. Now back in the Eredivisie with PSV Eindhoven, he ranks among the best playmakers in the North, Central American and Caribbean zone. Alongside Ruiz are a number of tried-and-trusted performers like Christian Bolanos and outstanding goalkeeper Keylor Navas.The dribbling skills and all-around attacking play of the young Joel Campbell have made him another of  most valuable assets. Jorge Luis Pinto FIFA World Cup Italy 1990 (Round of 16), FIFA U-20 World Cup Egypt 2009 (Fourth place)Hernan Medford, Paulo Wanchope, Walter Centeno ",
      "att_attempts": "38",
      "att_crosses": "62",
      "att_crosses_completed": "12",
      "att_crosses_completed_ta": "17.3",
      "att_crosses_ta": "73.8",
      "att_deliveries_penalty_area": "2",
      "att_deliveries_penalty_area_ta": "3",
      "att_dribble_penalty_area": "9",
      "att_dribble_penalty_area_ta": "11",
      "att_goals_scored": "5",
      "att_offsides": "11",
      "att_offsides_ta": "8.4",
      "att_shots_blocked": "5",
      "att_shots_saved": "8",
      "attempts_off_target": "20",
      "attempts_on_target": "18",
      "continent": "North, Central America and Caribbean",
      "country_code": "CRC",
      "country_name": "Costa Rica",
      "def_attempted_clearances": "81",
      "def_attempted_clearances_ta": "52",
      "def_blocks": "19",
      "def_completed_clearances": "62",
      "def_completed_clearances_ta": "43.1",
      "def_offsides_given": "41",
      "def_offsides_given_ta": "8.5",
      "def_recovered_balls": "222",
      "def_recovered_balls_ta": "156",
      "def_saves": "21",
      "def_saves_ta": "13.3",
      "def_tackles": "104",
      "def_tackles_lost": "62",
      "def_tackles_lost_ta": "41.4",
      "def_tackles_tol": "104",
      "def_tackles_tol_ta": "64.6",
      "def_tackles_won": "29",
      "def_tackles_won_ta": "17.5",
      "def_total_defense": "144",
      "distance_covered": "596.6",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/costa_rica.png",
      "goals_scored": "5",
      "id": 14,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=CostaRica&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "5",
      "one_g_freq_attempts": "7.6",
      "one_g_freq_min": "102",
      "open_play_goals": "4",
      "pass_crosses": "62",
      "pass_crosses_ta": "73.8",
      "pass_long_passes_complete": "197",
      "pass_medium_passes_complete": "958",
      "pass_short_passes_complete": "435",
      "pass_ta": "1458",
      "pass_throw_ins": "169",
      "pass_throw_ins_ta": "122",
      "pass_total": "1590",
      "rank": 28,
      "resource_uri": "/api/countries/Costa%20Rica/",
      "scoring_method_total": "5",
      "set_piece_goals": "1",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/costa_rica.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/crc.gif",
      "team_video_url": "//www.youtube.com/embed/H1R8R0via38",
      "tournament_average": "49.9"
    },
    {
      "article": "Buoyed by their fourth place finish at South Africa 2010 and their Copa America triumph a year later, La Celeste went into the South American qualifying competition for Brazil 2014 as firm favourites to progress. Their plans went awry in 2012, however, when they collected just two points out of a possible 18. The Uruguayans recovered their poise just in time, eventually edging into fifth and booking a place in the intercontinental play-offs for the fourth time in a row. Waiting for them there were Jordan, who were no match for Uruguay in the first leg in Amman, which ended in a 5-0 win for the visitors. Defending that lead comfortably in a goalless draw back in Montevideo, the Uruguayans made sure of their berth in Brazil. Prior to the 1970s, when they began a lengthy period in the doldrums, Uruguay were widely regarded as one of the giants of world football. That status was founded on their two FIFA World Cup™ wins, the first of them coming at home in 1930 and the second in Brazil 20 years later, when they stunned the host nation with a shock 2-1 win at the Maracana, an epoch-defining game that will forever be known as . Their run to the semi-finals at Mexico 1970 would be their last flourish for some considerable time, however. In the years that followed the Uruguayans appeared only infrequently in the global showpiece. After failing to qualify for USA 1994 and France 1998,  made their return at Korea/Japan 2002 only to go out in the group phase and then lose out to Australia in the play-off for a place at Germany 2006. Another play-off followed in the qualifiers for South Africa 2010, this time against Costa Rica and this time safely negotiated. In what was their 11th world finals, the Uruguayans brought back memories of yesteryear by surging to fourth place, with the inspirational Diego Forlan making off with the adidas Golden Ball as the tournament’s outstanding player. Strikers Luis Suarez and Edinson Cavani have become the standard bearers for Uruguayan football and the national team over the last couple of years. The Liverpool man ended the South American preliminaries as the leading scorer with 11 goals, and was the second most-used player by coach Oscar Tabarez. The deadly duo have plenty of ballast behind them, with the vastly experienced Diego Lugano directing rearguard operations with aplomb, and Fernando Muslera providing a safe pair of hands between the posts. Even so, after an often-troubled qualifying campaign  Tabarez will no doubt be looking to shuffle his pack and build up some momentum ahead of Brazil 2014. Oscar Washington TabarezFIFA World Cup Uruguay 1930 and Brazil 1950 (winners), Men’s Olympic Football Tournament Paris 1924, Amsterdam 1928 (winners), FIFA U-20 World Cup Malaysia 1997 (runners-up), FIFA Beach Soccer World Cup Rio de Janeiro 2006 (runners-up), FIFA U-17 World Cup Mexico 2011 (runners-up) Hector Scarone, Angel Romano, Obdulio Varela, Roque Maspoli, Alcides Ghiggia, Ladislao Mazurkiewicz, Pedro Rocha, Rodolfo Rodriguez, Hugo De Leon, Carlos Alberto Aguilera, Ruben Sosa, Enzo Francescoli, Alvaro Recoba ",
      "att_attempts": "48",
      "att_crosses": "76",
      "att_crosses_completed": "16",
      "att_crosses_completed_ta": "17",
      "att_crosses_ta": "72.4",
      "att_deliveries_penalty_area": "3",
      "att_deliveries_penalty_area_ta": "3",
      "att_dribble_penalty_area": "5",
      "att_dribble_penalty_area_ta": "10.6",
      "att_goals_scored": "11",
      "att_offsides": "11",
      "att_offsides_ta": "8",
      "att_shots_blocked": "4",
      "att_shots_saved": "13",
      "attempts_off_target": "20",
      "attempts_on_target": "29",
      "continent": "South America",
      "country_code": "URU",
      "country_name": "Uruguay",
      "def_attempted_clearances": "58",
      "def_attempted_clearances_ta": "50.9",
      "def_blocks": "9",
      "def_completed_clearances": "47",
      "def_completed_clearances_ta": "42.2",
      "def_offsides_given": "7",
      "def_offsides_given_ta": "8",
      "def_recovered_balls": "162",
      "def_recovered_balls_ta": "154",
      "def_saves": "10",
      "def_saves_ta": "13",
      "def_tackles": "84",
      "def_tackles_lost": "46",
      "def_tackles_lost_ta": "40.9",
      "def_tackles_tol": "84",
      "def_tackles_tol_ta": "63.8",
      "def_tackles_won": "12",
      "def_tackles_won_ta": "17.3",
      "def_total_defense": "103",
      "distance_covered": "419.5",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/uruguay.png",
      "goals_scored": "4",
      "id": 15,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Uruguay&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "4",
      "one_g_freq_attempts": "12.3",
      "one_g_freq_min": "90",
      "open_play_goals": "2",
      "pass_crosses": "76",
      "pass_crosses_ta": "72.4",
      "pass_long_passes_complete": "147",
      "pass_medium_passes_complete": "789",
      "pass_short_passes_complete": "288",
      "pass_ta": "1427",
      "pass_throw_ins": "143",
      "pass_throw_ins_ta": "120",
      "pass_total": "1224",
      "rank": 7,
      "resource_uri": "/api/countries/Uruguay/",
      "scoring_method_total": "4",
      "set_piece_goals": "2",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/uruguay.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/uru.gif",
      "team_video_url": "//www.youtube.com/embed/eELyHuqYlsU",
      "tournament_average": "49.1"
    },
    {
      "article": "The mammoth, two-year qualifying campaign saw Japan progress game-by-game under Alberto Zaccheroni, who took over in the wake of the team’s impressive run at the 2010 FIFA World Cup South Africa™. The new-look Japan were struggling to fit into the Italian’s strategy as they began their qualifying bid in lacklustre style, losing to Uzbekistan and Korea DPR before seeing their progression into the fourth round secured.  Their transition proved successful, inspired by talisman Keisuke Honda and spearheaded by the likes of Shinji Kagawa and Shinji Okazaki, the Japanese began to gel in the fourth round. Two emphatic opening victories over Oman (3-0) and Jordan (6-0) saw the Samurai Blue as the group’s runaway leaders and although they were held by Australia to a 1-1 draw, Oman and Iraq’s losses put Zaccheroni’s side on the cusp of qualification. An unexpected 2-1 loss in Jordan may have briefly delayed their celebration party, but they battled back to draw Australia 1-1, providing Japan with the requisite point to seal their fifth successive FIFA World Cup appearance.  They failed to live up to the expectations in their debut FIFA World Cup, losing three straight games to bow out. However, 2002 Korea/Japan saw them make history on home soil in Asia's first FIFA World Cup, winning a group that also featured Russia, Belgium and Tunisia to storm into the second round, only to lose out to eventual third-place finishers Turkey by a solitary goal. They were brought back down to earth at Germany 2006, salvaging merely a point from three group games to dump out. They more than redeemed themselves at South Africa 2010 though, progressing to the second stage at the expense of the likes of Denmark and Cameroon. They came close to stunning Paraguay in the consequent round-of-16 clash, with the South Americans only advancing through a penalty shootout victory after regular and extra time finished goalless.  Having excelled during the last FIFA World Cup and the recent AFC Asian Cup, AC Milan midfielder Keisuke Honda has quickly established his place as the team's new leader, filling the void left by Hidetoshi Nakata and Shunsuke Nakamura.  Spearheading the attacking-line are Shinji Kagawa and Shinji Okazaki, who finished the continental finals as the team's top-scorer with three goals. Driving the central field alongside Honda is set-piece specialist Yasuhito Endo while Schalke defender Atsuto Uchida is the key man at the rearguard. Alberto Zaccheroni  Men’s Olympic Football Tournament Mexico City 1968 (Third place), FIFA U-20 World Cup Nigeria 1999 (Runners-up), FIFA U-17 World Cup Mexico 2011 (Quarter-finals)  Kazuyoshi Miura, Shunsuke Nakamura, Hidetoshi Nakata ",
      "att_attempts": "46",
      "att_crosses": "58",
      "att_crosses_completed": "13",
      "att_crosses_completed_ta": "10.5",
      "att_crosses_ta": "44.9",
      "att_deliveries_penalty_area": "2",
      "att_deliveries_penalty_area_ta": "2.2",
      "att_dribble_penalty_area": "6",
      "att_dribble_penalty_area_ta": "7.1",
      "att_goals_scored": "13",
      "att_offsides": "2",
      "att_offsides_ta": "5.3",
      "att_shots_blocked": "2",
      "att_shots_saved": "13",
      "attempts_off_target": "18",
      "attempts_on_target": "28",
      "continent": "Asia",
      "country_code": "JPN",
      "country_name": "Japan",
      "def_attempted_clearances": "23",
      "def_attempted_clearances_ta": "31.8",
      "def_blocks": "8",
      "def_completed_clearances": "19",
      "def_completed_clearances_ta": "26.4",
      "def_offsides_given": "8",
      "def_offsides_given_ta": "5.3",
      "def_recovered_balls": "106",
      "def_recovered_balls_ta": "99.8",
      "def_saves": "8",
      "def_saves_ta": "7.9",
      "def_tackles": "44",
      "def_tackles_lost": "24",
      "def_tackles_lost_ta": "24.6",
      "def_tackles_tol": "44",
      "def_tackles_tol_ta": "40.7",
      "def_tackles_won": "9",
      "def_tackles_won_ta": "10.5",
      "def_total_defense": "61",
      "distance_covered": "317.5",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/japan.png",
      "goals_scored": "2",
      "id": 16,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Japan&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "23",
      "one_g_freq_min": "135",
      "open_play_goals": "2",
      "pass_crosses": "58",
      "pass_crosses_ta": "44.9",
      "pass_long_passes_complete": "116",
      "pass_medium_passes_complete": "811",
      "pass_short_passes_complete": "347",
      "pass_ta": "956",
      "pass_throw_ins": "90",
      "pass_throw_ins_ta": "77.9",
      "pass_total": "1274",
      "rank": 46,
      "resource_uri": "/api/countries/Japan/",
      "scoring_method_total": "2",
      "set_piece_goals": "0",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/japan.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/jpn.gif",
      "team_video_url": "//www.youtube.com/embed/cR37y8EtLRs",
      "tournament_average": "31.8"
    },
    {
      "article": "Having cruised to the 2010 FIFA World Cup South Africa™ with two games to spare, Australia entered their second qualifying campaign for the global showpiece since joining AFC targeting a second consecutive and smooth qualification. Instead, the road to Brazil 2014 proved to be a bumpy one for the Socceroos, who had to overcome some erratic form to secure their progression.  A narrow comeback win over Thailand and a loss to Oman in the opening stage served as a warning shot, although they ultimately progressed to the next phase as group winners. Then the Australians opened the next round in miserable fashion, drawing against Oman and Japan before losing to Jordan 2-1.  Though stunned, they rallied to claw back into contention with a victory over Iraq before two draws and a 4-0 defeat of Jordan put them on the cusp of qualification. They kept their cool in the final match of the round against Iraq as substitute Josh Kennedy scored late to seal their passage through. Coach Holger Osieck was dismissed in October 2013 after successive 6-0 defeats against Brazil and France, with former Brisbane Roar, Melbourne Victory and National Youth Teams coach Ange Postecoglou appointed.Though a team made up entirely of amateurs secured a scoreless draw against Chile, Australia departed from the 1974 FIFA World Cup without a goal to show from their inaugural appearance. The Socceroos made up for lost time at Germany 2006 and qualified for the Round of 16 before narrowly falling to eventual champions Italy. The German theme continued at South Africa 2010 although this time Australia suffered a 4-0 loss against the European giants in a scoreline which ultimately scuppered their progress. A ten-man 1-1 draw against Ghana and a 2-1 win against Serbia saw the Aussies eliminated on goal difference, three goals off the Africans. Tim Cahill remains the team’s undoubted star and talisman with a stunning goal ratio from midfield and equally remarkable heading ability despite his modest stature. Crystal Palace midfielder Mile Jedinak will look to carry his consistent performances in the English Premier League into Brazil 2014 for the Socceroos. Ange Postecoglou FIFA World Cup Germany 2006 (Round of 16), FIFA U-17 World Cup New Zealand 1999 (Runners-up)  Johnny Warren, Mark Viduka, Scott Chipperfield",
      "att_attempts": "26",
      "att_crosses": "47",
      "att_crosses_completed": "11",
      "att_crosses_completed_ta": "9.9",
      "att_crosses_ta": "41",
      "att_deliveries_penalty_area": "2",
      "att_deliveries_penalty_area_ta": "1.9",
      "att_dribble_penalty_area": "7",
      "att_dribble_penalty_area_ta": "6.4",
      "att_goals_scored": "5",
      "att_offsides": "3",
      "att_offsides_ta": "4.9",
      "att_shots_blocked": "3",
      "att_shots_saved": "5",
      "attempts_off_target": "13",
      "attempts_on_target": "14",
      "continent": "Asia",
      "country_code": "AUS",
      "country_name": "Australia",
      "def_attempted_clearances": "32",
      "def_attempted_clearances_ta": "29.4",
      "def_blocks": "11",
      "def_completed_clearances": "28",
      "def_completed_clearances_ta": "24.5",
      "def_offsides_given": "8",
      "def_offsides_given_ta": "4.9",
      "def_recovered_balls": "124",
      "def_recovered_balls_ta": "88.8",
      "def_saves": "11",
      "def_saves_ta": "7.3",
      "def_tackles": "47",
      "def_tackles_lost": "31",
      "def_tackles_lost_ta": "21.8",
      "def_tackles_tol": "47",
      "def_tackles_tol_ta": "36.7",
      "def_tackles_won": "9",
      "def_tackles_won_ta": "9.3",
      "def_total_defense": "70",
      "distance_covered": "354.3",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/australia.png",
      "goals_scored": "3",
      "id": 17,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Australia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "9",
      "one_g_freq_min": "90",
      "open_play_goals": "2",
      "pass_crosses": "47",
      "pass_crosses_ta": "41",
      "pass_long_passes_complete": "120",
      "pass_medium_passes_complete": "752",
      "pass_short_passes_complete": "231",
      "pass_ta": "868",
      "pass_throw_ins": "101",
      "pass_throw_ins_ta": "70.5",
      "pass_total": "1103",
      "rank": 62,
      "resource_uri": "/api/countries/Australia/",
      "scoring_method_total": "3",
      "set_piece_goals": "1",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/australia.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/aus.gif",
      "team_video_url": "//www.youtube.com/embed/2gn6VWRWkzY",
      "tournament_average": "28.7"
    },
    {
      "article": " England finished top of European Group H to reach the 2014 FIFA World Cup™ after securing victory on the final matchday against Poland, banishing the demons of four decades earlier when a draw against the same opponents saw the Three Lions miss out on the 1974 tournament.  The road to Brazil 2014 was not as smooth as their campaign to reach South Africa, where they won nine of their ten matches on the way to the 2010 finals. Even though Roy Hodgson guided his side to an undefeated campaign, automatic qualification evaded England until the final match at Wembley. Two draws against closest rivals Ukraine, as well as stalemates in Warsaw and Podogorica, left England fans nervous until captain Steven Gerrard put the home match against Poland beyond doubt with a late goal to double his side's advantage and seal qualification. England have appeared at 13 editions of the FIFA World Cup, including seven of the last eight. They were below-par at South Africa in 2010, narrowly qualifying from their group with a victory in the final match against Slovenia, before being outclassed 4-1 by Joachim Low’s Germany at the Round of 16 stage. The Three Lions have been FIFA World Cup winners once, in 1966 when they were hosts, but have since suffered a succession of early exits. Sir Bobby Robson came closest to matching the achievements of Sir Alf Ramsey’s ‘Wingless Wonders’, guiding England to the semi-finals at Italy 1990 only to be knocked out on penalties by Germany.  Wayne Rooney remains England’s greatest talent and his seven goals in six World Cup qualifying starts underlined his importance to Roy Hodgson's side. In midfield, Gerrard and Frank Lampard provide experience and creativity while young guns Jack Wilshere, Alex Oxlade-Chamberlain and Ross Barkley highlight the Three Lions' attacking flair for the future. Danny Welbeck came into his own during qualification, scoring four goals on the way to the finals, while Daniel Sturridge's emergence as one of the English Premier League's top forwards can only bolster Roy Hodgson's attacking options for Brazil. Roy Hodgson FIFA World Cup England 1966 (Winners), FIFA World Youth Championship Australia 1993 (Third place) Sir Bobby Charlton, Peter Shilton, Gary Lineker",
      "att_attempts": "39",
      "att_crosses": "70",
      "att_crosses_completed": "15",
      "att_crosses_completed_ta": "10.5",
      "att_crosses_ta": "44.9",
      "att_deliveries_penalty_area": "4",
      "att_deliveries_penalty_area_ta": "2.2",
      "att_dribble_penalty_area": "10",
      "att_dribble_penalty_area_ta": "7.1",
      "att_goals_scored": "7",
      "att_offsides": "2",
      "att_offsides_ta": "5.3",
      "att_shots_blocked": "2",
      "att_shots_saved": "10",
      "attempts_off_target": "20",
      "attempts_on_target": "19",
      "continent": "Europe",
      "country_code": "ENG",
      "country_name": "England",
      "def_attempted_clearances": "39",
      "def_attempted_clearances_ta": "31.8",
      "def_blocks": "4",
      "def_completed_clearances": "32",
      "def_completed_clearances_ta": "26.4",
      "def_offsides_given": "13",
      "def_offsides_given_ta": "5.3",
      "def_recovered_balls": "112",
      "def_recovered_balls_ta": "99.8",
      "def_saves": "6",
      "def_saves_ta": "7.9",
      "def_tackles": "33",
      "def_tackles_lost": "21",
      "def_tackles_lost_ta": "24.6",
      "def_tackles_tol": "33",
      "def_tackles_tol_ta": "40.7",
      "def_tackles_won": "6",
      "def_tackles_won_ta": "10.5",
      "def_total_defense": "43",
      "distance_covered": "319.0",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/england.png",
      "goals_scored": "2",
      "id": 18,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=England&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "19.5",
      "one_g_freq_min": "135",
      "open_play_goals": "2",
      "pass_crosses": "70",
      "pass_crosses_ta": "44.9",
      "pass_long_passes_complete": "160",
      "pass_medium_passes_complete": "796",
      "pass_short_passes_complete": "330",
      "pass_ta": "956",
      "pass_throw_ins": "87",
      "pass_throw_ins_ta": "77.9",
      "pass_total": "1286",
      "rank": 10,
      "resource_uri": "/api/countries/England/",
      "scoring_method_total": "2",
      "set_piece_goals": "0",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/england.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/eng.gif",
      "team_video_url": "//www.youtube.com/embed/-6q5xn84kGU",
      "tournament_average": "31.8"
    },
    {
      "article": " Following their group-phase exit at South Africa 2010 and the departure of coach Reinaldo Rueda,  went through a rocky period. The appointment of Luis Fernando Suarez in March 2011 brought stability to the national set-up, however, with the new coach also working hard with Honduras’ youth sides, steering the U-23s to the quarter-finals of the Men’s Olympic Football Tournament London 2012. Having gauged the quality of the country’s new generation, Suarez set about rejuvenating the full national team, giving it fresh impetus by drafting in a clutch of promising youngsters. The result was a convincing performance in Round 3 of the CONCACAF preliminaries, with topping their group on goal difference from Panama to knock out Canada and Cuba.  They went on to take the third and last direct qualifying slot in the final six-team phase, an achievement made possible by their form at home, where they dropped just four points, and an era-defining defeat of Mexico at their Azteca fortress in September 2013.  Upon making their first FIFA World Cup return in nearly three decades, Honduras were faced with tough group adversaries in South Africa, including eventual World Champions Spain. The Hondurans opened the tournament with a 1-0 loss to Chile, and soon became the ill-fated team to first encounter the wrath of tournament top-scorer David Villa, who grabbed both goals in Spain’s 2-0 win. In their only other FIFA World Cup appearance, Jose de La Paz held the coaching reins and steered Honduras to a surprising opening 1-1 draw with Spain, the 1982 tournament’s hosts, and followed up that account with the same scoreline against Northern Ireland. Their campaign was cut short, however, at the group stage after Yugoslavia beat 1-0 thanks to a late goal. Left-back Emilio Izaguirre was the find of the 2010/11 season for Celtic - named Scottish Premier League Player of the Year - and is a key force within Honduras's respectable backline. He is helped by captain and goalkeeper Noel Valladares who, despite a shy off-the-field personality, played an instrumental role in Honduras's qualification for South Africa 2010 and their deep run at the latest instalment of the Gold Cup. Wilson Palacios, one of the more recognisable faces of Honduran football playing for Stoke City, is also a crucial piece of the Honduran puzzle.  The front line have been doing their bit too, where old hand Carlo Costly has impressed alongside rising star Jerry Bengtson, who burst on to the international scene at London 2012 and top-scored for  in the qualifiers with nine goals. Luis Fernando Suarez FIFA World Cup Spain 1982, South Africa 2010 (Group stages) Amado Guevara, Carlos Pavón, Danny Turcios ",
      "att_attempts": "33",
      "att_crosses": "44",
      "att_crosses_completed": "10",
      "att_crosses_completed_ta": "11.8",
      "att_crosses_ta": "49.7",
      "att_deliveries_penalty_area": "2",
      "att_deliveries_penalty_area_ta": "2.3",
      "att_dribble_penalty_area": "6",
      "att_dribble_penalty_area_ta": "7.8",
      "att_goals_scored": "8",
      "att_offsides": "3",
      "att_offsides_ta": "5.7",
      "att_shots_blocked": "1",
      "att_shots_saved": "8",
      "attempts_off_target": "16",
      "attempts_on_target": "17",
      "continent": "North, Central America and Caribbean",
      "country_code": "HON",
      "country_name": "Honduras",
      "def_attempted_clearances": "36",
      "def_attempted_clearances_ta": "34.6",
      "def_blocks": "10",
      "def_completed_clearances": "32",
      "def_completed_clearances_ta": "28.9",
      "def_offsides_given": "4",
      "def_offsides_given_ta": "5.8",
      "def_recovered_balls": "122",
      "def_recovered_balls_ta": "110",
      "def_saves": "11",
      "def_saves_ta": "9",
      "def_tackles": "69",
      "def_tackles_lost": "41",
      "def_tackles_lost_ta": "27.6",
      "def_tackles_tol": "69",
      "def_tackles_tol_ta": "45.2",
      "def_tackles_won": "25",
      "def_tackles_won_ta": "12.1",
      "def_total_defense": "90",
      "distance_covered": "288.3",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/honduras.png",
      "goals_scored": "1",
      "id": 19,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Honduras&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "3",
      "one_g_freq_attempts": "33",
      "one_g_freq_min": "270",
      "open_play_goals": "1",
      "pass_crosses": "44",
      "pass_crosses_ta": "49.7",
      "pass_long_passes_complete": "122",
      "pass_medium_passes_complete": "668",
      "pass_short_passes_complete": "256",
      "pass_ta": "1053",
      "pass_throw_ins": "81",
      "pass_throw_ins_ta": "84.9",
      "pass_total": "1046",
      "rank": 33,
      "resource_uri": "/api/countries/Honduras/",
      "scoring_method_total": "1",
      "set_piece_goals": "0",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/honduras.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/hon.gif",
      "team_video_url": "//www.youtube.com/embed/IZsYf0Ov8g0",
      "tournament_average": "35.2"
    },
    {
      "article": "Greece enjoyed an excellent qualification campaign. Their points total of 25 from their ten games would have been enough to see them through as winners in five of the other eight groups; instead, they had to endure a play-off after losing out on goal difference to Bosnia-Herzegovina. Five of their eight victories were secured with 1-0 scorelines, and it was only against Group G’s eventual winners that the Greeks dropped points after a 0-0 draw at home and a 3-1 defeat in Zenica.  In the play-offs, Fernando Santos’ men were pitted against a Romanian outfit that boasted its fair share of FIFA World Cup™ experience, but the UEFA EURO 2004 winners carried their good form into the two-legged tie and advanced comfortably. After a storming 3-1 win at home, a 1-1 draw in Bucharest was enough for Greece to seal their place in Brazil next summer. Three of their four goals came from in-form striker Konstantinos Mitroglou, whose five strikes during qualifying make him Greece’s most potent attacking option.  The undoubted high point in Greek footballing history was their stunning triumph at EURO 2004 in Portugal, but their record at the FIFA World Cup finals is distinctly modest. At USA 1994, they departed for home with no points and no goals following group stage defeats to Argentina (4-0), Bulgaria (4-0) and Nigeria (2-0). Some 16 years later, the trip to South Africa did produce a 2-1 win over Nigeria, but 2-0 defeats to Korea Republic and Argentina meant another group stage exit.  The Greek FA and EURO 2004-winning coach Otto Rehhagel parted company after a disappointing 2010 World Cup, bringing an end to the veteran German’s nine-year tenure. His successor, Fernando Santos from Portugal, has effected a seamless transition, first guiding the team to EURO 2012 – where they were beaten by Germany in the quarter-finals – before delivering their most recent success by reaching next year’s World Cup.  Captain and seasoned midfield general Georgios Karagounis remains the dominant figure in the Greek line-up but forwards Dimitrios Salpingidis and Mitroglou will certainly have a part to play and provide Santos with a variety of attacking options. He can also call on the experience of the likes of Theofanis Gekas and Giorgos Samaras, which will be key when the tournament begins. Incidentally, though, despite their array of attacking talent, it was Greece’s defence that stole the show in qualifying, laying the foundation for success by conceding just four times in ten matches.  Fernando SantosUSA1994, South Africa 2010 (Group stages) Theodoros Zagorakis, Antonios Nikopolidis, Angelos Basinas",
      "att_attempts": "57",
      "att_crosses": "118",
      "att_crosses_completed": "19",
      "att_crosses_completed_ta": "14.2",
      "att_crosses_ta": "60.6",
      "att_deliveries_penalty_area": "2",
      "att_deliveries_penalty_area_ta": "2.7",
      "att_dribble_penalty_area": "13",
      "att_dribble_penalty_area_ta": "9",
      "att_goals_scored": "9",
      "att_offsides": "17",
      "att_offsides_ta": "7.1",
      "att_shots_blocked": "3",
      "att_shots_saved": "17",
      "attempts_off_target": "28",
      "attempts_on_target": "30",
      "continent": "Europe",
      "country_code": "GRE",
      "country_name": "Greece",
      "def_attempted_clearances": "54",
      "def_attempted_clearances_ta": "41.5",
      "def_blocks": "11",
      "def_completed_clearances": "42",
      "def_completed_clearances_ta": "34.6",
      "def_offsides_given": "4",
      "def_offsides_given_ta": "7.1",
      "def_recovered_balls": "149",
      "def_recovered_balls_ta": "132",
      "def_saves": "11",
      "def_saves_ta": "11",
      "def_tackles": "84",
      "def_tackles_lost": "56",
      "def_tackles_lost_ta": "35.3",
      "def_tackles_tol": "84",
      "def_tackles_tol_ta": "55.5",
      "def_tackles_won": "26",
      "def_tackles_won_ta": "14.7",
      "def_total_defense": "109",
      "distance_covered": "436.7",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/greece.png",
      "goals_scored": "3",
      "id": 20,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Greece&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "matches_played": "4",
      "one_g_freq_attempts": "19.3",
      "one_g_freq_min": "130",
      "open_play_goals": "2",
      "pass_crosses": "118",
      "pass_crosses_ta": "60.6",
      "pass_long_passes_complete": "192",
      "pass_medium_passes_complete": "786",
      "pass_short_passes_complete": "310",
      "pass_ta": "1250",
      "pass_throw_ins": "101",
      "pass_throw_ins_ta": "103",
      "pass_total": "1288",
      "rank": 12,
      "resource_uri": "/api/countries/Greece/",
      "scoring_method_total": "3",
      "set_piece_goals": "1",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/greece.jpg",
      "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/gre.gif",
      "team_video_url": "//www.youtube.com/embed/C-PRYMOvpSA",
      "tournament_average": "42.2"
    }] 

        for obj in response_objects:
            for key in obj:
                if type(obj[key]) == list:
                    obj[key] = sorted(obj[key])

        for obj in expected_response:
            for key in obj:
                if type(obj[key]) == list:
                    obj[key] = sorted(obj[key])


        for obj in response_objects:
            self.assertTrue(obj in expected_response)

    def test_get_country(self) :
        self.maxDiff = None
        expected_response ={
  "article": " After a so-so South Africa 2010 and a poor 2013 CAF Africa Cup of Nations, Algeria missed very few beats on their way to Brazil 2014. They won five of their six group matches to easily top what might have been a tricky section over Mali, Benin and Rwanda. Once in the final play-off round, they were unlucky to draw one of the continents form teams in Burkina Faso, who shocked Africa by finishing second at the 2013 AFCON. In that tie, they lost the first leg 3-2 to a late penalty, but just claimed the place in Brazil with a professional 1-0 win at home that gave them the advantage on away goals. Algeria have played in a total of three FIFA World Cup finals. They got off to the best possible start at the 1982 edition in Spain, beating West Germany 2-1 in their opening game. Despite a 3-2 victory over Chile in their final group game, an earlier 2-0 loss to Austria meant that while level on points with the latter, they were eliminated on goal difference. Mexico 1986 was less memorable for the north African side. Drawn in Group D with Brazil, Spain and Northern Ireland, two defeats and a draw left them bottom of the table and on the first flight home. Nor were things much better at South Africa 2010. Pitted against England, USA and Slovenia, they lost twice and drew their other fixture, departing the competition without a goal to their name. Madjid Bougherra is a key figure at the back, and he scored the all-important winner in the second leg against Burkina Faso. Sofiane Feghouli is an exciting attacking midfielder, while Medhi Lacen holds things down in front of the defence. Islam Slimani emerged as the most prolific option in attack during qualifying.  Vahid HalilhodzicFIFA World Cup Spain 1982, Mexico 1986, South Africa 2010 (Group stages)Lakhdar Belloumi, Rachid Mekhloufi, Mustapha Zitouni",
  "att_attempts": "37",
  "att_crosses": "67",
  "att_crosses_completed": "13",
  "att_crosses_completed_ta": "14.9",
  "att_crosses_ta": "64.2",
  "att_deliveries_penalty_area": "4",
  "att_deliveries_penalty_area_ta": "2.7",
  "att_dribble_penalty_area": "9",
  "att_dribble_penalty_area_ta": "9.3",
  "att_goals_scored": "7",
  "att_offsides": "7",
  "att_offsides_ta": "7.5",
  "att_shots_blocked": "5",
  "att_shots_saved": "10",
  "attempts_off_target": "15",
  "attempts_on_target": "22",
  "continent": "Africa",
  "country_code": "ALG",
  "country_name": "Algeria",
  "def_attempted_clearances": "82",
  "def_attempted_clearances_ta": "44.3",
  "def_blocks": "15",
  "def_completed_clearances": "69",
  "def_completed_clearances_ta": "37",
  "def_offsides_given": "11",
  "def_offsides_given_ta": "7.5",
  "def_recovered_balls": "183",
  "def_recovered_balls_ta": "139",
  "def_saves": "23",
  "def_saves_ta": "11.7",
  "def_tackles": "97",
  "def_tackles_lost": "58",
  "def_tackles_lost_ta": "37.1",
  "def_tackles_tol": "97",
  "def_tackles_tol_ta": "58.5",
  "def_tackles_won": "22",
  "def_tackles_won_ta": "15.9",
  "def_total_defense": "135",
  "distance_covered": "462.0",
  "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/algeria.png",
  "goals_scored": "7",
  "id": 25,
  "map_url": "https://www.google.com/maps/embed/v1/place?q=Algeria&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
  "matches_played": "4",
  "one_g_freq_attempts": "5.3",
  "one_g_freq_min": "56",
  "open_play_goals": "4",
  "pass_crosses": "67",
  "pass_crosses_ta": "64.2",
  "pass_long_passes_complete": "143",
  "pass_medium_passes_complete": "719",
  "pass_short_passes_complete": "332",
  "pass_ta": "1305",
  "pass_throw_ins": "146",
  "pass_throw_ins_ta": "107",
  "pass_total": "1194",
  "rank": 22,
  "resource_uri": "/api/countries/Algeria/",
  "scoring_method_total": "7",
  "set_piece_goals": "3",
  "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/algeria.jpg",
  "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/alg.gif",
  "team_video_url": "//www.youtube.com/embed/Yp41xOAY0EE",
  "tournament_average": "44.1"
}

        request = Request(self.url+"api/countries/algeria/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        
        for key in response_data:
            if type(response_data[key]) == list:
                response_data[key] = sorted(response_data[key])

        self.assertEqual(expected_response, response_data)
     

   # Players

    def test_get_all_players(self) :
        request = Request(self.url+"api/players/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        response_objects = response_data["objects"]
        expected_response = [    {
      "biography": "Sejad Salihovic, a multifunctional midfielder and set-piece specialist, has ample experience in the prestigious waters of the German Bundesliga and for Bosnia-Herzegovina.  Salihovic’s family emigrated to Berlin just before the outbreak of the Bosnian War, when he was seven, and he joined Hertha Berlin’s youth ranks as a teenager. The then-forward made his German top flight debut in 2004 but struggled for playing time at Hertha and joined Hoffenheim in 2006.  Converted into a midfielder, Salihovic played a fundamental role in the club’s leap from the third to the first tier of German football. His mix of defensive and offensive play even helped Hoffenheim lead the 2008/09 Bundesliga at its halfway stage, but an injury to his compatriot Vedad Ibisevic was chiefly behind them stumbling home in seventh.  Salihovic performed consistently over the following seasons and augmented his status at Hoffenheim on the final day of 2012/13. Requiring victory away to UEFA Champions League finalists Borussia Dortmund to go into a relegation play-off rather than suffer automatic relegation, Salihovic converted two late penalties – both masterfully curled high into the net – to grab Hoffenheim a come-from-behind 2-1 victory. The Sinsheim outfit then beat Kaiserslautern home and away to retain their top-flight status.  Salihovic, who has been sporadically used at left-back, has been a regular in the Bosnia-Herzegovina squad since 2007. ",
      "birth_date": "1984-10-08",
      "clubname": "TSG 1899 Hoffenheim",
      "first_international_appearance": "Greece - Bosnia and Herzegovina 13 Oct 2007",
      "full_name": "Sejad Salihovic",
      "goals": 4,
      "height": 182,
      "id": 1,
      "international_caps": 44,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/BosniaandHerzegovina/Sejad_SALIHOVIC.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Sejad%20Salihovic/",
      "shirt_number": 23,
      "sur_name": "Salihovic",
      "twitter_name": "salihovic2323"
    },
    {
      "biography": "Asamoah Gyan's name will forever be linked with his missed penalty in the South Africa 2010 quarter-finals. The miscue in the last minute of extra-time, in their famous clash against Uruguay, denied the Black Stars a semi-final place as they went on to lose the match via a shootout. Gyan also missed a penalty against Zambia in the last four at the CAF Africa Cup of Nations 2012, and he announced afterwards that he would be taking an indefinite break from international football. However, luckily for the Black Stars, his absence lasted just a few months and he was named as captain upon his return to the fold.\\r\\nGyan, who played his first game for Ghana as a 17-year-old and scored on his debut, plies his club trade in the United Arab Emirates, having joined Al Ain after stints in Europe with Italian clubs Udinese and Modena, French outfit Rennes and Sunderland of the English Premier League. Now 28, Gyan combines searing pace with a deadly touch in the penalty area. A powerful athlete, he has a blistering shot, the upper body strength to hassle defenders and a good spring to combat effectively in the air as well. ",
      "birth_date": "1985-11-22",
      "clubname": "Al Ain FC",
      "first_international_appearance": "Ghana - Somalia 19 Nov 2003",
      "full_name": "Asamoah Gyan",
      "goals": 41,
      "height": 180,
      "id": 2,
      "international_caps": 81,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Ghana/Asamoah_GYAN.png",
      "position": "Forward",
      "resource_uri": "/api/players/Asamoah%20Gyan/",
      "shirt_number": 3,
      "sur_name": "Gyan",
      "twitter_name": "ASAMOAH_GYAN3"
    },
    {
      "biography": "Never one to take his foot off the pedal, Lucas Digne spends the full 90 minutes of every game putting in maximum effort. \"When you play on the wing, you can\\'t allow yourself the slightest easing-off and you constantly have to work hard,\" the left-back told  during the FIFA U-20 World Cup Turkey 2013, which ended with France lifting the trophy. \"My first priority is to defend well, but I also have to do everything I can to help out offensively. That\\'s the job of a modern full-back. The coach gives you instructions, but there\\'s also an element of intuition, knowing when you can get forward and when to hold back so as not to unbalance the team.\"\\r\\nDigne first began learning the nuances of his role with Lille, where he made his Ligue 1 debut in 2011 before signing for Paris Saint-Germain in the summer of 2013. Despite stiff competition from Maxwell at the Parc des Princes, the youngster – who will turn 21 in July – earned promotion to the France side in February this year, when he came on for Patrice Evra against the Netherlands. A fan of Philipp Lahm, he derives much of his ambition to succeed from the example of his older brother, a former Lille youth academy member who had to quit the game after injury. \"He had a lot of quality, but he got injured and couldn\\'t regain his previous level and never got the chance to break into the professional squad,\" said Digne. \"I know that he\\'s now living his dream through me, and that gives me the strength to never admit defeat.\" ",
      "birth_date": "1993-07-20",
      "clubname": "Paris Saint-Germain FC",
      "first_international_appearance": "France - Netherlands 05 Mar 2014",
      "full_name": "Lucas Digne",
      "goals": 0,
      "height": 189,
      "id": 3,
      "international_caps": 3,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/France/Lucas_DIGNE.png",
      "position": "Defender",
      "resource_uri": "/api/players/Lucas%20Digne/",
      "shirt_number": 17,
      "sur_name": "Digne",
      "twitter_name": "LDigne"
    },
    {
      "biography": "Few Mexican players have achieved as much at international level as Giovani dos Santos. The talented playmaker won the FIFA U-17 World Cup in 2005, picked up a gold medal at the Men's Olympic Football Tournament London 2012, and was voted the third-best young player at the 2010 FIFA World Cup South Africa™ - all by the age of 24. Yet, for all his success with , dos Santos has struggled to show his best form on a consistent basis at club level. A product of the famous youth set-up at Barcelona,  spent just one year in 's first team before moving to England to join Tottenham Hotspur.    Playing opportunities in north London proved scarce, however, and his four years as a Tottenham player included loan spells at Ipswich Town, Galatasaray and Racing Santander. Those stints away from White Hart Lane did, at least, allow him to showcase his talents, and reinforced his need to find regular first-team football. His move to Mallorca the start of 2012/13 promised that much-needed stability, and he has duly become an important figure for the team. However, with the Balearic club seemingly destined for relegation from the Spanish top flight – despite their new recruit's best efforts – Dos Santos could soon be on the hunt for new employers once again.  With his combination of power, skill and grace, Dos Santos is one player sure to delight the crowds at Brazil 2014. ",
      "birth_date": "1989-05-11",
      "clubname": "Villarreal CF",
      "first_international_appearance": "Brazil - Mexico 12 Sep 2007",
      "full_name": "Giovani Dos Santos",
      "goals": 16,
      "height": 179,
      "id": 4,
      "international_caps": 78,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Mexico/Giovani_DOS_SANTOS.png",
      "position": "Forward",
      "resource_uri": "/api/players/Giovani%20Dos%20Santos/",
      "shirt_number": 10,
      "sur_name": "Dos Santos Ramirez",
      "twitter_name": "OficialGio"
    },
    {
      "biography": "  There were 18 minutes remaining of Brazil’s Round-of-16 match against Chile at the 2010 FIFA World Cup South Africa™ when Ramires went into the book for a typically committed challenge.  With his side leading 3-0 at the time, the player was unconcerned about picking up a caution. All that mattered was making sure his team held on to their lead, even if it meant him missing Brazil’s next match, a quarter-final against the Netherlands. Years later, in an interview with , Ramires reflected on that match: “I came off the pitch a happy man after the game against Chile. I played well and set up a goal too. It was my first start in a World Cup match and I never thought at the time it would be my last.” After sitting out  2-1 loss to the Dutch through suspension, Ramires is ready to return to the big stage and set the record straight. Now a well established figure at Chelsea, the pacy, committed and versatile midfielder has been a first choice for every coach that has taken up residence in the Blues dugout in the last four years. Discussing his adaptability in that same interview, he said: “I always try and pay attention to my surroundings when I arrive somewhere and find my feet as quickly as possible. I think I’ve been lucky up to now because I’ve come across a lot of people who’ve made me feel comfortable, though it’s not just down to that. I think I’ve managed to make the most of it.” As he belatedly resumes his World Cup career, the hard-running Ramires should have no problems at all in finding his bearings at Brazil 2014.      ",
      "birth_date": "1987-03-24",
      "clubname": "Chelsea FC",
      "first_international_appearance": "Uruguay - Brazil 06 Jun 2009",
      "full_name": "Ramires",
      "goals": 4,
      "height": 181,
      "id": 5,
      "international_caps": 49,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Brazil/RAMIRES.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Ramires/",
      "shirt_number": 16,
      "sur_name": "Santos Do Nascimento",
      "twitter_name": "Rami7oficial"
    },
    {
      "biography": "Jinking dribbles and lightning runs down the right wing have been a hallmark of Alexander Samedov since he was a youngster coming through the ranks at Spartak Moscow, earning him call-ups to the national team. However, the talented midfielder needed time to mature. A string of transfers also hindered his progress. Samedov moved to Lokomotiv Moscow, but did not stick around for long, moving again to Moscow FC, where he enjoyed his first great seasons. But it was after moving again, to city rivals Dynamo that the goals and the assists really began to flow, paving the way for his international debut. And while that long-awaited maiden appearance eventually came in October 2011, it was not in time for the then 27-year-old to make the cut for UEFA EURO 2012. Under Fabio Capello, however, he has become an important member of the national team, playing in eight qualifying games and scoring in both matches against Luxembourg. Samedov has shown excellent recent form too, ending 2013 by scoring in the 1-1 draw with Serbia, and starting 2014 with a decisive contribution in the victory over Armenia. Moreover, he played a leading role in Lokomotiv Moscow’s excellent campaign in the Russian Championship. It has taken him a long time, but on cusp of turning 30, Samedov has shown he still has the talent and speed to create headaches for the opposition. ",
      "birth_date": "1984-07-19",
      "clubname": "FC Lokomotiv Moscow",
      "first_international_appearance": "Slovakia - Russia 07 Oct 2011",
      "full_name": "Alexander Samedov",
      "goals": 3,
      "height": 178,
      "id": 6,
      "international_caps": 20,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Russia/Alexander_SAMEDOV.png",
      "position": "Forward",
      "resource_uri": "/api/players/Alexander%20Samedov/",
      "shirt_number": 19,
      "sur_name": "Samedov",
      "twitter_name": ""
    },
    {
      "biography": "At just 21 years of age, Ricardo Rodriguez has already established himself as first-choice left back both at Bundesliga club Wolfsburg and in the Swiss national team.\\r\\nWhile his exceptional technique and unbending fighting spirit have been key to his rapid ascent, Rodriguez’s attacking prowess and pinpoint crosses have been equally important.\\r\\nBorn to Spanish-Chilean parents, Rodriguez rose through the ranks in the FC Zurich youth academy but signed a four-and-a-half year deal with Wolfsburg after just two years as a professional.\\r\\nThe defender has yet to appear at a major international tournament at senior level, but was part of the triumphant Swiss side that lifted the FIFA U-17 World Cup title in Nigeria in 2009. Rodriguez, famed as much for the accuracy of his left-foot as for his ponytail, earned his first full cap on 7 October 2011 in a European Championship qualifier against Wales.\\r\\nThe 1.80 metre tall defender was an essential part of Switzerland’s 2014 FIFA World Cup Brazil™ qualifying campaign and played in every fixture bar the final match against Slovenia. Winning silverware in South America may be asking too much of the national side at this stage, but it would be unwise to write them off too soon if, as expected, they reach the knockout rounds. ",
      "birth_date": "1992-08-25",
      "clubname": "VfL Wolfsburg",
      "first_international_appearance": "Wales - Switzerland 07 Oct 2011",
      "full_name": "Ricardo Rodriguez",
      "goals": 0,
      "height": 180,
      "id": 7,
      "international_caps": 25,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Switzerland/Ricardo_RODRIGUEZ.png",
      "position": "Defender",
      "resource_uri": "/api/players/Ricardo%20Rodriguez/",
      "shirt_number": 13,
      "sur_name": "Rodriguez Araya",
      "twitter_name": "RRWWE"
    },
    {
      "biography": "One of several exciting prospects to have emerged from the Feyenoord youth system, Stefan de Vrij plays with an authority and composure that belie his tender years.  Though still just 22, he is firmly established as the Rotterdam outfit’s captain, having assumed the armband at the age of 20 when Ron Vlaar departed for Aston Villa. That honour reflects the maturity with which the centre-half conducts himself on and off the field, and the respect that he already commands from team-mates for both club and country.  Such esteem has been earned by consistently assured performances that have helped restore Feyenoord as a force to be reckoned with in the Eredivisie and established their young skipper as a recognised international.  De Vrij just missed out on UEFA EURO 2012, his name one of those cut from the provisional 36-man squad, but he has gone on to make nine appearances under Louis van Gaal since making his debut two years ago. The Netherlands coach clearly sees this classy defender as a future stalwart, and there will be plenty of big clubs watching with interest how he performs at Brazil 2014.  ",
      "birth_date": "1992-02-05",
      "clubname": "Feyenoord Rotterdam",
      "first_international_appearance": "Belgium - Netherlands 15 Aug 2012",
      "full_name": "Stefan De Vrij",
      "goals": 1,
      "height": 190,
      "id": 8,
      "international_caps": 19,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Netherlands/Stefan_DE_VRIJ.png",
      "position": "Defender",
      "resource_uri": "/api/players/Stefan%20De%20Vrij/",
      "shirt_number": 3,
      "sur_name": "De Vrij",
      "twitter_name": "Stefandevrij"
    },
    {
      "biography": "Few Mexican players have made their mark on the nation’s football scene as swiftly as Hector Herrera has done. In just four years he has gone from plying his trade in the second division to becoming one of the country's most talked-about stars. \\r\\nWatching him in action, it immediately becomes clear why he has people talking. Herrera is one of the most dynamic central midfielders Mexico has produced in a long time. Tactically disciplined, at ease in possession, intelligent and a tireless worker, Herrera's stock rose after being named the best player at the prestigious 2012 Toulon Tournament. He later consolidated his impressive displays with the Mexico side that took gold at the same year's Men's Olympic Football Tournament.  \\r\\nSince then, he played in the FIFA Confederations Cup Brazil 2013 and transferred to Portuguese giants Porto, where he has been a starter for most of the season. He is sure to be an integral part of Mexico in Brazil 2014 either as a pure holding midfielder, or as a box-to-box player where he is able to demonstrate his talent and versatility. ",
      "birth_date": "1990-04-19",
      "clubname": "FC Porto",
      "first_international_appearance": "Mexico - El Salvador 16 Oct 2012",
      "full_name": "Hector Herrera",
      "goals": 0,
      "height": 180,
      "id": 9,
      "international_caps": 17,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Mexico/Hector_HERRERA.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Hector%20Herrera/",
      "shirt_number": 6,
      "sur_name": "Herrera Lopez",
      "twitter_name": ""
    },
    {
      "biography": "Stephen Adams isn’t as tall as most goalkeepers, but he more than makes up for it with his agility. One of just a handful of domestic-based Black Stars called up for FIFA World Cup duty, Adams earned his place in the squad for Brazil 2014 with brilliant performances during the CAF African Nations Championship in 2014, in which he conceded just one goal in six matches en route to a second-placed finish. Nigeria coach Stephen Keshi admitted to being an admirer of Adams after Ghana beat his side in the semis. “He’s an outstanding goalkeeper and he’s done a wonderful job in the tournament,” Keshi told .\\r\\nAdams was named Ghana's top domestic-based goalkeeper in 2010, when his club Aduana Stars won the league championship. He has since been linked with a move to greener pastures in South Africa. Adams is capable of pulling off breathtaking saves from close range, amply making up for his smaller frame. It’s precisely this quality that Ghana coach Kwesi Appiah recognised in Adams as he penned the keeper’s name on his squad list for Brazil, four years after the disappointment of being one of the last dropped for South Africa 2010. ",
      "birth_date": "1989-09-28",
      "clubname": "Aduana Stars",
      "first_international_appearance": "Ghana - Congo 13 Jan 2014",
      "full_name": "Stephen Adams",
      "goals": 0,
      "height": 186,
      "id": 10,
      "international_caps": 6,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Ghana/Stephen_ADAMS.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Stephen%20Adams/",
      "shirt_number": 1,
      "sur_name": "Adams",
      "twitter_name": "RealStevenAdams"
    },
    {
      "biography": "The left-sided Zhirkov learned his trade with hometown club Spartak Tambov before leaving at the age of 18 for CSKA Moscow. Slotting in at left-back he won the 2005 UEFA Cup with the team from the capital, as well as two Russian Premier League titles, four Russian Cups and another four Russian Super Cups. More winner’s medals would come Zhirkov’s way following a move to Chelsea in 2009, with his new employers securing an English league and cup double the following year. In 2011 he was on his way back to Russia, this time to Anzhi Makhachkala, staying there for two years before joining current club Dinamo Moscow. Though a world finals novice, Zhirkov boasts an impressive CV with Russia, having earned more than 50 caps while performing as both full-back and winger on the left flank. In helping Russia finish third at UEFA EURO 2008, he was named in the Team of the Tournament, his performances in Austria and Switzerland also earning him the nod as Russian Footballer of the Year.  ",
      "birth_date": "1983-08-20",
      "clubname": "FC Dynamo Moscow",
      "first_international_appearance": "Italy - Russia 09 Feb 2005",
      "full_name": "Yury Zhirkov",
      "goals": 1,
      "height": 180,
      "id": 11,
      "international_caps": 62,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Russia/Yury_ZHIRKOV.png",
      "position": "Forward",
      "resource_uri": "/api/players/Yury%20Zhirkov/",
      "shirt_number": 18,
      "sur_name": "Zhirkov",
      "twitter_name": "YuriZhirkov1"
    },
    {
      "biography": "A quick threat down the flank, Samuel Inkoom has made a successful transition from Ghana\\'s U-20 team to the senior side. He was among the players who successfully converted a penalty in a shootout against Brazil in the final in Cairo, ensuring Ghana became the first African side to win the FIFA U-20 World Cup. His performances were such that he made the Black Stars squad for the FIFA World Cup™ the following year, and he has been a regular in the squad ever since. Inkoom, who turns 25 at the start of June, hails from the coastal town of Sekondi, where he began his club career at Sekondi Hasaacas. His potential and athletic ability saw him move to Asante Kotoko at the start of 2008 after only just a few months with Sekondi. By the end of the year he\\'d won his first international cap in a friendly against Tunisia and, in 2009, Inkoom was on the move again. He headed to Switzerland, where he signed for FC Basel before moving, once more, to Ukrainian outfit Dnipro Dnipropetrovsk. Two loan periods at French side Bastia and Greek outfit Platanias followed, with the defender eventually signing a permanent contract deal with the latter.",
      "birth_date": "1989-06-01",
      "clubname": "FC Platanias",
      "first_international_appearance": "Ghana - Tunisia 19 Nov 2008",
      "full_name": "Samuel Inkoom",
      "goals": 1,
      "height": 179,
      "id": 12,
      "international_caps": 46,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Ghana/Samuel_INKOOM.png",
      "position": "Defender",
      "resource_uri": "/api/players/Samuel%20Inkoom/",
      "shirt_number": 2,
      "sur_name": "Inkoom",
      "twitter_name": "InkoomSamuel"
    },
    {
      "biography": "A product of the much-admired youth system at FC Barcelona, Cesc Fabregas chose to leave at just 16 to try his luck with English giants Arsenal. Soon becoming the club’s youngest debutant and goalscorer, by the age of 21 the central midfielder was the Gunners’ captain and went on to play a total of eight seasons under Arsene Wenger – racking up 303 matches and 57 goals.  Victory in just one Community Shield and one FA Cup in his time at Arsenal were not enough to quench his thirst for silverware, however, and in 2011 Fabregas returned ‘home’ to Camp Nou – where he gelled immediately and in spectacular style with Lionel Messi and Co. Indeed, in his first season with he won the Spanish Super Cup, the UEFA Super Cup, the FIFA Club World Cup and the Copa del Rey. Playing in a slightly more advanced role than in his spell in England, even sometimes being used up front as a ‘false nine’, Fabregas continues to be a regular source of goals and assists for the Catalan club. \\r\\n",
      "birth_date": "1987-05-04",
      "clubname": "FC Barcelona",
      "first_international_appearance": "Spain - Ivory Coast 01 Mar 2006",
      "full_name": "Cesc Fabregas",
      "goals": 13,
      "height": 175,
      "id": 13,
      "international_caps": 91,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Spain/Cesc_FABREGAS.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Cesc%20Fabregas/",
      "shirt_number": 10,
      "sur_name": "Fabregas Soler",
      "twitter_name": "cesc4official"
    },
    {
      "biography": "Pint-sized midfielder Marvin Chavez may not be the tallest of players, but he more than makes up for his diminutive stature with explosive pace and a muscular frame. Indeed, those qualities allow the versatile La Ceiba native to play in central midfield or on the wing and have also helped him be part of two FIFA World Cup™ qualifying campaigns.\\r\\nThe 30-year-old, nicknamed (‘Son of the wind’) due to his speed, made his professional debut at Vida in 2005 and was called up to the national team to face Venezuela in a friendly after only a year at the club.\\r\\nIn total he spent three years at Vida and a further two at Marathon before moving to the USA in 2011. In the MLS he represented Dallas and San Jose Earthquakes prior to joining Colorado Rapids in 2014.\\r\\nGiven the fierce competition for places in the Honduran midfield, with veterans and hugely promising youngsters all jostling for a spot in the side, Chavez only played 177 minutes in Honduras’ Brazil 2014 qualifying campaign but still managed to score once. Nevertheless, national team coach Luis Fernando Suarez is an admirer of his talents and will be counting on him as a viable attacking alternative. ",
      "birth_date": "1983-11-03",
      "clubname": "CD Chivas USA",
      "first_international_appearance": "China PR - Honduras 12 Feb 2006",
      "full_name": "Marvin Chavez",
      "goals": 4,
      "height": 165,
      "id": 14,
      "international_caps": 44,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Honduras/Marvin_CHAVEZ.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Marvin%20Chavez/",
      "shirt_number": 23,
      "sur_name": "Chavez",
      "twitter_name": "marvinchavez18"
    },
    {
      "biography": "Chris Smalling made his Premier League debut as a Fulham substitute in the final fixture of the 2008/09 season against Everton at Craven Cottage at the age of 19.  The following season he helped the Cottagers to the final of the UEFA Europa League and attracted the attentions of Manchester United who signed him in the summer of 2010. At Old Trafford, he has won two Premier League titles and three FA Community Shields. Although primarily a central defender, he can also play as a right-back.  Smalling has represented England at various levels and is currently a member of the England senior squad. He played for the England Schools Under-18 team in early 2008 before making his debut for the U-20 side and the U-21 side in 2009. He made his debut for the England senior squad in the 3–0 win over Bulgaria on 2 September 2011.  He was also named in the UEFA European U-21 Championship’s Team of the Tournament following his displays in Denmark.  ",
      "birth_date": "1989-11-22",
      "clubname": "Manchester United FC",
      "first_international_appearance": "Bulgaria - England 02 Sep 2011",
      "full_name": "Chris Smalling",
      "goals": 0,
      "height": 194,
      "id": 15,
      "international_caps": 13,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/England/Chris_SMALLING.png",
      "position": "Defender",
      "resource_uri": "/api/players/Chris%20Smalling/",
      "shirt_number": 12,
      "sur_name": "Smalling",
      "twitter_name": "ChrisSmalling14"
    },
    {
      "biography": "Gonzalo Jara is a right-back with good technique, but it’s his versatility that makes him an even more valuable member of Chile’s squad, given that he can also operate on the left, as a centre-back or as a defensive midfielder. A bright future was on the cards for Jara ever since he captained Chile at the 2005 U-20 South American championship in Colombia. That year also saw the full-back further showcase his potential as he played in the U-20 World Cup in Netherlands and was also chosen as the best player at Huachipato, the club where he had arrived just two years earlier as a youth player. 2006 brought a new achievement as Nelson Acosta gave Jara his debut for Chile at just 20 years of age. The following year, he then moved to a big club, Colo-Colo, and went on to win three national titles before establishing himself as a regular under Marcelo Bielsa for Chile in 2009 and securing a transfer to West Bromwich Albion. A starter at the FIFA World Cup South Africa 2010, Jara was suspended for indiscipline in 2011 and subsequently missed ten games. He apologised, however, and returned to play in eight qualifiers en route to Brazil 2014, where he’ll hope to build on his successful season this term with Nottingham Forest.  ",
      "birth_date": "1985-08-29",
      "clubname": "Nottingham Forest FC",
      "first_international_appearance": "Chile - New Zealand 25 Apr 2006",
      "full_name": "Gonzalo Jara",
      "goals": 3,
      "height": 177,
      "id": 16,
      "international_caps": 69,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Chile/Gonzalo_JARA.png",
      "position": "Defender",
      "resource_uri": "/api/players/Gonzalo%20Jara/",
      "shirt_number": 18,
      "sur_name": "Jara Reyes",
      "twitter_name": "Gonzalo_Jara"
    },
    {
      "biography": "Matt Besler is a no-nonsense defender doing the quiet work for club and country at every opportunity.  The MLS veteran is strong in the tackle, but even better at reading the game and making sure he is in the right place at the right time. Besler was thrown in to the deep end by Jurgen Klinsmann, getting his first national team cap in Mexico City against the United States’ arch-rival to the south, and the defender, to his credit, was spot-on in doing his part to secure a goalless draw on the day. The consistency that might have surprised some USA supporters would have in no way taken Sporting Kansas City supporters unawares. Besler is the defensive rock for a club that prides itself on winning every ball and harrying the opposition into costly mistakes. It was just this kind of assurance in the centre of defence that helped SKC to last year’s MLS league title.  Besler’s only real competitive tournament experience for the Stars and Stripes came last summer when he was called in to take part in Jurgen Klinsmann’s experimental side for the 2013 CONCACAF Gold Cup. His performance en route to the trophy in that tournament, among unfamiliar teammates, testified to the calm he imparts on a football pitch.  ",
      "birth_date": "1987-02-11",
      "clubname": "Sporting Kansas City",
      "first_international_appearance": "USA - Canada 29 Jan 2013",
      "full_name": "Matt Besler",
      "goals": 0,
      "height": 182,
      "id": 17,
      "international_caps": 21,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/USA/Matt_BESLER.png",
      "position": "Defender",
      "resource_uri": "/api/players/Matt%20Besler/",
      "shirt_number": 5,
      "sur_name": "Besler",
      "twitter_name": ""
    },
    {
      "biography": "A physically imposing centre-back with good technique and a strong personality, Sebastian Coates was a key figure for Uruguayan giants Nacional by the age of just 19. A product of 's youth system, Coates had yet to make his first-team debut when, in 2009, he shone for the national youth side that qualified for the FIFA U-20 World Cup in Egypt. He made his professional club debut that same year and enjoyed a successful first campaign, winning the Uruguayan championship and reaching the semi-finals of the Copa Libertadores. After the FIFA U-20 World Cup in 2009, Coates decided against a move to Europe and instead stayed at Nacional, where he soon picked up another league title.  (The Boss), as he is known, capped 2009 with a call-up to Oscar Tabarez's Uruguay squad for the play-off against Costa Rica for a place at the 2010 FIFA World Cup South Africa™. He was not used in that game, though, and did not make s squad for South Africa 2010. The young defender continued to impress, however, and was eventually given his senior international debut by Tabarez in a friendly ahead of the 2011 Copa America. He then started the continental competition on the bench, but finished as a regular part of the starting line-up that won the championship. Coates has found his opportunities limited at Liverpool since moving to England, and has so far only featured in two qualifiers for Brazil 2014. He did, however, play in all three of Uruguay's games at the Men's Olympic Football Tournament London 2012, and remains a regular member of Tabarez's senior squad despite picking up some injuries.    ",
      "birth_date": "1990-10-07",
      "clubname": "Club Nacional de Football",
      "first_international_appearance": "Uruguay - Estonia 23 Jun 2011",
      "full_name": "Sebastian Coates",
      "goals": 0,
      "height": 196,
      "id": 18,
      "international_caps": 16,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Uruguay/Sebastian_COATES.png",
      "position": "Defender",
      "resource_uri": "/api/players/Sebastian%20Coates/",
      "shirt_number": 19,
      "sur_name": "Coates Nion",
      "twitter_name": "SebastianCoates"
    },
    {
      "biography": "Patrice Evra boasts the relentless energy of a dynamo. Watch the Manchester United and France full-back in action and what stands out is the sheer distance he covers down the left, both frustrating opposition attacks and lending a hand during his own team's forays forward. Since his days as a youth player in and around Paris, Evra has forged the mentality of a warrior and racked up an impressive level of experience, having first moved abroad to join third-tier Italian side Marsala aged just 17. Quickly spotted by Monza, he climbed up a division, only to return to France a season later to sign for Nice.  \\r\\nIt was with Nice's local rivals Monaco that Evra really began turning heads, however, playing a full part as the principality side finished runners-up in the UEFA Champions League under Didier Deschamps in 2003/04. From there, the defender set sail for Manchester, since when he has amassed a formidable list of honours, including wins in the Champions League and FIFA Club World Cup. Voted best left-back in the Premier League in 2007, 2009 and 2010, he was likewise singled out as the top player in his position in the 2009 FIFA/FIFPro World XI.\\r\\nFor France, his opportunities were initially limited by Eric Abidal, yet Evra finally made the left-back spot his own after the 2006 FIFA World Cup™. UEFA EURO 2008 proved a low point, but worse was to come at South Africa 2010, where Evra captained a side that disappointed supporters both on and off the pitch. Eager to shine on African soil, the native of Dakar, Senegal, was left heartbroken by that experience. He also served an extended period out of the team through suspension, but has forced his way back in thanks to his consistent displays for the Red Devils. ",
      "birth_date": "1981-05-15",
      "clubname": "Manchester United FC",
      "first_international_appearance": "France - Bosnia and Herzegovina 18 Aug 2004",
      "full_name": "Patrice Evra",
      "goals": 0,
      "height": 174,
      "id": 19,
      "international_caps": 62,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/France/Patrice_EVRA.png",
      "position": "Defender",
      "resource_uri": "/api/players/Patrice%20Evra/",
      "shirt_number": 3,
      "sur_name": "Evra",
      "twitter_name": ""
    },
    {
      "biography": "Having represented his birth nation of Germany at the youth level, Jermaine Jones made the switch to USA – the country of his father’s birth – in 2010. A combative and occasionally ill-tempered holding midfielder, he has given the Americans a little extra grit and endeavor since his arrival. He has also brought with him the indispensible lessons learned over years playing at the highest levels of the club game in Europe \\r\\nAfter coming up through the Eintracht Frankfurt system and a later spell with Bayer Leverkusen, Jones played the lion’s share of his club career with Schalke 04. There he won the German DFB-Pokal during the 2010/11 season and represented the club on Europe’s biggest stage, the UEFA Champions League, on more than one occasion. His gut-busting runs from one penalty area to the other have added a layer of dynamism to the US attack and defence, as have his clear and sometimes abrasive leadership qualities. \\r\\n“This is a team full of guys who like to get dirty, to work so hard. When one of us trips up, the other guy is right there to jump in and dig him out. This is what makes us strong,” Jones told  about the USA side where he’s fitting right in under childhood idol and countryman Jurgen Klinsmann.  ",
      "birth_date": "1981-11-03",
      "clubname": "Besiktas JK",
      "first_international_appearance": "USA - Poland 09 Oct 2010",
      "full_name": "Jermaine Jones",
      "goals": 3,
      "height": 184,
      "id": 20,
      "international_caps": 48,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/USA/Jermaine_JONES.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Jermaine%20Jones/",
      "shirt_number": 13,
      "sur_name": "Jones",
      "twitter_name": "Jermainejunior"
    }]
        for story in expected_response:
            self.assertTrue(story in response_objects)

    def test_get_player(self) :
        expected_response ={
  "biography": "Though goalkeeping is his trade, one of Camilo Vargas’ most memorable performances came when he scored the winning goal for Santa Fe in a 2011 instalment of their rivalry with Millonarios, the oldest derby in Colombian football. Aside from his goalscoring abilities, the 25-year-old custodian possesses lightning reflexes, is as agile as they come and is something of an expert at saving penalties. \\r\\nVargas’ brothers tried their luck as keepers but were unable to break into professional football. After starting out with Maracaneiros, he showed them how it was done, moving to Bogota side Santa Fe at the age of 16 and making his first division debut there in 2007. An idol at the club, he went on to win a Colombian league, Cup and Super Cup with them.\\r\\nA youth international with Colombia, Vargas has still to make his full international debut, though he has been an ever-present in Jose Pekerman squads since September 2012 and a lucky charm to boot – in the 11 Brazil 2014 World Cup qualifiers  played after the keeper’s first call-up they lost just one. \\r\\nAlthough Vargas goes to Brazil 2014 as Pekerman’s third-choice behind David Ospina and the veteran Faryd Mondragon, the world finals will represent a valuable experience for a keeper whose stock is rising all the time and who has a big future ahead of him. ",
  "birth_date": "1989-03-09",
  "clubname": "Independiente Santa Fe",
  "first_international_appearance": " - ",
  "full_name": "Camilo Vargas",
  "goals": 0,
  "height": 185,
  "id": 127,
  "international_caps": 0,
  "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Colombia/Camilo_VARGAS.png",
  "position": "Goalkeeper",
  "resource_uri": "/api/players/Camilo%20Vargas/",
  "shirt_number": 12,
  "sur_name": "Vargas Gil",
  "twitter_name": "Kmilovargas12"
}

        request = Request(self.url+"api/players/Camilo%20Vargas/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        #print(response_body)
        response_data = loads(response_body)

        self.assertEqual(expected_response, response_data)

        response_body = response.read()



    #Matches

    def test_get_all_matches(self) :
        request = Request(self.url+"api/matches/?offset=0&limit=5")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        response_objects = response_data["objects"]
        expected_response = [
            {
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1876413",
      "location": "Arena de Sao Paulo",
      "map_location": "https://www.google.com/maps/embed/v1/place?q=Arena de Sao Paulo+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "match_date": "2014-06-12",
      "match_num": 1,
      "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bra_cro.jpg",
      "resource_uri": "/api/matches/1/",
      "score": "3-1",
      "winner": "Brazil"
    },
    {
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1878138",
      "location": "Estadio das Dunas",
      "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio das Dunas+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "match_date": "2014-06-13",
      "match_num": 2,
      "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/mex_cmr.jpg",
      "resource_uri": "/api/matches/2/",
      "score": "1-0",
      "winner": "Mexico"
    },
    {
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1878787",
      "location": "Arena Fonte Nova",
      "map_location": "https://www.google.com/maps/embed/v1/place?q=Arena Fonte Nova+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "match_date": "2014-06-13",
      "match_num": 3,
      "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/esp_ned.jpg",
      "resource_uri": "/api/matches/3/",
      "score": "1-5",
      "winner": "Netherlands"
    },
    {
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1879607",
      "location": "Arena Pantanal",
      "map_location": "https://www.google.com/maps/embed/v1/place?q=Arena Pantanal+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "match_date": "2014-06-13",
      "match_num": 4,
      "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/chi_aus.jpg",
      "resource_uri": "/api/matches/4/",
      "score": "3-1",
      "winner": "Chile"
    },
    {
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1880788",
      "location": "Estadio Mineirao",
      "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio Mineirao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "match_date": "2014-06-14",
      "match_num": 5,
      "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/col_gre.jpg",
      "resource_uri": "/api/matches/5/",
      "score": "3-0",
      "winner": "Colombia"
    }
        ]

        for culture in expected_response:
            self.assertTrue(culture in response_objects)

    def test_get_match(self) :
        expected_response = {
          "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1891625 ",
          "location": "Estadio Beira-Rio",
          "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio Beira-Rio+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
          "match_date": "2014-06-18",
          "match_num": 20,
          "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/aus_ned.jpg",
          "resource_uri": "/api/matches/20/",
          "score": "2-3",
          "winner": "Netherlands"
        }
        request = Request(self.url+"api/matches/20/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        self.assertEqual(expected_response, response_data)

#All these API tests and API tests above require one terminal running python manage.py runserver
#before the other one running python manage.py test
class CountryResourceTest(ResourceTestCase):
    url = "http://127.0.0.1:8000/"
    def test_get_api_json(self):
        resp = self.api_client.get(self.url+'api/countries/', format='json')
        self.assertValidJSONResponse(resp)

class PlayerResourceTest(ResourceTestCase):
    url = "http://127.0.0.1:8000/"
    def test_get_api_json(self):
        resp = self.api_client.get(self.url+'api/players/', format='json')
        self.assertValidJSONResponse(resp)

class MatchResourceTest(ResourceTestCase):
    url = "http://127.0.0.1:8000/"
    def test_get_api_json(self):
        resp = self.api_client.get(self.url+'api/matches/', format='json')
        self.assertValidJSONResponse(resp)


#Team Possible - Must Read
#Prerequsite: setup the watson correctly
#Also make sure the mysql support less than 4 letters search
#by changing my.cnf since MySQL server which default  ft_min_word_len = 4
#it utilized MyISAM MySQL engine instead of InnoDB to support fulltext search
class SearchTests(unittest.TestCase):

    def test_search_country(self):
        a = Country.objects.create(country_name="Brazil")
        a.save()
        b = Country.objects.create(country_name="XCountry")
        b.save()
        c = Country.objects.create(country_name="BraBarLa")
        c.save()

        call_command('installwatson', verbosity=0, interactive=False)
        call_command('buildwatson', verbosity=0, interactive=False)
        
        #mini test 1
        query="Bra"
        results = watson.search(query, ranking=True)
        self.assertEqual(len(results), 2)

        #mini test 2
        query="Brazil"
        results = watson.search(query, ranking=True)
        self.assertEqual(len(results), 1)


    def test_search_player(self):
        c_obj = Country.objects.create(country_name="Cameroon")
        c_obj.save()

        a = Player.objects.create(full_name="Eros Smith", country=c_obj, birth_date="2014-5-10")
        a.save()
        b = Player.objects.create(full_name="Jeremiah Ronaldo", biography="His best friend is smitz",country=c_obj, birth_date="2014-5-10")
        b.save()
        c = Player.objects.create(full_name="Lee ChuYoong", country=c_obj, birth_date="2014-5-10")
        c.save()
        d = Player.objects.create(sur_name="Gleen",country=c_obj, birth_date="2014-5-10")
        d.save()

        call_command('installwatson', verbosity=0, interactive=False)
        call_command('buildwatson', verbosity=0, interactive=False)
        
        #mini test 1 for smit 
        #and expect to return eros smith and jeremiah ronaldo
        #also prove it is searchable for multiple fields at the same time
        query="smit"
        results = watson.search(query, ranking=True)
        self.assertEqual(len(results), 2)


        #mini test 2
        #we only setup up for char field or textfield
        #the expected result should be 0 even they are matching
        query="2014-5-10"
        results = watson.search(query, ranking=True)
        self.assertEqual(len(results), 0)


    def test_search_match(self):
        # match_num = models.IntegerField(default=0, primary_key=True)
        # country_A = models.ForeignKey(Country, related_name='country_A')
        # country_B = models.ForeignKey(Country, related_name='country_B')
        # winner = models.CharField(max_length=200)
        # score = models.CharField(max_length=64)
        a_obj = Country.objects.create(country_name="Germany")
        a_obj.save()

        c_obj = Country.objects.create(country_name="Brazil")
        c_obj.save()

        m1 = Match.objects.create(match_num=1, country_A=a_obj, country_B=c_obj, winner="Germany", score="3v1", match_date="2014-7-10")
        m1.save()

        #Wrong data search
        query="1v1"
        results = watson.search(query, ranking=True)
        self.assertEqual(len(results), 0)

        #prove that score is searchable as it is in charfield 
        query="3v1"
        results = watson.search(query, ranking=True)
        self.assertEqual(len(results), 1)










setup_test_environment()
#main()

