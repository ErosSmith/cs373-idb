# Create your tests here.
import os
import sys
import json
from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse

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
        expected_response = [
    {
      "country_code": "FRA",
      "country_name": "France",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/france.png",
      "id": 1,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=France&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 17,
      "resource_uri": "/api/countries/France/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/france.jpg"
    },
    {
      "country_code": "GER",
      "country_name": "Germany",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/germany.png",
      "id": 2,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Germany&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 2,
      "resource_uri": "/api/countries/Germany/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/germany.jpg"
    },
    {
      "country_code": "MEX",
      "country_name": "Mexico",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/mexico.png",
      "id": 3,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Mexico&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 20,
      "resource_uri": "/api/countries/Mexico/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/mexico.jpg"
    },
    {
      "country_code": "ALG",
      "country_name": "Algeria",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/algeria.png",
      "id": 4,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Algeria&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 22,
      "resource_uri": "/api/countries/Algeria/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/algeria.jpg"
    },
    {
      "country_code": "ENG",
      "country_name": "England",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/england.png",
      "id": 5,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=England&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 10,
      "resource_uri": "/api/countries/England/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/england.jpg"
    },
    {
      "country_code": "ARG",
      "country_name": "Argentina",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/argentina.png",
      "id": 6,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Argentina&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 5,
      "resource_uri": "/api/countries/Argentina/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/argentina.jpg"
    },
    {
      "country_code": "SUI",
      "country_name": "Switzerland",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/switzerland.png",
      "id": 7,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Switzerland&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 6,
      "resource_uri": "/api/countries/Switzerland/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/switzerland.jpg"
    },
    {
      "country_code": "POR",
      "country_name": "Portugal",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/portugal.png",
      "id": 8,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Portugal&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 4,
      "resource_uri": "/api/countries/Portugal/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/portugal.jpg"
    },
    {
      "country_code": "HON",
      "country_name": "Honduras",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/honduras.png",
      "id": 9,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Honduras&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 33,
      "resource_uri": "/api/countries/Honduras/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/honduras.jpg"
    },
    {
      "country_code": "BRA",
      "country_name": "Brazil",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png",
      "id": 10,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 3,
      "resource_uri": "/api/countries/Brazil/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg"
    },
    {
      "country_code": "NGA",
      "country_name": "Nigeria",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/nigeria.png",
      "id": 11,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Nigeria&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 44,
      "resource_uri": "/api/countries/Nigeria/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/nigeria.jpg"
    },
    {
      "country_code": "IRN",
      "country_name": "Iran",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/iran.png",
      "id": 12,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Iran&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 43,
      "resource_uri": "/api/countries/Iran/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/iran.jpg"
    },
    {
      "country_code": "BEL",
      "country_name": "Belgium",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/belgium.png",
      "id": 13,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Belgium&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 11,
      "resource_uri": "/api/countries/Belgium/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/belgium.jpg"
    },
    {
      "country_code": "CRC",
      "country_name": "Costa Rica",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/costa_rica.png",
      "id": 14,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=CostaRica&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 28,
      "resource_uri": "/api/countries/Costa%20Rica/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/costa_rica.jpg"
    },
    {
      "country_code": "ITA",
      "country_name": "Italy",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/italy.png",
      "id": 15,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Italy&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 9,
      "resource_uri": "/api/countries/Italy/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/italy.jpg"
    },
    {
      "country_code": "NED",
      "country_name": "Netherlands",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/netherlands.png",
      "id": 16,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Netherlands&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 15,
      "resource_uri": "/api/countries/Netherlands/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/netherlands.jpg"
    },
    {
      "country_code": "CMR",
      "country_name": "Cameroon",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/cameroon.png",
      "id": 17,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Cameroon&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 52,
      "resource_uri": "/api/countries/Cameroon/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/cameroon.jpg"
    },
    {
      "country_code": "URU",
      "country_name": "Uruguay",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/uruguay.png",
      "id": 18,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Uruguay&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 7,
      "resource_uri": "/api/countries/Uruguay/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/uruguay.jpg"
    },
    {
      "country_code": "GHA",
      "country_name": "Ghana",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ghana.png",
      "id": 19,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Ghana&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 37,
      "resource_uri": "/api/countries/Ghana/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ghana.jpg"
    },
    {
      "country_code": "CIV",
      "country_name": "Ivory Coast",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ivory_coast.png",
      "id": 20,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=IvoryCoast&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 23,
      "resource_uri": "/api/countries/Ivory%20Coast/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ivory_coast.jpg"
    }
  ]

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
        expected_response = {
      "country_code": "CIV",
      "country_name": "Ivory Coast",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ivory_coast.png",
      "id": 20,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=IvoryCoast&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 23,
      "resource_uri": "/api/countries/Ivory%20Coast/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ivory_coast.jpg"
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
        expected_response = [
    {
      "biography": "Although Alex Song is only 26, he is one of the most experienced players in a Cameroonian team loaded with promising stars-in-waiting. The nephew of former Cameroon captain Rigobert Song, the midfielder has represented his country at the FIFA U-17 tournament in Finland in 2003, at the Olympic Football Tournament in 2008 and at the last FIFA World Cup finals in South Africa. He was also ever-present in Cameroon's qualifying campaign, playing in all eight matches as the Indomitable Lions secured a second consecutive appearance on the global stage. ",
      "birth_date": "1987-09-09",
      "clubname": "FC Barcelona",
      "first_international_appearance": "Morocco - Cameroon 15 Nov 2005",
      "full_name": "Alexandre Song",
      "goals": 0,
      "height": 183,
      "id": 1,
      "international_caps": 49,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Cameroon/Alexandre_SONG.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Alexandre%20Song/",
      "shirt_number": 6,
      "sur_name": "Song Bilong"
    },
    {
      "biography": "Schalke defender Atsuto Uchida sets many female football supporters' hearts aflutter, but beneath the handsome exterior is a fiercely determined, attack-minded player who is developing into a world-class right back. Now a regular starter in the Bundesliga, Uchida has also become an integral player for the Samurai Blue under coach Alberto Zaccheroni. ",
      "birth_date": "1988-03-27",
      "clubname": "FC Schalke 04",
      "first_international_appearance": "Japan - Chile 26 Jan 2008",
      "full_name": "Atsuto Uchida",
      "goals": 2,
      "height": 176,
      "id": 2,
      "international_caps": 71,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Japan/Atsuto_UCHIDA.png",
      "position": "Defender",
      "resource_uri": "/api/players/Atsuto%20Uchida/",
      "shirt_number": 2,
      "sur_name": "Uchida"
    },
    {
      "biography": "Ruben Amorim must wish the FIFA World Cup was held every year. In 2010 he was selected by Carlos Queiroz for South Africa after winning the Portuguese Championship with Benfica, and now, ahead of Brazil 2014, he has again got the call after another league triumph for the Eagles.",
      "birth_date": "1985-01-27",
      "clubname": "SL Benfica",
      "first_international_appearance": "Ivory Coast - Portugal 15 Jun 2010",
      "full_name": "Ruben Amorim",
      "goals": 0,
      "height": 180,
      "id": 3,
      "international_caps": 14,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Portugal/Ruben_AMORIM.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Ruben%20Amorim/",
      "shirt_number": 20,
      "sur_name": "Marques Amorim"
    },
    {
      "biography": "Within every squad there are players considered to be among the coach's favourites and Marcelo Diaz is a prime example of that phenomenon. The central midfielder has played a pivotal part in the Chile team ever since Jorge Sampaoli took over as coach at the end of 2012. ",
      "birth_date": "1986-12-30",
      "clubname": "FC Basel",
      "first_international_appearance": "Uruguay - Chile 11 Nov 2011",
      "full_name": "Marcelo Diaz",
      "goals": 1,
      "height": 168,
      "id": 4,
      "international_caps": 25,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Chile/Marcelo_DIAZ.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Marcelo%20Diaz/",
      "shirt_number": 21,
      "sur_name": "Diaz Rojas"
    },
    {
      "biography": "Jozy Altidore is an enigmatic striker. His brawny build and physical power make him a nightmare for defenders with his back to goal, and his ability to hold the ball up and bring teammates into the play is as good as any in the world. While questions have been raised about his commitment and output, Altidore seems to have found his proper rhythm under current ",
      "birth_date": "1989-11-06",
      "clubname": "Sunderland AFC",
      "first_international_appearance": "South Africa - USA 17 Nov 2007",
      "full_name": "Jozy Altidore",
      "goals": 22,
      "height": 185,
      "id": 5,
      "international_caps": 70,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/USA/Jozy_ALTIDORE.png",
      "position": "Forward",
      "resource_uri": "/api/players/Jozy%20Altidore/",
      "shirt_number": 17,
      "sur_name": "Altidore"
    },
    {
      "biography": "Brazil have certainly not struggled for quality in the right-back position, particularly since tireless wide-man Cafu first burst onto the scene. And though the man who captained his country to their record fifth world crown had a cast-iron grip on the role, since he hung up his boots several names have battled it out to make the position their own - with Maicon first-choice at the 2010 FIFA World Cup South Africa. ",
      "birth_date": "1981-07-26",
      "clubname": "AS Roma",
      "first_international_appearance": "Mexico - Brazil 13 Jul 2003",
      "full_name": "Maicon",
      "goals": 7,
      "height": 186,
      "id": 6,
      "international_caps": 75,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Brazil/MAICON.png",
      "position": "Defender",
      "resource_uri": "/api/players/Maicon/",
      "shirt_number": 23,
      "sur_name": "Sisenando"
    },
    {
      "biography": "Left-back Leighton Baines began his career with Wigan Athletic. He was a first-team regular at the DW Stadium for four seasons, two in the second tier and two in the Premier League, before Everton signed him in 2007. ",
      "birth_date": "1984-12-11",
      "clubname": "Everton FC",
      "first_international_appearance": "England - Egypt 03 Mar 2010",
      "full_name": "Leighton Baines",
      "goals": 1,
      "height": 172,
      "id": 7,
      "international_caps": 26,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/England/Leighton_BAINES.png",
      "position": "Defender",
      "resource_uri": "/api/players/Leighton%20Baines/",
      "shirt_number": 3,
      "sur_name": "Baines"
    },
    {
      "biography": "",
      "birth_date": "1992-04-14",
      "clubname": "Coton Sport FC",
      "first_international_appearance": "Cameroon - Paraguay 29 May 2014",
      "full_name": "Loic Feudjou",
      "goals": 0,
      "height": 178,
      "id": 8,
      "international_caps": 2,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Cameroon/Loic_FEUDJOU.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Loic%20Feudjou/",
      "shirt_number": 1,
      "sur_name": "Feudjou Nguegang"
    },
    {
      "biography": "Already a legend of Mexican football, Carlos Salcido has become one of his country's most integral players in recent years. Currently operating as a defensive midfielder, this 33-year-ols has won more than 100 caps for ",
      "birth_date": "1980-04-02",
      "clubname": "Tigres UANL",
      "first_international_appearance": "Trinidad and Tobago - Mexico 08 Sep 2004",
      "full_name": "Carlos Salcido",
      "goals": 10,
      "height": 176,
      "id": 9,
      "international_caps": 122,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Mexico/Carlos_SALCIDO.png",
      "position": "Defender",
      "resource_uri": "/api/players/Carlos%20Salcido/",
      "shirt_number": 3,
      "sur_name": "Salcido Flores"
    },
    {
      "biography": "Another that started his international career at youth level after being plucked from obscurity by Ange Postecoglou during his tenure as U-20 coach. Langerak is a highly accomplished shot-stopper capable of making spectacular saves. Tall and lean in build he is a dedicated and enthusiastic trainer, committed to improving himself. ",
      "birth_date": "1988-08-22",
      "clubname": "Borussia Dortmund",
      "first_international_appearance": "France - Australia 11 Oct 2013",
      "full_name": "Mitch Langerak",
      "goals": 0,
      "height": 191,
      "id": 10,
      "international_caps": 3,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Australia/Mitch_LANGERAK.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Mitch%20Langerak/",
      "shirt_number": 12,
      "sur_name": "Langerak"
    },
    {
      "biography": "Eiji Kawashima has established himself as Japan's first-choice goalkeeper, and his growing reputation for saving penalties in key games could be a valuable asset at the 2014 FIFA World Cup. ",
      "birth_date": "1983-03-20",
      "clubname": "Standard Liege",
      "first_international_appearance": "Japan - Korea DPR 17 Feb 2008",
      "full_name": "Eiji Kawashima",
      "goals": 0,
      "height": 185,
      "id": 11,
      "international_caps": 59,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Japan/Eiji_KAWASHIMA.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Eiji%20Kawashima/",
      "shirt_number": 1,
      "sur_name": "Kawashima"
    },
    {
      "biography": "Kim Changsoo may not have enjoyed an illustrious career since his professional debut ten years ago, but the 28-year-old defender is relishing his finest hour at his current club Kashiwa Reysol. After a short stint at Ulsan Hyundai in 2004, Kim moved to Daejeon Citizen where he began to make a name for himself as a consistent performer on the right flank. But it was not until 2008 that he proved his potential as the fullback established himself with speedy overlapping and accurate deliveries playing with Busan IPark.",
      "birth_date": "1985-09-12",
      "clubname": "Kashiwa Reysol",
      "first_international_appearance": "Syria - Korea Republic 01 Feb 2009",
      "full_name": "Kim Changsoo",
      "goals": 0,
      "height": 179,
      "id": 12,
      "international_caps": 9,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Korea Republic/KIM_Changsoo.png",
      "position": "Defender",
      "resource_uri": "/api/players/Kim%20Changsoo/",
      "shirt_number": 2,
      "sur_name": "Kim"
    },
    {
      "biography": "An international since 1999, the left-footed central defender has reached the world finals at the fourth attempt, having now turned 38 and with a century of caps in sight. Only the legendary duo of Leonel Alvarez and Carlos Valderrama have pulled the ",
      "birth_date": "1976-01-13",
      "clubname": "Atalanta Bergamo",
      "first_international_appearance": "Colombia - Germany 09 Feb 1999",
      "full_name": "Mario Yepes",
      "goals": 6,
      "height": 186,
      "id": 13,
      "international_caps": 102,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Colombia/Mario_YEPES.png",
      "position": "Defender",
      "resource_uri": "/api/players/Mario%20Yepes/",
      "shirt_number": 3,
      "sur_name": "Yepes Diaz"
    },
    {
      "biography": "At 35, Diego Forlan already has his own chapter in Uruguayan football history. He holds the distinction of being Uruguay's most-capped player of all time, and has been an integral part of the set-up throughout the reign of current coach Oscar Tabarez. ",
      "birth_date": "1979-05-19",
      "clubname": "Cerezo Osaka",
      "first_international_appearance": "Saudi Arabia - Uruguay 27 Mar 2002",
      "full_name": "Diego Forlan",
      "goals": 36,
      "height": 181,
      "id": 14,
      "international_caps": 112,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Uruguay/Diego_FORLAN.png",
      "position": "Forward",
      "resource_uri": "/api/players/Diego%20Forlan/",
      "shirt_number": 10,
      "sur_name": "Forlan Corazo"
    },
    {
      "biography": "Having watched Russia's qualification campaign from afar, Maksim Kanunnikov was a surprise late inclusion in Fabio Capello squad for Brazil 2014. The 22-year-old forward had yet to represent his country at senior level when he was named in the Italian's provisional squad in May, doing enough in Russia's subsequent warm-up games to convince Capello to take him to Brazil. ",
      "birth_date": "1991-07-14",
      "clubname": "FK Amkar Perm",
      "first_international_appearance": "Russia - Slovakia 26 May 2014",
      "full_name": "Maksim Kanunnikov",
      "goals": 0,
      "height": 184,
      "id": 15,
      "international_caps": 4,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Russia/Maksim_KANUNNIKOV.png",
      "position": "Forward",
      "resource_uri": "/api/players/Maksim%20Kanunnikov/",
      "shirt_number": 6,
      "sur_name": "Kanunnikov"
    },
    {
      "biography": "Yamoussoukro-born Cheick Ismael Tiote is a rugged, dogged and impressively consistent defensive midfielder. He first made waves in the high levels of European football with Roda JC, while on loan from Anderlecht at the beginning of the 2007-08 season. He had made his debut at the wealthy Belgian side two seasons earlier, at the age of just 19, but it wasn't until his season with Roda and subsequent move to Twente - where he won the Dutch league in 2010 - that he drew serious notice. ",
      "birth_date": "1986-06-21",
      "clubname": "Newcastle United FC",
      "first_international_appearance": "Tunisia - Ivory Coast 12 Aug 2009",
      "full_name": "Ismael Tiote",
      "goals": 1,
      "height": 175,
      "id": 16,
      "international_caps": 46,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/IvoryCoast/Ismael_TIOTE.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Ismael%20Tiote/",
      "shirt_number": 9,
      "sur_name": "Tiote"
    },
    {
      "biography": "Alejandro Bedoya comes from sturdy footballing stock, with both his father and his grandfather having played professionally in their native Colombia. He is a dangerous presence out wide in midfield who gets forward in a flash and is able to serve in dangerous crosses. ",
      "birth_date": "1987-04-29",
      "clubname": "FC Nantes",
      "first_international_appearance": "USA - Honduras 23 Jan 2010",
      "full_name": "Alejandro Bedoya",
      "goals": 1,
      "height": 178,
      "id": 17,
      "international_caps": 31,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/USA/Alejandro_BEDOYA.png",
      "position": "Midfielder",
      "resource_uri": "/api/players/Alejandro%20Bedoya/",
      "shirt_number": 11,
      "sur_name": "Bedoya"
    },
    {
      "biography": "Athletic, quick off his line and adept at dealing with low shots despite his 6'4 frame, Salvatore Sirigu has established himself as the latest understudy to Italy goalkeeper Gianluigi Buffon. Exemplary between the posts for Paris Saint-Germain, the Sardinian has come a long way since starting out at Palermo, where he was nicknamed ",
      "birth_date": "1987-01-12",
      "clubname": "Paris Saint-Germain FC",
      "first_international_appearance": "Italy - Ivory Coast 10 Aug 2010",
      "full_name": "Salvatore Sirigu",
      "goals": 0,
      "height": 190,
      "id": 18,
      "international_caps": 9,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Italy/Salvatore_SIRIGU.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Salvatore%20Sirigu/",
      "shirt_number": 12,
      "sur_name": "Sirigu"
    },
    {
      "biography": "In the national team picture since 2010, Patrick Pemberton has not been able to establish himself as a consistent presence in goal for Costa Rica, but nevertheless he has served admirably for ",
      "birth_date": "1982-04-24",
      "clubname": "LD Alajuelense",
      "first_international_appearance": "Jamaica - Costa Rica 05 Sep 2010",
      "full_name": "Patrick Pemberton",
      "goals": 0,
      "height": 178,
      "id": 19,
      "international_caps": 21,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Costa Rica/Patrick_PEMBERTON.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Patrick%20Pemberton/",
      "shirt_number": 18,
      "sur_name": "Pemberton Bernard"
    },
    {
      "biography": "Though goalkeeping is his trade, one of Camilo Vargas' most memorable performances came when he scored the winning goal for Santa Fe in a 2011 instalment of their rivalry with Millonarios, the oldest derby in Colombian football. Aside from his goalscoring abilities, the 25-year-old custodian possesses lightning reflexes, is as agile as they come and is something of an expert at saving penalties. ",
      "birth_date": "1989-03-09",
      "clubname": "Independiente Santa Fe",
      "first_international_appearance": " - ",
      "full_name": "Camilo Vargas",
      "goals": 0,
      "height": 185,
      "id": 20,
      "international_caps": 0,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Colombia/Camilo_VARGAS.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Camilo%20Vargas/",
      "shirt_number": 12,
      "sur_name": "Vargas Gil"
    }
  ]
        for story in expected_response:
            self.assertTrue(story in response_objects)

    def test_get_player(self) :
        expected_response = {
      "biography": "Though goalkeeping is his trade, one of Camilo Vargas' most memorable performances came when he scored the winning goal for Santa Fe in a 2011 instalment of their rivalry with Millonarios, the oldest derby in Colombian football. Aside from his goalscoring abilities, the 25-year-old custodian possesses lightning reflexes, is as agile as they come and is something of an expert at saving penalties. ",
      "birth_date": "1989-03-09",
      "clubname": "Independiente Santa Fe",
      "first_international_appearance": " - ",
      "full_name": "Camilo Vargas",
      "goals": 0,
      "height": 185,
      "id": 20,
      "international_caps": 0,
      "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Colombia/Camilo_VARGAS.png",
      "position": "Goalkeeper",
      "resource_uri": "/api/players/Camilo%20Vargas/",
      "shirt_number": 12,
      "sur_name": "Vargas Gil"
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1881469",
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1882075",
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1882674",
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1886374",
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1886825",
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1889171 ",
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1890294 ",
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1891625 ",
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1892629 ",
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
      "highlight_url": "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1892629 ",
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

class SearchTests(unittest.TestCase):

    def test_search_1(self):
        query = "brazil"
        
        results = watson.search(query, ranking=True)
        if len(results) > 0:
            self.assertTrue([x.title for x in results] == ['Greek mythology', 'Roman mythology', 'Trojan War', 'Zeus', 'Labours of Hercules', 'Osiris', 'Athena'])



setup_test_environment()
#main()

