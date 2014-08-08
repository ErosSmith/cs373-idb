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
        expected_response =[{
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
        "id": 1,
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
    }, {
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
        "id": 2,
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
    }, {
        "article": "Ghana survived one of the continent's toughest qualifying groups by winning five of their six matches against 2012 African champions Zambia, Lesotho and Sudan. A 1-0 defeat in Zambia was their only set-back in a campaign that saw them outscore their opponents by 18 goals to three. That sent them into the final play-off round, where again the Black Stars were done no favours by the draw, which set them up against seven-time African champions Egypt. However, a resounding 6-1 win the home first leg basically settled the tie and sent them into their third FIFA World Cup in succession even before a meaningless 2-1 defeat in Cairo. An impressive FIFA World Cup finals in 2006 saw the Black Stars beat the Czech Republic and the USA before being eliminated by Brazil in the second round, but they were the only African team to escape their group. In 2010, they were again the only side from the continent in the knockout rounds, and they equalled Africa’s best-ever performance by beating the USA to reach the quarter-finals. Ghana’s loss in a penalty kick shoot-out to Uruguay in the last eight was perhaps the most dramatic of the tournament, and they may well consider themselves as having unfinished business after Asamoah Gyan’s missed penalty kick denied them from becoming the first African side to reach the semi-finals of a FIFA World Cup. There are few better midfields in the world than Ghana's as the Black Stars can call on veterans Michael Essien and Sulley Muntari as well as players hitting their prime like Andre Ayew, Kwadwo Asamoah and Kevin-Prince Boateng. Up front, the athletic Asamoah Gyan will be a vital focal point and no doubt anxious to prove that Ghana can be the undisputed class of Africa.  Kwesi AppiahFIFA World Cup South Africa 2010 (Quarter-finals), FIFA U-17 World Cup Italy 1991, Ecuador 1995 (Winners), FIFA U-20 World Cup Egypt 2009 (Winners)Abedi Pele, Samuel Kuffour, Ibrahim Sunday",
        "att_attempts": "58",
        "att_crosses": "60",
        "att_crosses_completed": "21",
        "att_crosses_completed_ta": "12.4",
        "att_crosses_ta": "52.2",
        "att_deliveries_penalty_area": "2",
        "att_deliveries_penalty_area_ta": "2.4",
        "att_dribble_penalty_area": "7",
        "att_dribble_penalty_area_ta": "7.9",
        "att_goals_scored": "8",
        "att_offsides": "14",
        "att_offsides_ta": "6.1",
        "att_shots_blocked": "4",
        "att_shots_saved": "11",
        "attempts_off_target": "35",
        "attempts_on_target": "24",
        "continent": "Africa",
        "country_code": "GHA",
        "country_name": "Ghana",
        "def_attempted_clearances": "28",
        "def_attempted_clearances_ta": "36",
        "def_blocks": "6",
        "def_completed_clearances": "24",
        "def_completed_clearances_ta": "30.1",
        "def_offsides_given": "2",
        "def_offsides_given_ta": "6.2",
        "def_recovered_balls": "140",
        "def_recovered_balls_ta": "115",
        "def_saves": "12",
        "def_saves_ta": "9.5",
        "def_tackles": "31",
        "def_tackles_lost": "23",
        "def_tackles_lost_ta": "29.1",
        "def_tackles_tol": "31",
        "def_tackles_tol_ta": "47.3",
        "def_tackles_won": "8",
        "def_tackles_won_ta": "12.6",
        "def_total_defense": "49",
        "distance_covered": "332.8",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ghana.png",
        "goals_scored": "4",
        "id": 3,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Ghana&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "3",
        "one_g_freq_attempts": "14.8",
        "one_g_freq_min": "68",
        "open_play_goals": "4",
        "pass_crosses": "60",
        "pass_crosses_ta": "52.2",
        "pass_long_passes_complete": "144",
        "pass_medium_passes_complete": "657",
        "pass_short_passes_complete": "264",
        "pass_ta": "1109",
        "pass_throw_ins": "123",
        "pass_throw_ins_ta": "89.3",
        "pass_total": "1065",
        "rank": 37,
        "resource_uri": "/api/countries/Ghana/",
        "scoring_method_total": "4",
        "set_piece_goals": "0",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ghana.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/gha.gif",
        "team_video_url": "//www.youtube.com/embed/5zQgjAESpZE",
        "tournament_average": "36.8"
    }, {
        "article": " Before finally securing their eighth consecutive FIFA World Cup™ qualification, Korea Republic had twice seen their campaign in significant peril. Unlike Japan, who counted on the same starting XI and Australia, who used their core of experienced players throughout qualification, a proven and reliable starting line-up was elusive for Korea Republic throughout the qualifying competition.  With the squad changing constantly, an unprepared Taeguk Warrior side were stunned 2-1 by Lebanon in the third round’s penultimate match, which left their hopes hanging by a thread. The defeat cost Cho Kwangrae his job but under new boss Choi Kanghee, Korea Republic dispatched Kuwait 2-0 to progress at the West Asian’s expense.  The next round continued nearly in the same vein, with Choi’s side floundering with draws against Uzbekistan and Lebanon and a defeat to Iran. A 1-0 home win against Uzbekistan in the penultimate game saw their fortunes revived, but after losing the closing game to Iran by the identical scoreline, they had to wait until Uzbekistan’s 5-1 defeat of Qatar to confirm their direct qualification by edging the central Asians on goal difference.  Despite being Asia’s most frequent visitors to world football’s showpiece event, Korea Republic had never won a match at the finals until they co-hosted Korea/Japan 2002. They got off to a winning start with victory over Poland before defeating Portugal to reach the second round for the first time. The Taeguk Warriors went on to reach the semi-finals at the expense of Italy and Spain, only to lose to Germany in the last four. In 2010, they made history again by reaching the knockout stage for the first time on foreign soil, before going down at the hands of Uruguay in the Round of 16.  The squad's make-up kept changing during the qualifying and under new coach Hong Myungbo, a new-look team has taken shape. A series of emerging stars, notably German-based Son Heungmin and Ji Dongwon, have graduated into the team's backbone force. Mainz's Koo Jacheol is the new man wearing the captain's armband and home-based Kim Shinwook and Lee Keunho are proven goal-scorers. Hong Myungbo FIFA World Cup Korea/Japan 2002 (Fourth place)Cha Bumkun, Hong Myungbo, Park Jisung",
        "att_attempts": "37",
        "att_crosses": "52",
        "att_crosses_completed": "15",
        "att_crosses_completed_ta": "12.8",
        "att_crosses_ta": "54.2",
        "att_deliveries_penalty_area": "0",
        "att_deliveries_penalty_area_ta": "2.5",
        "att_dribble_penalty_area": "5",
        "att_dribble_penalty_area_ta": "8.3",
        "att_goals_scored": "9",
        "att_offsides": "2",
        "att_offsides_ta": "6.4",
        "att_shots_blocked": "3",
        "att_shots_saved": "12",
        "attempts_off_target": "13",
        "attempts_on_target": "24",
        "continent": "Asia",
        "country_code": "KOR",
        "country_name": "Korea Republic",
        "def_attempted_clearances": "38",
        "def_attempted_clearances_ta": "36.9",
        "def_blocks": "11",
        "def_completed_clearances": "32",
        "def_completed_clearances_ta": "30.9",
        "def_offsides_given": "5",
        "def_offsides_given_ta": "6.5",
        "def_recovered_balls": "132",
        "def_recovered_balls_ta": "120",
        "def_saves": "12",
        "def_saves_ta": "10.2",
        "def_tackles": "42",
        "def_tackles_lost": "31",
        "def_tackles_lost_ta": "30.4",
        "def_tackles_tol": "42",
        "def_tackles_tol_ta": "48.8",
        "def_tackles_won": "11",
        "def_tackles_won_ta": "12.8",
        "def_total_defense": "65",
        "distance_covered": "333.0",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/korea.png",
        "goals_scored": "3",
        "id": 4,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Korea&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "3",
        "one_g_freq_attempts": "12.3",
        "one_g_freq_min": "90",
        "open_play_goals": "3",
        "pass_crosses": "52",
        "pass_crosses_ta": "54.2",
        "pass_long_passes_complete": "160",
        "pass_medium_passes_complete": "714",
        "pass_short_passes_complete": "276",
        "pass_ta": "1153",
        "pass_throw_ins": "95",
        "pass_throw_ins_ta": "93.6",
        "pass_total": "1150",
        "rank": 57,
        "resource_uri": "/api/countries/Korea%20Republic/",
        "scoring_method_total": "3",
        "set_piece_goals": "0",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/korea.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/kor.gif",
        "team_video_url": "//www.youtube.com/embed/OUkb2-vKFkU",
        "tournament_average": "38.5"
    }, {
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
        "id": 5,
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
    }, {
        "article": " Colombia began the South American qualifiers well enough, collecting four points from their first two games before defeat at home to Argentina in their third outing spelled the end of Leonel Alvarez’s reign as coach. The arrival of Jose Nestor Pekerman as his replacement represented a turning point for in their journey to Brazil 2014, with the Argentinian coach overseeing a run of five wins in their next six games, a sequence that put them firmly on course for the finals.  Colombia’s convincing home form at their Barranquilla citadel was central to their successful campaign, as was the balance between attack and defence and their cutting edge up front. No side in the group let in fewer goals than their 13 and only two of their continental rivals scored more than their 27. After clinching a trip to their first world finals since France 1998 on the penultimate matchday, the Colombians eventually took second place, their highest ever finish since the introduction of the current qualifying system.  With the exception of Italy 1990, when the golden generation that included Rene Higuita and Carlos Valderrama slipped up against unfancied Cameroon in the Round of 16, Colombia have never made it past the group stage at the FIFA World Cup. In fact, an analysis of the other three campaigns reveals a disappointing combined record of six defeats, one draw and just two wins at the tournament.  Despite the absence of Radamel Falcao, Colombia's attacking line still boasts strikers such as Teofilo Gutierrez, who scored six goals in qualifiers, Adrian Ramos, Bundesliga's best player, Carlos Bacca, UEFA Europe League champion with Sevilla and Porto's star Jackson Martinez. The creativity of James Rodriguez and the experience of Mario Yepes, captain and team's leader, also stand out for Colombia.  Jose PekermanFIFA U-20 World Cup UAE 2003 (Third place), FIFA World Cup Italy 1990 (Round of 16) Rene Higuita, Carlos Valderrama, Faustino Asprilla",
        "att_attempts": "57",
        "att_crosses": "65",
        "att_crosses_completed": "19",
        "att_crosses_completed_ta": "16.7",
        "att_crosses_ta": "71.3",
        "att_deliveries_penalty_area": "3",
        "att_deliveries_penalty_area_ta": "3",
        "att_dribble_penalty_area": "11",
        "att_dribble_penalty_area_ta": "10.4",
        "att_goals_scored": "12",
        "att_offsides": "10",
        "att_offsides_ta": "7.8",
        "att_shots_blocked": "10",
        "att_shots_saved": "16",
        "attempts_off_target": "19",
        "attempts_on_target": "38",
        "continent": "South America",
        "country_code": "COL",
        "country_name": "Colombia",
        "def_attempted_clearances": "56",
        "def_attempted_clearances_ta": "49.8",
        "def_blocks": "20",
        "def_completed_clearances": "47",
        "def_completed_clearances_ta": "41.1",
        "def_offsides_given": "6",
        "def_offsides_given_ta": "7.8",
        "def_recovered_balls": "180",
        "def_recovered_balls_ta": "151",
        "def_saves": "22",
        "def_saves_ta": "13",
        "def_tackles": "85",
        "def_tackles_lost": "63",
        "def_tackles_lost_ta": "40.2",
        "def_tackles_tol": "85",
        "def_tackles_tol_ta": "62.9",
        "def_tackles_won": "22",
        "def_tackles_won_ta": "17.1",
        "def_total_defense": "127",
        "distance_covered": "516.6",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/colombia.png",
        "goals_scored": "12",
        "id": 6,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Colombia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "5",
        "one_g_freq_attempts": "4.8",
        "one_g_freq_min": "38",
        "open_play_goals": "9",
        "pass_crosses": "65",
        "pass_crosses_ta": "71.3",
        "pass_long_passes_complete": "168",
        "pass_medium_passes_complete": "902",
        "pass_short_passes_complete": "407",
        "pass_ta": "1406",
        "pass_throw_ins": "159",
        "pass_throw_ins_ta": "117",
        "pass_total": "1477",
        "rank": 8,
        "resource_uri": "/api/countries/Colombia/",
        "scoring_method_total": "12",
        "set_piece_goals": "3",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/colombia.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/col.gif",
        "team_video_url": "//www.youtube.com/embed/67813ps8cR4",
        "tournament_average": "48.5"
    }, {
        "article": " Drawn alongside Portugal, Russia were not favourites to win Group F and earn direct passage to Brazil 2014. Expectations soon shifted after a perfect start to their campaign, as the Russians kicked off with wins over Northern Ireland and Israel. Having set the tone, Fabio Capello’s side then revealed their ambitions by beating the Portuguese in Moscow courtesy of a solitary Alexander Kerzhakov goal.  A narrow 1-0 defeat of Azerbaijan made it four wins out of four, at which point the Russians stumbled, losing to Portugal away and then going down unexpectedly to the Northern Irish in a fixture that had to be rescheduled due to bad weather. With the Portuguese breathing down their necks, Capello’s charges had no option but to react, which they did, sandwiching a home win over Israel with two defeats of Luxembourg. That run that left them needing only a draw away to the Azeris to book their return to the world finals, a result they duly secured.  Russia reached the quarter-finals at Sweden 1958, Chile 1962 and Mexico 1970. In the former two tournaments, they were eliminated by the hosts, while Uruguay were accountable for their exit after extra time in Mexico City. The Eastern Europeans went one better at England 1966, when, inspired by goalkeeper Lev Yashin and forward Igor Chislenko, they topped their group and edged a formidable Hungary, before losing 2-1 to both West Germany in the semis and Portugal in the play-off for third place.  First-phase elimination befell the Russians in the last two appearances at the FIFA World Cup, at USA 1994 and Korea/Japan 2002, though they made their mark in the States with a crushing 6-1 defeat of Cameroon, a match in which Oleg Salenko scored five goals en route to ending the tournament as joint leading marksman. Russia then failed to reach Germany 2006 and South Africa 2010, the second of those campaigns ending in frustration in the play-offs, where they were beaten by Slovenia. This latest Russian side is built on solid defensive foundations. Goalkeeper Igor Akinfeev did not miss a single minute of the qualifying competition and conceded just five goals during the course of it, while Sergey Ignashevich marshalled the defence with aplomb. Yet Fabio Capello’s most prized assets can be found in what is a technically gifted and astute midfield unit, where Victor Fayzulin had a successful qualifying campaign. Captain Roman Shirokov will miss the tournament due to a knee ligament injury.  Perhaps not surprisingly, the team’s top scorer was Kerzhakov. Though not always a starter, the Zenit striker helped himself to five goals during the campaign, the most important of them being that winner against the Portuguese. A lethal finisher, the former Sevilla man could wreak havoc in Brazil. Fabio CapelloFIFA World Cup England 1966 (Fourth place) Yashin, Eduard Streltsov, Oleg Blokhin",
        "att_attempts": "39",
        "att_crosses": "74",
        "att_crosses_completed": "15",
        "att_crosses_completed_ta": "12.8",
        "att_crosses_ta": "54.2",
        "att_deliveries_penalty_area": "2",
        "att_deliveries_penalty_area_ta": "2.5",
        "att_dribble_penalty_area": "4",
        "att_dribble_penalty_area_ta": "8.3",
        "att_goals_scored": "10",
        "att_offsides": "3",
        "att_offsides_ta": "6.4",
        "att_shots_blocked": "2",
        "att_shots_saved": "11",
        "attempts_off_target": "16",
        "attempts_on_target": "23",
        "continent": "Europe",
        "country_code": "RUS",
        "country_name": "Russia",
        "def_attempted_clearances": "32",
        "def_attempted_clearances_ta": "36.9",
        "def_blocks": "6",
        "def_completed_clearances": "29",
        "def_completed_clearances_ta": "30.9",
        "def_offsides_given": "9",
        "def_offsides_given_ta": "6.5",
        "def_recovered_balls": "131",
        "def_recovered_balls_ta": "120",
        "def_saves": "10",
        "def_saves_ta": "10.2",
        "def_tackles": "33",
        "def_tackles_lost": "27",
        "def_tackles_lost_ta": "30.4",
        "def_tackles_tol": "33",
        "def_tackles_tol_ta": "48.8",
        "def_tackles_won": "6",
        "def_tackles_won_ta": "12.8",
        "def_total_defense": "49",
        "distance_covered": "347.5",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/russia.png",
        "goals_scored": "2",
        "id": 7,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Russia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "3",
        "one_g_freq_attempts": "19.5",
        "one_g_freq_min": "135",
        "open_play_goals": "2",
        "pass_crosses": "74",
        "pass_crosses_ta": "54.2",
        "pass_long_passes_complete": "114",
        "pass_medium_passes_complete": "754",
        "pass_short_passes_complete": "309",
        "pass_ta": "1153",
        "pass_throw_ins": "100",
        "pass_throw_ins_ta": "93.6",
        "pass_total": "1177",
        "rank": 19,
        "resource_uri": "/api/countries/Russia/",
        "scoring_method_total": "2",
        "set_piece_goals": "0",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/russia.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/rus.gif",
        "team_video_url": "//www.youtube.com/embed/pNii1Iy02Jc",
        "tournament_average": "38.5"
    }, {
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
        "id": 8,
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
    }, {
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
        "id": 9,
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
    }, {
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
        "id": 10,
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
    }, {
        "article": " Switzerland secured their place at the 2014 FIFA World Cup Brazil™ on the penultimate qualifying matchday. However, it was far from plain sailing for Die Eidgenossen, who faced several setbacks along the way.  Coach Ottmar Hitzfeld’s ensemble raced to the group summit following opening victories over Slovenia and Albania, but dropped points for the first time in their next qualifying games. Hitzfeld's charges recorded a 1-1 draw with Norway and a 2-0 victory over Iceland before chalking up a draw and a win against Cyprus. Nerves got the better of Switzerland in their next game against Iceland, when they ended up drawing 4-4 after leading 4-1. There were no further slip-ups in their final outings though, with a 2-0 triumph over Norway all but ensuring their qualification for a third consecutive World Cup, before a 2-1 win over Albania sealed Switzerland’s Brazil 2014 ticket with a game to spare.  Switzerland have contested the FIFA World Cup finals nine times to date (1934, 1938, 1950, 1954, 1962, 1966, 1994, 2006 and 2010), reaching the last eight on three occasions. However, their most recent appearance at the quarter-final stage came almost 50 years ago, at the 1954 finals on home soil.  Since then, the Swiss have twice made the last sixteen (1994 and 2006), but failed to survive the group stage three times. Their group campaign in 2010 was a bittersweet affair: they handed eventual world champions Spain a 1-0 defeat in their opening fixture, but ultimately packed for home after just three games.  There is undoubted quality throughout the side, starting with keeper Diego Benaglio, a German championship winner in 2009 with VfL Wolfsburg. The combination of experienced players such as Tranquillo Barnetta, Gokhan Inler and Philippe Senderos, with highly-talented youngsters Xherdan Shaqiri, Fabian Schar, Granit Xhaka and Valentin Stocker, has borne fruit and the side are more than capable of making their mark at Brazil 2014.  Ottmar HitzfeldFIFA U-17 World Cup Nigeria 2009 (Winners), FIFA Beach Soccer World Cup Dubai 2009 (Runners-up), FIFA World Cup Italy 1934, France 1938, Switzerland 1954 (Quarter-finals) Alexander Frei, Stephane Chapuisat, Johann Vogel, Hakan Yakin",
        "att_attempts": "65",
        "att_crosses": "59",
        "att_crosses_completed": "14",
        "att_crosses_completed_ta": "16",
        "att_crosses_ta": "69.1",
        "att_deliveries_penalty_area": "5",
        "att_deliveries_penalty_area_ta": "2.9",
        "att_dribble_penalty_area": "8",
        "att_dribble_penalty_area_ta": "10",
        "att_goals_scored": "14",
        "att_offsides": "5",
        "att_offsides_ta": "7.6",
        "att_shots_blocked": "7",
        "att_shots_saved": "19",
        "attempts_off_target": "25",
        "attempts_on_target": "40",
        "continent": "Europe",
        "country_code": "SUI",
        "country_name": "Switzerland",
        "def_attempted_clearances": "82",
        "def_attempted_clearances_ta": "47.5",
        "def_blocks": "21",
        "def_completed_clearances": "60",
        "def_completed_clearances_ta": "39.3",
        "def_offsides_given": "6",
        "def_offsides_given_ta": "7.6",
        "def_recovered_balls": "179",
        "def_recovered_balls_ta": "146",
        "def_saves": "22",
        "def_saves_ta": "12.7",
        "def_tackles": "77",
        "def_tackles_lost": "43",
        "def_tackles_lost_ta": "39.3",
        "def_tackles_tol": "77",
        "def_tackles_tol_ta": "61.6",
        "def_tackles_won": "28",
        "def_tackles_won_ta": "16.8",
        "def_total_defense": "120",
        "distance_covered": "472.9",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/switzerland.png",
        "goals_scored": "7",
        "id": 11,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Switzerland&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "4",
        "one_g_freq_attempts": "9.3",
        "one_g_freq_min": "56",
        "open_play_goals": "5",
        "pass_crosses": "59",
        "pass_crosses_ta": "69.1",
        "pass_long_passes_complete": "122",
        "pass_medium_passes_complete": "976",
        "pass_short_passes_complete": "456",
        "pass_ta": "1366",
        "pass_throw_ins": "125",
        "pass_throw_ins_ta": "113",
        "pass_total": "1554",
        "rank": 6,
        "resource_uri": "/api/countries/Switzerland/",
        "scoring_method_total": "7",
        "set_piece_goals": "2",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/switzerland.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/sui.gif",
        "team_video_url": "//www.youtube.com/embed/lIrKW0_gPdY",
        "tournament_average": "47.1"
    }, {
        "article": "  For the second time in succession Portugal had to go through the play-offs in order to advance to the world finals. Reprising their aggregate defeat of Bosnia and Herzegovina on the road to South Africa 2010, the Portuguese saw off Sweden 4-2 over two legs to book their place at Brazil 2014. Their hero of the hour was none other than Cristiano Ronaldo, who scored all four of their goals against the Swedes to round off a qualifying tournament full of ups and downs for Paulo Bento’s side.  They began their bid to reach their sixth FIFA World Cup as the favourites to win Group F, having made the semi-finals of UEFA EURO 2012, where they lost on penalties to Spain. And though they held their own against Russia, losing in Moscow but winning the return fixture in Lisbon, the Portuguese had to settle for second place in the section after surprise draws at home to Northern Ireland and home and away to Israel. That left them with no option but to take the play-off route again, but in a duel that pitted together two of the world’s best players, Ronaldo got the better of Zlatan Ibrahimovic, the scorer of his side’s two goals, to guide the Portuguese safely to Brazil. It was not until England 1966 that the Portuguese made their world finals debut, yet as entrances go it could hardly have been more impressive. Spearheaded by the irrepressible Eusebio, Portugal’s golden generation knocked out Brazil en route to the semi-finals, where they came up just short against the host nation. Consolation came in the shape of victory over the Soviet Union in the match for third place. The Portuguese do not have happy memories of their next appearance on the big stage, however, which came at Mexico 1986. Despite opening up with a win over England, they went out in the group phase after defeats to Poland and Morocco.  Absent from Italy 1990, USA 1994 and France 1998, the Portuguese contested their third World Cup at Korea/Japan 2002, where they once again fell at the first hurdle. A very different story would follow at Germany 2006. Coached on that occasion by Luiz Felipe Scolari, the man who had taken Brazil to the world title four years earlier, Portugal made it all the way to last four before being knocked out by a Zinedine Zidane penalty, with Scolari’s side then going on to lose the match for third place against hosts Germany. In South Africa four years later Portugal’s dream ended in the Round of 16, when they were edged out 1-0 be eventual champions Spain.  As he showed in the play-off against Sweden, Cristiano Ronaldo is still very much Portugal’s go-to man, though the peerless Real Madrid star is supported is by a very able cast. The central-defensive pairing of Pepe and Bruno Alves is the cornerstone of a very solid rearguard that also features flying full-backs Joao Pereira and Fabio Coentrao. Joao Moutinho is the heartbeat of a creative midfield unit, while Nani can also be relied upon to shine alongside Ronaldo. Paulo Bento  1966 FIFA World Cup England (third place), FIFA U-20 World Cup Saudi Arabia 1989 and Portugal 1991 (winners), FIFA U-20 World Cup Colombia 2011 (runners-up), FIFA U-17 World Cup Scotland 1989 (third place).  Eusebio, Coluna, Simoes, Jose Augusto, Torres, Jaime Graca, Rui Costa and Luis Figo.",
        "att_attempts": "53",
        "att_crosses": "68",
        "att_crosses_completed": "13",
        "att_crosses_completed_ta": "12.4",
        "att_crosses_ta": "52.2",
        "att_deliveries_penalty_area": "1",
        "att_deliveries_penalty_area_ta": "2.4",
        "att_dribble_penalty_area": "6",
        "att_dribble_penalty_area_ta": "7.9",
        "att_goals_scored": "11",
        "att_offsides": "5",
        "att_offsides_ta": "6.1",
        "att_shots_blocked": "3",
        "att_shots_saved": "14",
        "attempts_off_target": "25",
        "attempts_on_target": "28",
        "continent": "Europe",
        "country_code": "POR",
        "country_name": "Portugal",
        "def_attempted_clearances": "21",
        "def_attempted_clearances_ta": "36",
        "def_blocks": "7",
        "def_completed_clearances": "14",
        "def_completed_clearances_ta": "30.1",
        "def_offsides_given": "7",
        "def_offsides_given_ta": "6.2",
        "def_recovered_balls": "130",
        "def_recovered_balls_ta": "115",
        "def_saves": "7",
        "def_saves_ta": "9.5",
        "def_tackles": "35",
        "def_tackles_lost": "25",
        "def_tackles_lost_ta": "29.1",
        "def_tackles_tol": "35",
        "def_tackles_tol_ta": "47.3",
        "def_tackles_won": "10",
        "def_tackles_won_ta": "12.6",
        "def_total_defense": "52",
        "distance_covered": "323.1",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/portugal.png",
        "goals_scored": "3",
        "id": 12,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Portugal&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "3",
        "one_g_freq_attempts": "13.3",
        "one_g_freq_min": "68",
        "open_play_goals": "4",
        "pass_crosses": "68",
        "pass_crosses_ta": "52.2",
        "pass_long_passes_complete": "143",
        "pass_medium_passes_complete": "839",
        "pass_short_passes_complete": "315",
        "pass_ta": "1109",
        "pass_throw_ins": "90",
        "pass_throw_ins_ta": "89.3",
        "pass_total": "1297",
        "rank": 4,
        "resource_uri": "/api/countries/Portugal/",
        "scoring_method_total": "4",
        "set_piece_goals": "0",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/portugal.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/por.gif",
        "team_video_url": "//www.youtube.com/embed/DSyYg_N3zcw",
        "tournament_average": "36.8"
    }, {
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
        "id": 13,
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
    }, {
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
        "id": 14,
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
    }, {
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
        "id": 15,
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
    }, {
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
        "id": 16,
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
    }, {
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
        "id": 17,
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
    }, {
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
        "id": 18,
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
    }, {
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
        "id": 19,
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
    }, {
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
        "id": 20,
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
    }, {
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
        "id": 21,
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
    }, {
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
        "id": 22,
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
    }, {
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
        "id": 23,
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
    }, {
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
        "id": 24,
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
    }, {
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
        "id": 25,
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
    }, {
        "article": "After Chile started their qualifying campaign by winning 12 of the first 18 points on offer, including away victories in Bolivia and Venezuela, three consecutive defeats (among them two home fixtures against Colombia and Argentina) spelled the end of Argentinian coach Claudio Borghi’s tenure. His compatriot Jorge Sampaoli was brought in as a replacement, although his reign got off to a poor start with a reverse in Peru. Yet the loss marked a turning point in Chile’s campaign, as they subsequently embarked on their best ever run of results in FIFA World Cup™ qualifying, chalking up five victories and a draw in their next six encounters to qualify for a second successive World Cup for the first time. Under Sampaoli La Roja developed into an extremely attack-minded team, so much so that their 29-goal haul during qualification was bettered by only one nation. However, they also conceded more often (25 times) than any of the continent’s other automatic qualifiers and drew only once in their 16 qualifying fixtures. With eight FIFA World Cups™ under their belts, Chile are level with Paraguay in fourth place on the list of South American nations that have appeared at most editions of the showpiece event. Their best performance to date came when finishing third as host nation in 1962. On five other occasions they have failed to progress from the group phase, while at France 1998 and South Africa 2010 they reached the Round of 16, only to exit at the hands of Brazil on both occasions.. Forwards Alexis Sanchez and Eduardo Vargas, as well as attacking midfielders Matias Fernandez and Arturo Vidal, are the leading men in a squad packed with talent and boasting viable alternatives in each position. Nor must we forget experienced performers such as Claudio Bravo, Gary Medel and Jorge Valdivia, or exciting rising stars like Jean Beausejour and Marcelo Diaz. Jorge Sampaoli FIFA World Cup Chile 1962 (Third place), FIFA U-17 World Cup Japan 1993 (Third place), FIFA U-20 World Cup Canada 2007 (Third place), Men’s Olympic Football Tournament Sydney 2000 (Third place)Elias Figueroa, Ivan Zamorano, Marcelo Salas",
        "att_attempts": "38",
        "att_crosses": "74",
        "att_crosses_completed": "17",
        "att_crosses_completed_ta": "13.3",
        "att_crosses_ta": "56.2",
        "att_deliveries_penalty_area": "2",
        "att_deliveries_penalty_area_ta": "2.6",
        "att_dribble_penalty_area": "15",
        "att_dribble_penalty_area_ta": "8.7",
        "att_goals_scored": "6",
        "att_offsides": "8",
        "att_offsides_ta": "6.6",
        "att_shots_blocked": "6",
        "att_shots_saved": "7",
        "attempts_off_target": "19",
        "attempts_on_target": "19",
        "continent": "South America",
        "country_code": "CHI",
        "country_name": "Chile",
        "def_attempted_clearances": "74",
        "def_attempted_clearances_ta": "38.7",
        "def_blocks": "14",
        "def_completed_clearances": "61",
        "def_completed_clearances_ta": "32.3",
        "def_offsides_given": "5",
        "def_offsides_given_ta": "6.6",
        "def_recovered_balls": "193",
        "def_recovered_balls_ta": "124",
        "def_saves": "18",
        "def_saves_ta": "10.3",
        "def_tackles": "83",
        "def_tackles_lost": "55",
        "def_tackles_lost_ta": "32.5",
        "def_tackles_tol": "83",
        "def_tackles_tol_ta": "51.7",
        "def_tackles_won": "19",
        "def_tackles_won_ta": "13.6",
        "def_total_defense": "115",
        "distance_covered": "481.2",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/chile.png",
        "goals_scored": "6",
        "id": 26,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Chile&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "4",
        "one_g_freq_attempts": "6.3",
        "one_g_freq_min": "65",
        "open_play_goals": "6",
        "pass_crosses": "74",
        "pass_crosses_ta": "56.2",
        "pass_long_passes_complete": "256",
        "pass_medium_passes_complete": "1235",
        "pass_short_passes_complete": "359",
        "pass_ta": "1179",
        "pass_throw_ins": "158",
        "pass_throw_ins_ta": "96.2",
        "pass_total": "1850",
        "rank": 14,
        "resource_uri": "/api/countries/Chile/",
        "scoring_method_total": "6",
        "set_piece_goals": "0",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/chile.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/chi.gif",
        "team_video_url": "//www.youtube.com/embed/_bnOs1Av5nw",
        "tournament_average": "39.6"
    }, {
        "article": "  Croatia put their fans through the emotional mill in their qualification campaign. The Balkan team looked to be cruising after winning five and drawing one of their first six games, but they then took just one point from the next 12 available, losing at home to Scotland (1-0) and Belgium (2-1). Their good start eventually laid the foundation for a second-place finish, two points ahead of Serbia but nine adrift of runaway leaders Belgium. A day after the final group game, Igor Stimac resigned from his post as head coach, with former Bundesliga player and Croatian international Niko Kovac – up until then in charge of the U-21 team – replacing him. Assisted by his brother Robert, Niko successfully led Croatia through their play-off against Iceland, but they were pushed all the way. Despite having a man advantage for long spells, the first leg ended goalless, before Croatia prevailed 2-0 in the return fixture. Mario Mandzukic grabbed the opener with Darijo Srna’s decisive effort giving supporters the cue to celebrate, although a red card shown to Mandzukic – one that means he will likely miss Croatia’s tournament opener – may dampen the mood somewhat by the time the tournament rolls around. The Croats arrived for their maiden shot at the FIFA World Cup™ in 1998 as virtual unknowns, but were to prove one of the surprises of the tournament. They finished second in their group behind Argentina after losing 1-0 to the South Americans, but beating Jamaica 3-1 and Japan 1-0. A 1-0 win over Romania saw them through to the last eight and a meeting with Germany, where they stunningly won 3-0 to send the three-time world champions packing. Hosts and eventual winners France proved too strong in a 2-1 semi-final defeat, but the new boys crowned a dream debut by beating the Netherlands 2-1 in the third place play-off. The next two tournaments proved thoroughly disappointing by comparison, as Croatia failed to survive the group stage at both Korea/Japan 2002 and Germany 2006.  Despite their absence from the 2010 finals, Croatia are a match for anyone on their day. Their goal is to recapture the glory days of the late 90's golden generation, of which he himself was a member. With many of the squad playing regularly in the English Premier League and the German Bundesliga, there is no reason why they cannot make an impact at Brazil 2014.  Experienced captain Darijo Srna is a born leader, and playmakers Luka Modric and Ivan Rakitic can always be relied upon for moments of inspiration. Kovac presides over a wealth of international-class attacking talent including Eduardo, Ivica Olic, Nikita Jelavic and Mario Mandzukic.  Niko Kovac1998 FIFA World Cup France (Third place) Davor Suker, Zvonimir Boban, Robert Prosinecki",
        "att_attempts": "41",
        "att_crosses": "68",
        "att_crosses_completed": "19",
        "att_crosses_completed_ta": "9.9",
        "att_crosses_ta": "41",
        "att_deliveries_penalty_area": "2",
        "att_deliveries_penalty_area_ta": "1.9",
        "att_dribble_penalty_area": "15",
        "att_dribble_penalty_area_ta": "6.4",
        "att_goals_scored": "8",
        "att_offsides": "5",
        "att_offsides_ta": "4.9",
        "att_shots_blocked": "5",
        "att_shots_saved": "10",
        "attempts_off_target": "18",
        "attempts_on_target": "23",
        "continent": "Europe",
        "country_code": "CRO",
        "country_name": "Croatia",
        "def_attempted_clearances": "35",
        "def_attempted_clearances_ta": "29.4",
        "def_blocks": "5",
        "def_completed_clearances": "35",
        "def_completed_clearances_ta": "24.5",
        "def_offsides_given": "2",
        "def_offsides_given_ta": "4.9",
        "def_recovered_balls": "107",
        "def_recovered_balls_ta": "88.8",
        "def_saves": "5",
        "def_saves_ta": "7.3",
        "def_tackles": "59",
        "def_tackles_lost": "32",
        "def_tackles_lost_ta": "21.8",
        "def_tackles_tol": "59",
        "def_tackles_tol_ta": "36.7",
        "def_tackles_won": "16",
        "def_tackles_won_ta": "9.3",
        "def_total_defense": "77",
        "distance_covered": "314.4",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/croatia.png",
        "goals_scored": "5",
        "id": 27,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Croatia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "3",
        "one_g_freq_attempts": "8.2",
        "one_g_freq_min": "54",
        "open_play_goals": "5",
        "pass_crosses": "68",
        "pass_crosses_ta": "41",
        "pass_long_passes_complete": "171",
        "pass_medium_passes_complete": "613",
        "pass_short_passes_complete": "237",
        "pass_ta": "868",
        "pass_throw_ins": "110",
        "pass_throw_ins_ta": "70.5",
        "pass_total": "1021",
        "rank": 18,
        "resource_uri": "/api/countries/Croatia/",
        "scoring_method_total": "6",
        "set_piece_goals": "1",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/croatia.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/cro.gif",
        "team_video_url": "//www.youtube.com/embed/n_0Yz0-nrSQ",
        "tournament_average": "28.7"
    }, {
        "article": " Often below par during qualifying before raising their game at final tournaments, Italy went about things differently for once by taking imperious control of Group B in the European Zone. Their task appeared potentially tricky when they were drawn alongside Denmark, the Czech Republic and Bulgaria, but  surged through unbeaten and booked their ticket to Brazil with time to spare, meaning they will head to the finals confident that their internal revolution has been a success. After all, Cesare Prandelli seems to have consigned  to the past. \"It's now obvious that you can't get results without playing attractive football,\" explained the coach when he first took over. Since then he has led the side to the UEFA EURO 2012 showpiece and a 14 consecutive FIFA World Cup™ finals berth – all while remaining faithful to an attacking style of play.  With four world titles to their name (1934, 1938, 1982 and 2006) and two runners-up slots (1970 and 1994), Italy lie second only to Brazil on the all-time FIFA World Cup honours board.  are also the only team along with the Brazilians to have won the competition twice in a row. Their 4-3 semi-final defeat of West Germany at Mexico 1970 is widely regarded as one of the most spectacular matches in the history of the tournament. Captain and goalkeeper Gianluigi Buffon is the only survivor from their 2006 triumph in Germany along with Andrea Pirlo, while a host of youngsters have broken into the team, such as central defender Andrea Ranocchia and midfielder Marco Verratti. Up front, the transition from old to new has been even more dramatic thanks to the emergence of Stephan El Shaarawy and Giuseppe Rossi's return to the fore. Also with a vital role to play are the maverick duo of Mario Balotelli and Pablo Osvaldo.  Cesare Prandelli FIFA World Cup Italy 1934, France 1938, Spain 1982 and Germany 2006 (Winners), Men's Olympic Football Tournament Berlin 1936 (Winners) Dino Zoff, Paolo Maldini, Silvio Piola",
        "att_attempts": "31",
        "att_crosses": "36",
        "att_crosses_completed": "6",
        "att_crosses_completed_ta": "10.5",
        "att_crosses_ta": "44.9",
        "att_deliveries_penalty_area": "1",
        "att_deliveries_penalty_area_ta": "2.2",
        "att_dribble_penalty_area": "3",
        "att_dribble_penalty_area_ta": "7.1",
        "att_goals_scored": "6",
        "att_offsides": "21",
        "att_offsides_ta": "5.3",
        "att_shots_blocked": "2",
        "att_shots_saved": "8",
        "attempts_off_target": "15",
        "attempts_on_target": "16",
        "continent": "Europe",
        "country_code": "ITA",
        "country_name": "Italy",
        "def_attempted_clearances": "33",
        "def_attempted_clearances_ta": "31.8",
        "def_blocks": "8",
        "def_completed_clearances": "24",
        "def_completed_clearances_ta": "26.4",
        "def_offsides_given": "5",
        "def_offsides_given_ta": "5.3",
        "def_recovered_balls": "113",
        "def_recovered_balls_ta": "99.8",
        "def_saves": "12",
        "def_saves_ta": "7.9",
        "def_tackles": "37",
        "def_tackles_lost": "23",
        "def_tackles_lost_ta": "24.6",
        "def_tackles_tol": "37",
        "def_tackles_tol_ta": "40.7",
        "def_tackles_won": "11",
        "def_tackles_won_ta": "10.5",
        "def_total_defense": "57",
        "distance_covered": "321.3",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/italy.png",
        "goals_scored": "2",
        "id": 28,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Italy&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "3",
        "one_g_freq_attempts": "15.5",
        "one_g_freq_min": "135",
        "open_play_goals": "2",
        "pass_crosses": "36",
        "pass_crosses_ta": "44.9",
        "pass_long_passes_complete": "117",
        "pass_medium_passes_complete": "1039",
        "pass_short_passes_complete": "424",
        "pass_ta": "956",
        "pass_throw_ins": "77",
        "pass_throw_ins_ta": "77.9",
        "pass_total": "1580",
        "rank": 9,
        "resource_uri": "/api/countries/Italy/",
        "scoring_method_total": "2",
        "set_piece_goals": "0",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/italy.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/ita.gif",
        "team_video_url": "//www.youtube.com/embed/NofTWmHkDg8",
        "tournament_average": "31.8"
    }, {
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
        "id": 29,
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
    }, {
        "article": "So demanding are the Brazilian faithful, even a  squad that finishes runners-up at a FIFA World Cup finals cannot be sure what kind of reception they will get on their return home. The only nation to have taken part in every edition of the elite competition, Brazil have lifted the coveted Trophy on a record five occasions (1958, 1962, 1970, 1994 and 2002), finished in second place twice (1950 and 1998) and taken the last spot on the podium at another two editions (1938 and 1978).  Given they are set to host the next FIFA World Cup, Brazil have been spared the rigours of South American Zone qualifying. With that in mind, and fully aware of the enormous burden of expectation sure to surround  in 2014, the national set-up have put in place an intense preparatory process featuring friendly clashes against fellow members of the global elite. This approach has been underlined by meetings with opponents of the calibre of Argentina, France, USA and the Netherlands since South Africa 2010. However, in their first major test on the road to 2014, the Brazil crashed out of the 2011 Copa America at the quarter-final stage, eliminated by Paraguay. Striker Neymar is already being hailed as a man capable of playing a key role for the five-time world champions come Brazil 2014. Currently among the supporting cast in attack is the youngster’s former Santos team-mate Robinho, while Barcelona’s Dani Alves is a lung-bursting presence on the flank. Between the sticks, veteran goalkeeper Julio Cesar exudes confidence and security to the rest of the backline.  Luiz Felipe Scolari FIFA World Cup Sweden 1958, Chile 1962, Mexico 1970, USA 1994, Korea/Japan 2002 (Winners), FIFA U-20 World Cup Mexico 1983, USSR 1985, Australia 1993, UAE 2003 (Winners), FIFA U-17 World Cup Egypt 1997, New Zealand 1999, Finland 2003 (Winners), FIFA Confederations Cup Saudi Arabia 1997, Germany 2005, South Africa 2009 (Winners) Garrincha, Pele, Ronaldo",
        "att_attempts": "111",
        "att_crosses": "155",
        "att_crosses_completed": "36",
        "att_crosses_completed_ta": "17.8",
        "att_crosses_ta": "77",
        "att_deliveries_penalty_area": "7",
        "att_deliveries_penalty_area_ta": "3.1",
        "att_dribble_penalty_area": "26",
        "att_dribble_penalty_area_ta": "11.7",
        "att_goals_scored": "28",
        "att_offsides": "15",
        "att_offsides_ta": "8.9",
        "att_shots_blocked": "11",
        "att_shots_saved": "33",
        "attempts_off_target": "39",
        "attempts_on_target": "72",
        "continent": "South America",
        "country_code": "BRA",
        "country_name": "Brazil",
        "def_attempted_clearances": "93",
        "def_attempted_clearances_ta": "54.6",
        "def_blocks": "10",
        "def_completed_clearances": "73",
        "def_completed_clearances_ta": "45.3",
        "def_offsides_given": "9",
        "def_offsides_given_ta": "8.9",
        "def_recovered_balls": "300",
        "def_recovered_balls_ta": "164",
        "def_saves": "10",
        "def_saves_ta": "13.8",
        "def_tackles": "141",
        "def_tackles_lost": "93",
        "def_tackles_lost_ta": "43",
        "def_tackles_tol": "141",
        "def_tackles_tol_ta": "66.8",
        "def_tackles_won": "48",
        "def_tackles_won_ta": "18.2",
        "def_total_defense": "168",
        "distance_covered": "747.6",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png",
        "goals_scored": "11",
        "id": 30,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "7",
        "one_g_freq_attempts": "10.1",
        "one_g_freq_min": "60",
        "open_play_goals": "8",
        "pass_crosses": "155",
        "pass_crosses_ta": "77",
        "pass_long_passes_complete": "316",
        "pass_medium_passes_complete": "1688",
        "pass_short_passes_complete": "727",
        "pass_ta": "1547",
        "pass_throw_ins": "203",
        "pass_throw_ins_ta": "127",
        "pass_total": "2731",
        "rank": 3,
        "resource_uri": "/api/countries/Brazil/",
        "scoring_method_total": "11",
        "set_piece_goals": "3",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/bra.gif",
        "team_video_url": "//www.youtube.com/embed/6E_Lav_N-Ho",
        "tournament_average": "52"
    }, {
        "article": " The Netherlands positively cruised into the finals of Brazil 2014, coming through as Europe's the joint-top point scorers - alongside Germany - on 28, with their 2-2 draw against Estonia the only minor blemish on a near-faultless campaign. At times they were absolutely purring, in no game more so than their 8-1 defeat of Hungary, while Germany were the only side on the continent to score more goals than their 34. They registered comfortable wins over their three main Group D rivals - Turkey, Hungary and Romania - in their opening four games to see them shoot clear of the competition, with only a spectacular collapse looking able to deny them an automatic spot. That never came and a, somewhat nervy, 2-0 win over Andorra saw them, alongside Italy, become the first Europeans to seal their place in Brazil. They finished nine points ahead of Romania, a gap only matched by neighbours Belgium.  With legendary coach Rinus Michels pulling the strings from the bench, Johan Cruyff, Johan Neeskens and Co won their way through to the Final in 1974, only to lose out to hosts Germany. Four years on, their revolutionary Total Football again took them to the showpiece, but history repeated itself as they suffered another defeat to the host nation, succumbing 3-1 in Buenos Aires. The  then experienced Final heartbreak for a third time in Johannesburg, coming within four minutes of taking Spain to penalties before Andres Iniesta crushed their dreams.  Robin van Persie's blossoming into one of the finest strikers in the world has been a huge boon to the Dutch, with the Manchester United marksman topping the goal-scoring charts with 11 goals. He was able assisted in that department though by Jermaine Lens, who has progressed into a key part of the outfit. Arjen Robben continues to be a menace on the wing, while formerly promising youngsters such as Daley Blind and Daryl Janmaat are now key components of the side.  Louis Van Gaal FIFA World Cup Germany 1974, Argentina 1978, South Africa 2010 (Runners-up), FIFA Futsal World Cup Netherlands 1989 (Runners-up), Men’s Olympic Football Tournament London 1908, Stockholm 1912, Antwerp 1920 (Third place), FIFA U-17 World Cup Peru 2005 (Third place) Johan Cruyff, Marco van Basten, Dennis Bergkamp",
        "att_attempts": "90",
        "att_crosses": "121",
        "att_crosses_completed": "28",
        "att_crosses_completed_ta": "17.8",
        "att_crosses_ta": "77",
        "att_deliveries_penalty_area": "7",
        "att_deliveries_penalty_area_ta": "3.1",
        "att_dribble_penalty_area": "31",
        "att_dribble_penalty_area_ta": "11.7",
        "att_goals_scored": "23",
        "att_offsides": "27",
        "att_offsides_ta": "8.9",
        "att_shots_blocked": "15",
        "att_shots_saved": "26",
        "attempts_off_target": "26",
        "attempts_on_target": "64",
        "continent": "Europe",
        "country_code": "NED",
        "country_name": "Netherlands",
        "def_attempted_clearances": "93",
        "def_attempted_clearances_ta": "54.6",
        "def_blocks": "13",
        "def_completed_clearances": "81",
        "def_completed_clearances_ta": "45.3",
        "def_offsides_given": "16",
        "def_offsides_given_ta": "8.9",
        "def_recovered_balls": "308",
        "def_recovered_balls_ta": "164",
        "def_saves": "18",
        "def_saves_ta": "13.8",
        "def_tackles": "92",
        "def_tackles_lost": "57",
        "def_tackles_lost_ta": "43",
        "def_tackles_tol": "92",
        "def_tackles_tol_ta": "66.8",
        "def_tackles_won": "30",
        "def_tackles_won_ta": "18.2",
        "def_total_defense": "123",
        "distance_covered": "826.3",
        "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/netherlands.png",
        "goals_scored": "15",
        "id": 31,
        "map_url": "https://www.google.com/maps/embed/v1/place?q=Netherlands&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
        "matches_played": "7",
        "one_g_freq_attempts": "6",
        "one_g_freq_min": "46",
        "open_play_goals": "13",
        "pass_crosses": "121",
        "pass_crosses_ta": "77",
        "pass_long_passes_complete": "425",
        "pass_medium_passes_complete": "2006",
        "pass_short_passes_complete": "569",
        "pass_ta": "1547",
        "pass_throw_ins": "228",
        "pass_throw_ins_ta": "127",
        "pass_total": "3000",
        "rank": 15,
        "resource_uri": "/api/countries/Netherlands/",
        "scoring_method_total": "15",
        "set_piece_goals": "2",
        "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/netherlands.jpg",
        "team_logo_url": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/ned.gif",
        "team_video_url": "//www.youtube.com/embed/BJt7Bm_xiRg",
        "tournament_average": "52"
    }, {
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
        "id": 32,
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
          "id": 1,
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
        }

        request = Request(self.url+"api/countries/Ivory%20Coast/")
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
        expected_response = [{
      "biography": "Birmingham-born Daniel Sturridge is a forward who was developed by Coventry City and Manchester City before Chelsea signed him in July 2009.  He became the first player to score in the Premier League, the FA Cup and the FA Youth Cup in the same season in 2007/08 and made a significant contribution for Manchester City in the Premier League in 2008/09, netting four times in 16 appearances while still a teenager.  He made his Premier League debut for Chelsea as a substitute against Sunderland in August 2009 and came into his own after Christmas, starting against Birmingham City and grabbing a brace in the FA Cup Third Round tie with Watford.  Sturridge won his first England cap for the U-16s in 2004 and was a regular scorer at all age levels before making his U-21 bow in August 2009.  In January 2011 he moved to Bolton Wanderers on loan from Chelsea, before starring for England in the UEFA European U-21 Championship in Denmark in which he was named in the team of the tournament.  He returned to Stamford Bridge for the start of the 2010/11 season and put in some impressive displays which caught the eye of Fabio Capello, who duly called Sturridge up to the senior squad for the first time for the double-header with Spain and Sweden, making his debut against the latter.  In 2012, Sturridge was part of Pearce's Team GB squad in the London 2012 Olympic Games before making a switch north to Liverpool in the January transfer window of 2013. Two months later he scored his first goal for England in an 8-0 win in San Marino during the qualifiers for Brazil 2014.  ",
      "birth_date": "1989-09-01",
      "clubname": "Liverpool FC",
      "first_international_appearance": "England - Sweden 15 Nov 2011",
      "full_name": "Daniel Sturridge",
      "goals": 5,
      "height": 179,
      "id": 1,
      "international_caps": 15,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/England/Daniel_STURRIDGE.png",
      "position": "Forward",
      "resource_uri": "/api/players/Daniel%20Sturridge/",
      "shirt_number": 9,
      "sur_name": "Sturridge",
      "twitter_name": "D_Sturridge"
    },
    {
      "biography": "\\r\\nWhat was hugely impressive, however, was the fact that, in a matter of months, the attacking midfielder went from promising youngster to pulling the strings for the senior . That progression can be traced back to the FIFA U-20 World Cup Colombia 2011, when Oscar struck all three goals in the 3-2 final win over Portugal, which led to him earning his first call-ups for the full national squad.  By no means overwhelmed, Oscar adapted seamlessly to life at the top and underlined his knack of performing on the big occasion. “If I’ve been able to show I’m capable of being  No10, I know that it’s something I started over there, in Colombia,” he told  during the Olympic Football Tournament London 2012, where he starred in Brazil’s run to silver.  Nor did Oscar feel out of place when joining up with Chelsea in summer 2012, shortly after the club’s triumph in the UEFA Champions League. Indeed, his first competitive game for the Blues came in September that year in that very competition, when he scored twice in a 2-2 draw with Juventus. ",
      "birth_date": "1991-09-09",
      "clubname": "Chelsea FC",
      "first_international_appearance": "Argentina - Brazil 14 Sep 2011",
      "full_name": "Oscar",
      "goals": 11,
      "height": 181,
      "id": 2,
      "international_caps": 38,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Brazil/OSCAR.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Oscar/",
      "shirt_number": 11,
      "sur_name": "Dos Santos Emboaba Junior",
      "twitter_name": "TheAcademy"
    },
    {
      "biography": "At just 21 years of age, Ricardo Rodriguez has already established himself as first-choice left back both at Bundesliga club Wolfsburg and in the Swiss national team.\\r\\nWhile his exceptional technique and unbending fighting spirit have been key to his rapid ascent, Rodriguez’s attacking prowess and pinpoint crosses have been equally important.\\r\\nBorn to Spanish-Chilean parents, Rodriguez rose through the ranks in the FC Zurich youth academy but signed a four-and-a-half year deal with Wolfsburg after just two years as a professional.\\r\\nThe defender has yet to appear at a major international tournament at senior level, but was part of the triumphant Swiss side that lifted the FIFA U-17 World Cup title in Nigeria in 2009. Rodriguez, famed as much for the accuracy of his left-foot as for his ponytail, earned his first full cap on 7 October 2011 in a European Championship qualifier against Wales.\\r\\nThe 1.80 metre tall defender was an essential part of Switzerland’s 2014 FIFA World Cup Brazil™ qualifying campaign and played in every fixture bar the final match against Slovenia. Winning silverware in South America may be asking too much of the national side at this stage, but it would be unwise to write them off too soon if, as expected, they reach the knockout rounds. ",
      "birth_date": "1992-08-25",
      "clubname": "VfL Wolfsburg",
      "first_international_appearance": "Wales - Switzerland 07 Oct 2011",
      "full_name": "Ricardo Rodriguez",
      "goals": 0,
      "height": 180,
      "id": 3,
      "international_caps": 25,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Switzerland/Ricardo_RODRIGUEZ.png",
      "position": "Defender",
      "resource_uri": "/api/players/Ricardo%20Rodriguez/",
      "shirt_number": 13,
      "sur_name": "Rodriguez Araya",
      "twitter_name": "RRWWE"
    },
    {
      "biography": "Constant Djakpa has steadily risen to prominence in the German Bundesliga thanks to his pace and range of skills. The 27-year-old can play out wide as a conventional attacking winger, but has usually featured at left-back for his current club Eintracht Frankfurt. Djakpa learned the basics in the youth section at Stella Club in his home town of Abidjan. The agile left-footed player graduated to the senior squad and eventually opted to try his hand in Europe. He joined Sogndal in the Norwegian second division in 2006, before signing for Romanian top-flight outfit Pandurii Targu Jiu a year later. Bayer Leverkusen came calling for the Ivorian in 2008, but after his first season the Rhineland side loaned Djakpa to Hannover. The player finally made the breakthrough in the Bundesliga with the Lower Saxony club, and has been more or less a regular since switching to Frankfurt in 2011. He appeared in Côte d’Ivoire colours at the CAF Africa Cup of Nations 2008 in Ghana. Djakpa, a firm crowd favourite in Frankfurt for his stamina and hard-running determination, is now aiming to bolster his reputation at the 2014 FIFA World Cup Brazil™. ",
      "birth_date": "1986-10-17",
      "clubname": "Eintracht Frankfurt",
      "first_international_appearance": "Qatar - Ivory Coast 21 Nov 2007",
      "full_name": "Constant Djakpa",
      "goals": 0,
      "height": 177,
      "id": 4,
      "international_caps": 6,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/IvoryCoast/Constant_DJAKPA.png",
      "position": "Defender",
      "resource_uri": "/api/players/Constant%20Djakpa/",
      "shirt_number": 18,
      "sur_name": "Djakpa",
      "twitter_name": ""
    },
    {
      "biography": "Barely out of his teenage years and only with a handful of caps for USA, DeAndre Yedlin is very much a star in the making and has risen quickly to take his place in Jurgen Klinsmann\\'s 23-man squad bound for Brazil. A fast-moving defender known as much for his maturity and calm at such a tender age as for his wild and ever-changing hairstyles, the player had an instant impact with hometown side Seattle Sounders in Major League Soccer last term. \\r\\nHe was named an MLS all-star in his debut season, the same year he earned his first cap for USA under coach Jurgen Klinsmann. He is most comfortable playing on the right side of defence and his instincts send him zipping forward at every opportunity, not illogical considering he began his career as an out-and-out attacker. \\r\\nExplosive and exciting though he may be, Yedlin’s lack of experience at international level had many in the US media and fan ranks questioning Klinsmann’s decision to include the Sounders’ burgeoning star. “He’s a huge talent,” said the coach. “It will be interesting to see how he takes to this because, obviously, he doesn’t have the experience like other players have.\" ",
      "birth_date": "1993-07-09",
      "clubname": "Seattle Sounders FC",
      "first_international_appearance": "USA - Korea Republic 01 Feb 2014",
      "full_name": "Deandre Yedlin",
      "goals": 0,
      "height": 175,
      "id": 5,
      "international_caps": 7,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/USA/DeAndre_YEDLIN.png",
      "position": "Defender",
      "resource_uri": "/api/players/Deandre%20Yedlin/",
      "shirt_number": 2,
      "sur_name": "Yedlin",
      "twitter_name": "yedlinny"
    },
    {
      "biography": "Measuring in at 1.87m, Martin Silva is a solid, reliable keeper known for his excellent positioning and commanding presence in the box. Those qualities allowed him to shine at youth level for his country, though his fine performances were not enough to help Uruguay win qualification to the FIFA U-20 World Cup UAE 2003. A youth player at Defensor Sporting, Silva made his debut with   in 2006, quickly establishing his place in the team and playing a vital part in the side that won the league title in 2008 and reached the quarter-finals of the Copa Libertadores in 2007 and 2009. After being called up on several occasions by Oscar Tabarez, Silva earned his first cap in a friendly against Algeria in Algiers in August 2009, a game the Uruguayans lost 1-0. Though he has rarely played for the national team since then, he was a member of the squad that finished fourth at the 2010 FIFA World Cup South Africa™, and won the 2011 Copa America and finished fourth at the FIFA Confederations Cup Brazil 2013. After his success with Olimpia de Paraguay, with whom he won two national championships and reached the final of the Copa Libertadores 2013, Silva moved on to the Vasco da Gama of Brazil, where he is an indisputable starter. ",
      "birth_date": "1983-03-25",
      "clubname": "CR Vasco da Gama",
      "first_international_appearance": "Algeria - Uruguay 12 Aug 2009",
      "full_name": "Martin Silva",
      "goals": 0,
      "height": 187,
      "id": 6,
      "international_caps": 4,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Uruguay/Martin_SILVA.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Martin%20Silva/",
      "shirt_number": 23,
      "sur_name": "Silva Leites",
      "twitter_name": "elflacomsilva"
    },
    {
      "biography": "Daniel Pranjic has enjoyed varied fortunes when it comes to the national team in recent seasons. His international career began brightly: he made his senior debut in November 2004 and then became a familiar face the in the squad, participating at both the 2006 FIFA World Cup™ in Germany and UEFA EURO 2008. However, after publicly criticising the national team’s sporting set-up in 2011, he was banned from the squad by then coach Slaven Bilic. He was recalled by Bilic’s successor Igor Stimac but only featured fleetingly in the early days of Stimac’s tenure, and did not play a single minute of his country’s qualification campaign for the 2014 FIFA World Cup Brazil. That period out in the cold was then ended when new coach Niko Kovac brought him back into the first-team fold for the World Cup play-off against Iceland in November 2013. Pranjic soon repaid his coach’s trust, helping the 1998 FIFA World Cup semi-finalists book their ticket for Brazil. At club level Pranjic’s most notable successes have come with Bayern Munich, with whom he reached two UEFA Champions League finals and won the league title. Previously he had helped Dutch top-tier outfit SC Heerenveen win their domestic cup, before leaving for Germany in 2009, even financing part of the transfer himself. He has also represented Dinamo Zagreb, Sporting Lisbon and Panathinaikos, making him one of Croatia’s most experienced players. Pranjic is able to play on the left side of both attack and defence, as well as in central midfield. ",
      "birth_date": "1981-12-02",
      "clubname": "Panathinaikos FC",
      "first_international_appearance": "Republic of Ireland - Croatia 16 Nov 2004",
      "full_name": "Danijel Pranjic",
      "goals": 0,
      "height": 172,
      "id": 7,
      "international_caps": 52,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Croatia/Danijel_PRANJIC.png",
      "position": "Defender",
      "resource_uri": "/api/players/Danijel%20Pranjic/",
      "shirt_number": 3,
      "sur_name": "Pranjic",
      "twitter_name": "CFDanijel"
    },
    {
      "biography": "In a Germany team that has grabbed headlines for its free-flowing attacking style in recent years, Sami Khedira’s tireless running, defensive expertise and on-field leadership have been crucial to adding steel to the creative talent in the side. The holding midfielder has long been a mainstay in Joachim Low’s preferred starting line-up, which is why news that the Real Madrid star has recovered from a cruciate ligament injury sustained last November and been declared fit in time for the 2014 FIFA World Cup™ has been met with a loud chorus of approval.  \\r\\nEven from an early age it was clear that Khedira, who has a Tunisian father and a German mother, possessed the qualities to succeed at the very top. At the age of eight he joined the renowned Stuttgart academy and won two German youth championships with the Swabians prior to turning professional. He repeated the feat in his debut Bundesliga season in 2006/07, before captaining the Germany U-21 side to the European Championship title in 2009. Khedira, whose younger brother Rani now plays for Stuttgart, moved to Madrid in summer 2010 and went on to win the Spanish league title and the Copa del Rey in subsequent seasons.  \\r\\nKhedira did not need long to establish himself in the Germany set-up but it was at South Africa 2010 that he truly cemented his place in the first team, crowning a series of superb displays at the tournament with the winning goal in the match for third place against Uruguay.  The midfielder, a model professional both on and off the pitch, was among Germany’s best players at UEFA EURO 2012 and started every game as the side swept into the semi-finals, where they were eliminated by Italy. In Brazil he will be aiming to add to an already impressive collection of silverware. ",
      "birth_date": "1987-04-04",
      "clubname": "Real Madrid CF",
      "first_international_appearance": "Germany - South Africa 05 Sep 2009",
      "full_name": "Sami Khedira",
      "goals": 5,
      "height": 189,
      "id": 8,
      "international_caps": 51,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Germany/Sami_KHEDIRA.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Sami%20Khedira/",
      "shirt_number": 6,
      "sur_name": "Khedira",
      "twitter_name": "Sami_Khedira_24"
    },
    {
      "biography": "As one of the most experienced players in Ottmar Hitzfeld’s Switzerland side, 29-year-old defensive rock Philippe Senderos will be a vital component of the Swiss challenge at what will be his third FIFA World Cup™.\\r\\nStanding at 1.89 metres tall and weighing 87 kilograms, Senderos boasts an unrivalled aerial game while also possessing the physique to deal with more robust attackers. The centre-back’s no-nonsense style is accentuated by his shaved head, which has long been his personal trademark.\\r\\nBorn to Spanish-Serbian parents, Senderos played for FC Servette Geneva as a youngster and made his debut in the Swiss top flight as a 16-year-old, before moving to Arsenal in July 2003. \\r\\nThe towering defender soon became a first team regular under Arsene Wenger and received the honour of being awarded the No6 jersey last worn by club legend Tony Adams in 2002.  Following subsequent stints at AC Milan, Everton and Fulham, Senderos now plies his trade in the Primera Division with Valencia.\\r\\nSenderos has represented Switzerland at international level since 2002, when he captained the U-17s to continental glory in Denmark. Three years later he also wore the captain’s armband in leading his country at the FIFA U-20 World Cup in the Netherlands. \\r\\nA first senior cap arrived on 26 March 2005 in a World Cup qualifier against France and he has since gone on to earn many more, including appearances at the global showdowns in Germany and South Africa.   \\r\\nWhile Senderos may have been restricted to sporadic outings during Brazil 2014 qualifying, he will nevertheless be a central figure in the Swiss team at the tournament thanks to his respected standing within the squad. ",
      "birth_date": "1985-02-14",
      "clubname": "Valencia CF",
      "first_international_appearance": "France - Switzerland 26 Mar 2005",
      "full_name": "Philippe Senderos",
      "goals": 5,
      "height": 190,
      "id": 9,
      "international_caps": 54,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Switzerland/Philippe_SENDEROS.png",
      "position": "Defender",
      "resource_uri": "/api/players/Philippe%20Senderos/",
      "shirt_number": 4,
      "sur_name": "Senderos",
      "twitter_name": "Philsend4"
    },
    {
      "biography": "Fans at Lisbon’s Alvalade Stadium are used to cheering on great idols, and in 2013/14 they witnessed the meteoric rise of a new Sporting and Portugal star, William Carvalho.  Always one step ahead of his peers, William was born in Angola, went to Portugal as a boy and did not waste time in showing he was a footballer of the highest calibre.  After watching him play for minnows Clube Mira Sintra, Benfica tried to sign him, but William was from a family of Sporting supporters so he preferred to bide his time and wait for the green and whites to come calling. And so they did. Aurelio Pereira, the scout who had brought talents such as Luis Figo, Simao Sabrosa, Nani and Cristiano Ronaldo to the Alvalade, presented the club with a new diamond.  In contrast to his illustrious predecessors, it is not on the wings that William shines, and speed is not his number one asset. An imposing physical presence, William is a brilliant holding midfielder, showing calmness and maturity beyond his 22 years.  After a year and a half on loan at Belgian outfit Cercle Brugge, he was a surprise inclusion in Sporting’s first-team squad ahead of the 2013/14 season, but after a handful of matches nobody doubted his ability. He was simply sensational in Leonardo Jardim’s team and also played an important role in helping Portugal win the World Cup play-off. The quality and talent of William Carvalho can now be witnessed on the biggest stage of all, at the 2014 FIFA World Cup Brazil™.  ",
      "birth_date": "1992-04-07",
      "clubname": "Sporting CP",
      "first_international_appearance": "Sweden - Portugal 19 Nov 2013",
      "full_name": "William",
      "goals": 0,
      "height": 185,
      "id": 10,
      "international_caps": 6,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Portugal/WILLIAM.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/William/",
      "shirt_number": 6,
      "sur_name": "Silva Carvalho",
      "twitter_name": "iamwill"
    },
    {
      "biography": "Luis Garrido has risen to prominence in Honduran football thanks to the fierce on-field battling qualities that have earned him the nickname  ('The Beast'). The diminutive defensive midfielder is deceptively quick and is highly effective at breaking up opposition attacks, although some of his best performances have come when fielded on the left, from where he cuts inside onto his stronger right foot to instigate attacks with his pinpoint passing. \\r\\nGarrido made his senior debut at club level for Juticalpa in 2007 and after a string of consistently good displays he moved to Olimpia at the end of the season. After initially struggling to break into the first team he joined Deportivo Savio on loan, but returned in 2011 having gained more experience and he has since established himself at Olimpia, one of the country's biggest clubs. \\r\\nNational team coach Luis Fernando Suarez selected Garrido for international duty for the first time in 2012 and he has been involved ever since. He played almost 1000 minutes across 11 games in Honduras' 2014 FIFA World Cup Brazil™ qualifying campaign, during which he demonstrated he has the ability to shine at his first global showdown. ",
      "birth_date": "1990-11-05",
      "clubname": "CD Olimpia",
      "first_international_appearance": "Panama - Honduras 12 Oct 2012",
      "full_name": "Luis Garrido",
      "goals": 0,
      "height": 170,
      "id": 11,
      "international_caps": 22,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Honduras/Luis_GARRIDO.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Luis%20Garrido/",
      "shirt_number": 19,
      "sur_name": "Garrido",
      "twitter_name": "lgarrido92"
    },
    {
      "biography": "Never one to take his foot off the pedal, Lucas Digne spends the full 90 minutes of every game putting in maximum effort. \"When you play on the wing, you can\\'t allow yourself the slightest easing-off and you constantly have to work hard,\" the left-back told  during the FIFA U-20 World Cup Turkey 2013, which ended with France lifting the trophy. \"My first priority is to defend well, but I also have to do everything I can to help out offensively. That\\'s the job of a modern full-back. The coach gives you instructions, but there\\'s also an element of intuition, knowing when you can get forward and when to hold back so as not to unbalance the team.\"\\r\\nDigne first began learning the nuances of his role with Lille, where he made his Ligue 1 debut in 2011 before signing for Paris Saint-Germain in the summer of 2013. Despite stiff competition from Maxwell at the Parc des Princes, the youngster – who will turn 21 in July – earned promotion to the France side in February this year, when he came on for Patrice Evra against the Netherlands. A fan of Philipp Lahm, he derives much of his ambition to succeed from the example of his older brother, a former Lille youth academy member who had to quit the game after injury. \"He had a lot of quality, but he got injured and couldn\\'t regain his previous level and never got the chance to break into the professional squad,\" said Digne. \"I know that he\\'s now living his dream through me, and that gives me the strength to never admit defeat.\" ",
      "birth_date": "1993-07-20",
      "clubname": "Paris Saint-Germain FC",
      "first_international_appearance": "France - Netherlands 05 Mar 2014",
      "full_name": "Lucas Digne",
      "goals": 0,
      "height": 189,
      "id": 12,
      "international_caps": 3,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/France/Lucas_DIGNE.png",
      "position": "Defender",
      "resource_uri": "/api/players/Lucas%20Digne/",
      "shirt_number": 17,
      "sur_name": "Digne",
      "twitter_name": "LDigne"
    },
    {
      "biography": "Asmir Avdukic is a goalkeeper who boasts ten years of international experience but, contradictably, just a few caps. The reason for this is the presence of Asmir Begovic, Bosnia-Herzegovina’s undisputed first-choice between the sticks, but coach Safet Susic has described the deputy as someone he “wouldn’t hesitate to call upon”.  Avdukic, born in the former Yugoslavia in 1981, began his career with Celik Zenica – the first of six clubs from six Bosnian cities he would defend. Avdukic also played for Kamen Ingrad in the Croatian top tier and on loan at Iranian giants Persepolis. The 6ft 3ins keeper helped the latter reach the last 16 in the AFC Champions League 2012, performing superbly in a 3-0 win over Al-Gharafa in Doha.  Avdukic’s best season in his homeland came when he captained Borac Banja Luka to Bosnian Premier League glory in 2011, keeping an incredible 19 clean sheets in 30 games along the way. He also helped them finish third in 2012/13. ",
      "birth_date": "1981-05-13",
      "clubname": "FK Borac Banja Luka",
      "first_international_appearance": "Bosnia and Herzegovina - Finland 28 Apr 2004",
      "full_name": "Asmir Avdukic",
      "goals": 0,
      "height": 190,
      "id": 13,
      "international_caps": 3,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/BosniaandHerzegovina/Asmir_AVDUKIC.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Asmir%20Avdukic/",
      "shirt_number": 22,
      "sur_name": "Avdukic",
      "twitter_name": ""
    },
    {
      "biography": "The youngest of the Ayew brothers, Jordan (related to Dede and Ibrahim) joined Marseille as a 15-year-old in 2006. The fleet-footed attacker signed a three-year contract with the French club three years later and appeared in his first game shortly after his 18th birthday, marking his debut with a goal. He was then forced to wait over a year before he hit the back of the net again. The goal finally came in a 4-2 victory over Nice, a game in which his brother Dede scored the other three goals for OM.\\r\\nThe son of two-time African Footballer of the Year Abedi Pele, Jordan first played for the Black Stars in September 2010 in a CAF Africa Cup of Nations qualifier. He scored his first goal for his country in a 2014 FIFA World Cup Brazil™ qualifier against Lesotho two years later. After being dropped from the Ghana squad for the Africa Cup of Nations 2013, Ayew informed the country's football officials that he no longer wanted to be considered for international duty, but he changed his mind a few months later. After failing to earn a regular place in the Marseille starting XI, Ayew shipped out on loan to Sochaux at the beginning of this year, hoping to get the match experience necessary to stay in contention for a place in Ghana's World Cup squad. It was a gamble that paid off. ",
      "birth_date": "1991-09-11",
      "clubname": "FC Sochaux-Montb\\u00c3\\u00a9liard",
      "first_international_appearance": "Swaziland - Ghana 05 Sep 2010",
      "full_name": "Jordan Ayew",
      "goals": 5,
      "height": 182,
      "id": 14,
      "international_caps": 16,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Ghana/Jordan_AYEW.png",
      "position": "Forward",
      "resource_uri": "/api/players/Jordan%20Ayew/",
      "shirt_number": 13,
      "sur_name": "Ayew",
      "twitter_name": "AyewAndre"
    },
    {
      "biography": "Joe Hart was born in Shrewsbury and began his professional career with local League club Shrewsbury Town, then in League Two. He appeared in all 46 matches in the 2005/06 season, the Shrews finishing tenth, and impressed Premier League Manchester City enough for them to sign him for the following season.  Still only 19, he featured in just one Premier League match and had spells on loan at Tranmere Rovers and Blackpool. He became more of a regular in the next two seasons, with 26 and 23 appearances respectively, before spending the whole of 2009/10 on loan at Birmingham City, where he blossomed into one of the country’s top ‘keepers.  Joe made his debut for England’s Under-21s as a substitute for Scott Carson in a 2-2 friendly draw against Spain in February 2007, going on to collect 21 caps at that level and start three matches in the UEFA U-21 European Championships Sweden.  Fabio Capello handed him his first senior cap as a substitute for David James in Trinidad and Tobago in June 2008 and since then he has gone from strength to strength, establishing himself as No1 for both Manchester City and England.  Hart won the FA Cup with City in 2011 and was outstanding the following season as Roberto Mancini's side won the Premier League title. He also won the league’s Golden Glove award between 2011 and 2013.  He travelled with England to the 2010 FIFA World Cup™ as third-choice keeper but did not make an appearance; since then however he has played regularly for his country including in all of the Three Lions games at UEFA EURO 2012.  ",
      "birth_date": "1987-04-19",
      "clubname": "Manchester City FC",
      "first_international_appearance": "Trinidad and Tobago - England 01 Jun 2008",
      "full_name": "Joe Hart",
      "goals": 0,
      "height": 191,
      "id": 15,
      "international_caps": 43,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/England/Joe_HART.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Joe%20Hart/",
      "shirt_number": 1,
      "sur_name": "Hart",
      "twitter_name": "_joehart"
    },
    {
      "biography": "Quick, skilful and explosive, with elusive dribbling and cool finishing to boot, not for nothing has attacker Fidel Martinez has been nicknamed ‘the Ecuadorian Neymar’in his homeland. Born in Sucumbios, Martinez began his pro career with Independiente del Valle, before spending a two-year spell at Brazilian outfit Cruzeiro. Then came a switch to Deportivo Quito, where he rose to promenence and played a key role in their 2011 Ecuadorian title win. His performances and eye for goal subsequently earned him a transfer to Mexican side Tijuana where, again, championship victory would come his way. At national-team level, Martinez caught the eye at the 2007 Pan American Games, where he helped Ecuador bring home the gold medal. Two years later he was also part of his country’s squad at the U-20 Sudamericano in 2009. On his senior debut for  in 2008, Martinez notched a goal in a friendly versus Iran, though several more years would pass before he would return to the fold – just in time for the final two 2014 FIFA World Cup Brazil™ qualifiers. And despite only enjoying seven minutes of action, his displays in Ecuador’s build-up friendlies earned him the nod from coach Reinaldo Rueda. ",
      "birth_date": "1990-02-15",
      "clubname": "Club Tijuana",
      "first_international_appearance": "Iran - Ecuador 17 Dec 2008",
      "full_name": "Fidel Martinez",
      "goals": 2,
      "height": 176,
      "id": 16,
      "international_caps": 8,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Ecuador/Fidel_MARTINEZ.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Fidel%20Martinez/",
      "shirt_number": 20,
      "sur_name": "Martinez Tenorio",
      "twitter_name": "FMalegriatrevi7"
    },
    {
      "biography": "Despite making his debut back in 2008, Lazaros Christodoulopoulos has had to wait for his opportunity in the Greece side, having missed out on consecutive tournaments at UEFA EURO 2008, the 2010 FIFA World Cup South Africa™ and EURO 2012. The languid winger with a vicious long-range drive has forged a formidable reputation since moving to Serie A side Bologna in early 2013. He exploded on to the scene in Italy, grabbing a goal on his debut against Fiorentina after coming on as a substitute. He has gone on to establish himself as a key component of squad since joining from Panathinaikos, where he picked up a Greek league and cup double in 2010. Fernando Santos has taken on board the impact Christodoulopoulos has had at club level and played him in every qualifying group game after he grabbed the winner against Lithuania in Vilnius. The Bologna man was on the bench for the play-off games against Romania, but his place in the finals squad gives Santos some much-needed flair to unpick the Colombian, Japanese and Ivorian defences. ",
      "birth_date": "1986-12-19",
      "clubname": "Bologna FC",
      "first_international_appearance": " - ",
      "full_name": "Lazaros Christodoulopoulos",
      "goals": 1,
      "height": 182,
      "id": 17,
      "international_caps": 21,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Greece/Lazaros_CHRISTODOULOPOULOS.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Lazaros%20Christodoulopoulos/",
      "shirt_number": 16,
      "sur_name": "Christodoulopoulos",
      "twitter_name": ""
    },
    {
      "biography": "One of just a few players from Iran’s 2006 FIFA World Cup Germany™ squad to feature in Carlos Queiroz’s side, 31-year-old Andranik Timotian forms ’s experienced core alongside captain Javad Nekonam and Masoud Shojaei. After putting in a series of outstanding performances and helping Iran to Brazil 2014, the midfielder is expected to play a key role as  aim to progress from a hard group which also features Argentina, Bosnia and Herzegovina and Nigeria. Timotian was still with second-division side Aboumoslem when he earned an unexpected call-up to the national team in the run-up to Germany 2006. With his international debut not coming until August 2005 in a friendly against Libya – after Iran had secured a place at Germany 2006, Timotian surprised even his own supporters by making it into Branko Ivankovic’s World Cup squad. Aside from showcasing his talents on the global stage, the midfielder cut an emotional figure as Iran crashed out with a 1-1 draw against Angola in the closing group match. After the final whistle he collapsed on the turf, sobbing wildly and being comforted by coaches – a poignant scene which made him a national hero in the eyes of Iranian fans. Eight years have elapsed but the ex-Bolton Wanderers and Fulham man's aspirations for success have yet to diminish. Having been an integral in qualifying for Brazil 2014, the player is brimming with renewed passion and added confidence heading into his second World Cup.    A defensive midfielder, Timotian is dangerous whenever he surges forward. His attacking prowess was highlighted in last year’s AFC Champions League quarter-final clash when the dynamic player, having seen his corner turned in by a team-mate, unleashed a long-range effort in stoppage-time to seal a decisive 2-1 victory for Esteghlal at Buriram United.  ",
      "birth_date": "1983-03-06",
      "clubname": "Esteghlal Tehran FC",
      "first_international_appearance": "Iran - Libya 24 Aug 2005",
      "full_name": "Andranik Timotian",
      "goals": 8,
      "height": 178,
      "id": 18,
      "international_caps": 81,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Iran/Andranik_TIMOTIAN.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Andranik%20Timotian/",
      "shirt_number": 14,
      "sur_name": "Timotian Samarani",
      "twitter_name": ""
    },
    {
      "biography": "Spotted while performing at a local community centre by former France goalkeeper Dominique Baratelli, Hugo Lloris was invited to join Nice’s youth academy at the tender age of ten. After gradually coming through the ranks, he debuted for the senior team during the 2005/06 season, playing every French League Cup match up to and including ’ ill-fated final against Nancy. The 20-year-old shot-stopper exhibited enough promise during the run to persuade the coaching staff to promote him to the starting line-up the following campaign, leaving Damien Gregorini and Lionel Letizi – both vastly more experienced between the sticks – on the bench.  An excellent all-round ’keeper who is as decisive coming out to claim the ball as he is in one-on-on-ones with on-rushing strikers, Lloris subsequently found himself the subject of interest from major European clubs, including AC Milan and Tottenham Hotspur. He instead chose to commit himself to Lyon, where he was faced with the not insignificant task of succeeding the much-admired Gregory Coupet. His outings with  caught the eye of France coach Raymond Domenech, who handed him his first cap in November 2008, despite Marseille’s Steve Mandanda occupying the No1 position at the time. Lloris’ first ‘victory’ over his rival came at the end of season 2008/09, when he was named Ligue 1 Goalkeeper of the Year ahead of the Marseille player, who had won the award the year before. Continuing to put in exceptional displays while Mandanda was suffering a loss of form, he was confirmed as ’ first-choice custodian ahead of a friendly match with Turkey in June 2009, a role that he fulfils to this day. After a disappointing 2010 FIFA World Cup™ campaign in South Africa, he was assigned the captain’s armband by Laurent Blanc. Blanc’s successor, Didier Deschamps, confirmed Lloris’ incumbent status upon his appointment in July 2012, the same summer that the talented ’keeper chose to export his skills to Tottenham. ",
      "birth_date": "1986-12-26",
      "clubname": "Tottenham Hotspur FC",
      "first_international_appearance": "France - Uruguay 19 Nov 2008",
      "full_name": "Hugo Lloris",
      "goals": 0,
      "height": 188,
      "id": 19,
      "international_caps": 62,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/France/Hugo_LLORIS.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Hugo%20Lloris/",
      "shirt_number": 1,
      "sur_name": "Lloris",
      "twitter_name": "H_Lloris"
    },
    {
      "biography": "Milan Badelj is one of the many Croatian internationals to have been schooled in the Dinamo Zagreb youth system. The 25-year-old was named as the Croatian top flight’s Young Player of the Year in 2009 and won four league championships and a trio of a cup titles between 2009 and 2012, before moving to the Bundesliga with Hamburg in summer later that year. “He’s a playmaker but not a classic No10,” said Frank Arnesen, Hamburg’s sporting director at the time. “He controls the game from deep, is an intelligent player and is a very good passer.” After a difficult teething period, Badelj has now settled in and is eager to showcase his talents in Brazil too. However, given the intense competition for places in Croatia’s midfield, the “diamond from Zagreb”, as the country’s media have dubbed him, will not have it easy. Badelj only featured three times during 2014 FIFA World Cup™ qualifying, although he finished on the winning team each time. ",
      "birth_date": "1989-02-25",
      "clubname": "Hamburger SV",
      "first_international_appearance": "Croatia - Wales 23 May 2010",
      "full_name": "Milan Badelj",
      "goals": 1,
      "height": 186,
      "id": 20,
      "international_caps": 9,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Croatia/Milan_BADELJ.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Milan%20Badelj/",
      "shirt_number": 15,
      "sur_name": "Badelj",
      "twitter_name": "MilanBadelj"
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
            "id": 435,
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
        request = Request(self.url+"api/matches/")
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
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1882674",
              "location": "Arena Pernambuco",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-14",
              "match_num": 6,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/civ_jpn.jpg",
              "resource_uri": "/api/matches/6/",
              "score": "2-1",
              "winner": "Ivory Coast"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1881469",
              "location": "Estadio Castelao",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio Castelao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-14",
              "match_num": 7,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/uru_crc.jpg",
              "resource_uri": "/api/matches/7/",
              "score": "1-3",
              "winner": "Costa Rica"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1882075",
              "location": "Arena Amazonia",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Arena Amazonia+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-14",
              "match_num": 8,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/eng_ita.jpg",
              "resource_uri": "/api/matches/8/",
              "score": "1-2",
              "winner": "Italy"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1883821",
              "location": "Estadio Nacional",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio Nacional+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-15",
              "match_num": 9,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/sui_ecu.jpg",
              "resource_uri": "/api/matches/9/",
              "score": "2-1",
              "winner": "Switzerland"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1884329",
              "location": "Estadio Beira-Rio",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio Beira-Rio+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-15",
              "match_num": 10,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/fra_hon.jpg",
              "resource_uri": "/api/matches/10/",
              "score": "3-0",
              "winner": "France"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1885053",
              "location": "Estadio do Maracana",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio do Maracana+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-15",
              "match_num": 11,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/arg_bih.jpg",
              "resource_uri": "/api/matches/11/",
              "score": "2-1",
              "winner": "Argentina"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1886825",
              "location": "Arena da Baixada",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Arena da Baixada+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-16",
              "match_num": 12,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/irn_nga.jpg",
              "resource_uri": "/api/matches/12/",
              "score": "0-0",
              "winner": "Draw"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1886374",
              "location": "Arena Fonte Nova",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Arena Fonte Nova+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-16",
              "match_num": 13,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ger_por.jpg",
              "resource_uri": "/api/matches/13/",
              "score": "4-0",
              "winner": "Germany"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1887620",
              "location": "Estadio das Dunas",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio das Dunas+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-16",
              "match_num": 14,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/gha_usa.jpg",
              "resource_uri": "/api/matches/14/",
              "score": "1-2",
              "winner": "USA"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1888684",
              "location": "Estadio Mineirao",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio Mineirao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-17",
              "match_num": 15,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bel_alg.jpg",
              "resource_uri": "/api/matches/15/",
              "score": "2-1",
              "winner": "Belgium"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1890294 ",
              "location": "Arena Pantanal",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Arena Pantanal+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-17",
              "match_num": 16,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/rus_kor.jpg",
              "resource_uri": "/api/matches/16/",
              "score": "1-1",
              "winner": "Draw"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1889171 ",
              "location": "Estadio Castelao",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio Castelao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-17",
              "match_num": 17,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bra_mex.jpg",
              "resource_uri": "/api/matches/17/",
              "score": "0-0",
              "winner": "Draw"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1892629 ",
              "location": "Arena Amazonia",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Arena Amazonia+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-18",
              "match_num": 18,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/cmr_cro.jpg",
              "resource_uri": "/api/matches/18/",
              "score": "0-4",
              "winner": "Croatia"
            },
            {
              "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1892188 ",
              "location": "Estadio do Maracana",
              "map_location": "https://www.google.com/maps/embed/v1/place?q=Estadio do Maracana+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
              "match_date": "2014-06-18",
              "match_num": 19,
              "merge_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/esp_chi.jpg",
              "resource_uri": "/api/matches/19/",
              "score": "0-2",
              "winner": "Chile"
            },
            {
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

