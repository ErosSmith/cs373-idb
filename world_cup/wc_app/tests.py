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
        country_test_dict1 = {"Brazil": ["BRA", 5]}

        Country.objects.create(country_name="Brazil", country_code=country_test_dict1["Brazil"][0], rank = country_test_dict1["Brazil"][1])
 
        Country_Brazil = Country.objects.get(country_name="Brazil")
        self.assertEqual(Country_Brazil.country_name, "Brazil")
        self.assertEqual(Country_Brazil.country_code, "BRA")
        self.assertEqual(Country_Brazil.rank, 5)
        

    def test_country_model2(self):
        #Dictionary Key: Country Name
        #Dictionary Value: [Country_code, country_rank]
        country_test_dict2 = {'Brazil': ['BRA', 5], 'Italy': ['ITA',7]}

        Country.objects.create(country_name="Brazil", country_code=country_test_dict2["Brazil"][0], rank = country_test_dict2["Brazil"][1])
        Country.objects.create(country_name="Italy", country_code=country_test_dict2["Italy"][0], rank = country_test_dict2["Italy"][1])

        #Brazil check      
        Country_Brazil = Country.objects.get(country_name="Brazil")
        self.assertEqual(Country_Brazil.country_name, "Brazil")
        self.assertEqual(Country_Brazil.country_code, "BRA")
        self.assertEqual(Country_Brazil.rank, 5)

        #Italy check       
        Country_Brazil = Country.objects.get(country_name="Italy")
        self.assertEqual(Country_Brazil.country_name, "Italy")
        self.assertEqual(Country_Brazil.country_code, 'ITA')
        self.assertEqual(Country_Brazil.rank, 7)


    def test_country_model3(self):
        ########################################
        #Kim change the file location to your computer thanks
        #########################################
         s = open("wc_app/testing_country_date.json")
         country_test_dic = json.load(s)
         s.close()

         for country in country_test_dic.keys():
            Country.objects.create(country_name=country, country_code=country_test_dic[country][0], rank = country_test_dic[country][1])

         for current_country in country_test_dic.keys():
            temp = Country.objects.get(country_name=current_country)
            self.assertEqual(temp.country_name, current_country)
            self.assertEqual(temp.country_code, country_test_dic[current_country][0])
            self.assertEqual(temp.rank, country_test_dic[current_country][1])

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
        #Dictionary Value: [sur_name, country,Clubname,Position,Birthdate]
        player_test_dict1 = {"Andrea Barzagli": ["Barzagli", "Italy", "Juventus FC", "Defender", "1981-05-08"]}

        Country.objects.create(country_name = player_test_dict1["Andrea Barzagli"][1])
        c1 = Country.objects.create(country_name = player_test_dict1["Andrea Barzagli"][1])

        Player.objects.create(country=c1, sur_name= player_test_dict1["Andrea Barzagli"][0],full_name = "Andrea Barzagli" ,clubname = player_test_dict1["Andrea Barzagli"][2], position = player_test_dict1["Andrea Barzagli"][3], birth_date =player_test_dict1["Andrea Barzagli"][4])
        
        player_get = Player.objects.get(full_name = "Andrea Barzagli")
        self.assertEqual(player_get.country.__str__(), player_test_dict1["Andrea Barzagli"][1])
        self.assertEqual(player_get.sur_name, player_test_dict1["Andrea Barzagli"][0])
        self.assertEqual(player_get.full_name, "Andrea Barzagli")
        self.assertEqual(player_get.clubname, player_test_dict1["Andrea Barzagli"][2])
        self.assertEqual(player_get.position, player_test_dict1["Andrea Barzagli"][3])
        self.assertEqual(player_get.birth_date.__str__(), player_test_dict1["Andrea Barzagli"][4])


    def test_player_model2(self):
        #Dictionary Key: Player full name
        #Dictionary Value: [sur_name, country,Clubname,Position,Birthdate]
        player_test_dict1 = {"Andrea Barzagli": ["Barzagli", "Italy", "Juventus FC", "Defender", "1981-05-08"],"Yoshito Okubo": ["Okubo", "Japan", "Kawasaki Frontale", "Forward", "1982-06-09"]}

        Country.objects.create(country_name = player_test_dict1["Andrea Barzagli"][1])
        Country.objects.create(country_name = player_test_dict1["Yoshito Okubo"][1])

        c1 = Country.objects.get(country_name = player_test_dict1["Andrea Barzagli"][1])
        c2 = Country.objects.get(country_name = player_test_dict1["Yoshito Okubo"][1])

        player1_name= "Andrea Barzagli"
        player2_name= "Yoshito Okubo"

        Player.objects.create(country=c1, sur_name= player_test_dict1[player1_name][0],full_name = "Andrea Barzagli" ,clubname = player_test_dict1[player1_name][2], position = player_test_dict1[player1_name][3], birth_date =player_test_dict1[player1_name][4])
        Player.objects.create(country=c2, sur_name= player_test_dict1[player2_name][0],full_name = "Yoshito Okubo" ,clubname = player_test_dict1[player2_name][2], position = player_test_dict1[player2_name][3], birth_date =player_test_dict1[player2_name][4])
        

        player_get = Player.objects.get(full_name = player1_name)
        self.assertEqual(player_get.country.__str__(), player_test_dict1[player1_name][1])
        self.assertEqual(player_get.sur_name, player_test_dict1[player1_name][0])
        self.assertEqual(player_get.full_name, player1_name)
        self.assertEqual(player_get.clubname, player_test_dict1[player1_name][2])
        self.assertEqual(player_get.position, player_test_dict1[player1_name][3])
        self.assertEqual(player_get.birth_date.__str__(), player_test_dict1[player1_name][4])

        
        player_get = Player.objects.get(full_name = player2_name)
        self.assertEqual(player_get.country.__str__(), player_test_dict1[player2_name][1])
        self.assertEqual(player_get.sur_name, player_test_dict1[player2_name][0])
        self.assertEqual(player_get.full_name, player2_name)
        self.assertEqual(player_get.clubname, player_test_dict1[player2_name][2])
        self.assertEqual(player_get.position, player_test_dict1[player2_name][3])
        self.assertEqual(player_get.birth_date.__str__(), player_test_dict1[player2_name][4])

    def test_player_model3(self):
        #Dictionary Key: Player full name
        #Dictionary Value: [sur_name, country,Clubname,Position,Birthdate]

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
            Player.objects.create(country=c1, sur_name= player_test_diction[player_name][0],full_name = player_name ,clubname = player_test_diction[player_name][2], position = player_test_diction[player_name][3], birth_date =player_test_diction[player_name][4])

        for player_name in player_test_diction.keys():
            player_get = Player.objects.get(full_name = player_name)
            self.assertEqual(player_get.country.__str__(), player_test_diction[player_name][1])
            self.assertEqual(player_get.sur_name, player_test_diction[player_name][0])
            self.assertEqual(player_get.full_name, player_name)
            self.assertEqual(player_get.clubname, player_test_diction[player_name][2])
            self.assertEqual(player_get.position, player_test_diction[player_name][3])
            self.assertEqual(player_get.birth_date.__str__(), player_test_diction[player_name][4])


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
        #Dictionary Value: [Match_Number, HomeTeam, HomeTeamScore,AwayTeam, AwayTeamScore, Winner, Location, date]
        match_test_dict1 = {'Argentina-Belgium': [60, 'Argentina', 1, 'Belgium', 0, 'Argentina', 'Estadio Nacional', '2014-07-05']}

        score_cat = str(match_test_dict1["Argentina-Belgium"][2]) + "-" + str(match_test_dict1["Argentina-Belgium"][4])
                
        Country.objects.create(country_name = "Argentina")
        Country.objects.create(country_name = "Belgium")
        
        Match.objects.create(match_num = match_test_dict1["Argentina-Belgium"][0], country_A = Country.objects.get(country_name = match_test_dict1["Argentina-Belgium"][1]), country_B = Country.objects.get(country_name = match_test_dict1["Argentina-Belgium"][3]), winner = match_test_dict1["Argentina-Belgium"][5], score = score_cat, location = match_test_dict1["Argentina-Belgium"][6], match_date = match_test_dict1["Argentina-Belgium"][7])

        #need to create country objects and add __str__ methods assert equals
        match_get = Match.objects.get(match_num = match_test_dict1["Argentina-Belgium"][0])
        self.assertEqual(match_get.match_num, match_test_dict1["Argentina-Belgium"][0])
        self.assertEqual(match_get.country_A.country_name, match_test_dict1["Argentina-Belgium"][1])
        self.assertEqual(match_get.country_B.country_name, match_test_dict1["Argentina-Belgium"][3])
        self.assertEqual(match_get.winner, match_test_dict1["Argentina-Belgium"][5])
        self.assertEqual(match_get.score, score_cat)
        self.assertEqual(match_get.location, match_test_dict1["Argentina-Belgium"][6])
        self.assertEqual(match_get.match_date.__str__(), match_test_dict1["Argentina-Belgium"][7])

    def test_match_model2(self):
        #Dictionary Key: HomeTeam vs AwayTeam
        #Dictionary Value: [Match_Number, HomeTeam, HomeTeamScore,AwayTeam, AwayTeamScore, Winner, Location, date]
        match_test_dict1 ={'Argentina-Belgium': [60, 'Argentina', 1, 'Belgium', 0, 'Argentina', 'Estadio Nacional', '2014-07-05'], 'Russia-Korea Republic': [16, 'Russia', 1, 'Korea Republic', 1, 'Draw', 'Arena Pantanal', '2014-06-17']}

        Country.objects.create(country_name = "Argentina")
        Country.objects.create(country_name = "Belgium")
        Country.objects.create(country_name = "Russia")
        Country.objects.create(country_name = "Korea Republic")

        score_cat = str(match_test_dict1["Argentina-Belgium"][2]) + "-" + str(match_test_dict1["Argentina-Belgium"][4])
        Match.objects.create(match_num = match_test_dict1["Argentina-Belgium"][0], country_A = Country.objects.get(country_name = match_test_dict1["Argentina-Belgium"][1]), country_B = Country.objects.get(country_name = match_test_dict1["Argentina-Belgium"][3]), winner = match_test_dict1["Argentina-Belgium"][5], score = score_cat, location = match_test_dict1["Argentina-Belgium"][6], match_date = match_test_dict1["Argentina-Belgium"][7])
        
        score_cat2 = str(match_test_dict1["Russia-Korea Republic"][2]) + "-" + str(match_test_dict1["Russia-Korea Republic"][4])
        Match.objects.create(match_num = match_test_dict1["Russia-Korea Republic"][0], country_A = Country.objects.get(country_name = match_test_dict1["Russia-Korea Republic"][1]), country_B = Country.objects.get(country_name = match_test_dict1["Russia-Korea Republic"][3]), winner = match_test_dict1["Russia-Korea Republic"][5], score = score_cat2, location = match_test_dict1["Russia-Korea Republic"][6], match_date = match_test_dict1["Russia-Korea Republic"][7])

        match_get = Match.objects.get(match_num = match_test_dict1["Argentina-Belgium"][0])
        self.assertEqual(match_get.match_num, match_test_dict1["Argentina-Belgium"][0])
        self.assertEqual(match_get.country_A.country_name, match_test_dict1["Argentina-Belgium"][1])
        self.assertEqual(match_get.country_B.country_name, match_test_dict1["Argentina-Belgium"][3])
        self.assertEqual(match_get.winner, match_test_dict1["Argentina-Belgium"][5])
        self.assertEqual(match_get.score, score_cat)
        self.assertEqual(match_get.location, match_test_dict1["Argentina-Belgium"][6])
        self.assertEqual(match_get.match_date.__str__(), match_test_dict1["Argentina-Belgium"][7])

        match_get = Match.objects.get(match_num = match_test_dict1["Russia-Korea Republic"][0])
        self.assertEqual(match_get.match_num, match_test_dict1["Russia-Korea Republic"][0])
        self.assertEqual(match_get.country_A.country_name, match_test_dict1["Russia-Korea Republic"][1])
        self.assertEqual(match_get.country_B.country_name, match_test_dict1["Russia-Korea Republic"][3])
        self.assertEqual(match_get.winner, match_test_dict1["Russia-Korea Republic"][5])
        self.assertEqual(match_get.score, score_cat2)
        self.assertEqual(match_get.location, match_test_dict1["Russia-Korea Republic"][6])
        self.assertEqual(match_get.match_date.__str__(), match_test_dict1["Russia-Korea Republic"][7])

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
            Match.objects.create(match_num = match_test_diction[match_vs][0], country_A = Country.objects.get(country_name = match_test_diction[match_vs][1]), country_B = Country.objects.get(country_name = match_test_diction[match_vs][3]), winner = match_test_diction[match_vs][5], score = score_cat, location = match_test_diction[match_vs][6], match_date = match_test_diction[match_vs][7])
            
        for match_vs in match_test_diction:    
            match_get = Match.objects.get(match_num = match_test_diction[match_vs][0])
            self.assertEqual(match_get.match_num, match_test_diction[match_vs][0])
            self.assertEqual(match_get.country_A.country_name, match_test_diction[match_vs][1])
            self.assertEqual(match_get.country_B.country_name, match_test_diction[match_vs][3])
            self.assertEqual(match_get.winner, match_test_diction[match_vs][5])
            self.assertEqual(match_get.score, str(match_test_diction[match_vs][2]) + "-" + str(match_test_diction[match_vs][4]))
            self.assertEqual(match_get.location, match_test_diction[match_vs][6])
            self.assertEqual(match_get.match_date.__str__(), match_test_diction[match_vs][7])


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
      "country_code": "CIV",
      "country_name": "Ivory Coast",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ivory_coast.png",
      "id": 1,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=IvoryCoast&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 23,
      "resource_uri": "/api/countries/Ivory%20Coast/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ivory_coast.jpg"
    },
    {
      "country_code": "ENG",
      "country_name": "England",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/england.png",
      "id": 2,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=England&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 10,
      "resource_uri": "/api/countries/England/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/england.jpg"
    },
    {
      "country_code": "IRN",
      "country_name": "Iran",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/iran.png",
      "id": 3,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Iran&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 43,
      "resource_uri": "/api/countries/Iran/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/iran.jpg"
    },
    {
      "country_code": "AUS",
      "country_name": "Australia",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/australia.png",
      "id": 4,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Australia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 62,
      "resource_uri": "/api/countries/Australia/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/australia.jpg"
    },
    {
      "country_code": "HON",
      "country_name": "Honduras",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/honduras.png",
      "id": 5,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Honduras&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 33,
      "resource_uri": "/api/countries/Honduras/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/honduras.jpg"
    },
    {
      "country_code": "SUI",
      "country_name": "Switzerland",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/switzerland.png",
      "id": 6,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Switzerland&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 6,
      "resource_uri": "/api/countries/Switzerland/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/switzerland.jpg"
    },
    {
      "country_code": "NED",
      "country_name": "Netherlands",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/netherlands.png",
      "id": 7,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Netherlands&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 15,
      "resource_uri": "/api/countries/Netherlands/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/netherlands.jpg"
    },
    {
      "country_code": "KOR",
      "country_name": "Korea Republic",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/korea.png",
      "id": 8,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Korea&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 57,
      "resource_uri": "/api/countries/Korea%20Republic/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/korea.jpg"
    },
    {
      "country_code": "CMR",
      "country_name": "Cameroon",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/cameroon.png",
      "id": 9,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Cameroon&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 52,
      "resource_uri": "/api/countries/Cameroon/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/cameroon.jpg"
    },
    {
      "country_code": "ESP",
      "country_name": "Spain",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/Spain.png",
      "id": 10,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Spain&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 1,
      "resource_uri": "/api/countries/Spain/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/spain.jpg"
    },
    {
      "country_code": "GER",
      "country_name": "Germany",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/germany.png",
      "id": 11,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Germany&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 2,
      "resource_uri": "/api/countries/Germany/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/germany.jpg"
    },
    {
      "country_code": "ARG",
      "country_name": "Argentina",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/argentina.png",
      "id": 12,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Argentina&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 5,
      "resource_uri": "/api/countries/Argentina/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/argentina.jpg"
    },
    {
      "country_code": "RUS",
      "country_name": "Russia",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/russia.png",
      "id": 13,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Russia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 19,
      "resource_uri": "/api/countries/Russia/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/russia.jpg"
    },
    {
      "country_code": "MEX",
      "country_name": "Mexico",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/mexico.png",
      "id": 14,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Mexico&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 20,
      "resource_uri": "/api/countries/Mexico/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/mexico.jpg"
    },
    {
      "country_code": "ECU",
      "country_name": "Ecuador",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ecuador.png",
      "id": 15,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Ecuador&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 26,
      "resource_uri": "/api/countries/Ecuador/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ecuador.jpg"
    },
    {
      "country_code": "GRE",
      "country_name": "Greece",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/greece.png",
      "id": 16,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Greece&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 12,
      "resource_uri": "/api/countries/Greece/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/greece.jpg"
    },
    {
      "country_code": "CHI",
      "country_name": "Chile",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/chile.png",
      "id": 17,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Chile&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 14,
      "resource_uri": "/api/countries/Chile/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/chile.jpg"
    },
    {
      "country_code": "NGA",
      "country_name": "Nigeria",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/nigeria.png",
      "id": 18,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Nigeria&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 44,
      "resource_uri": "/api/countries/Nigeria/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/nigeria.jpg"
    },
    {
      "country_code": "URU",
      "country_name": "Uruguay",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/uruguay.png",
      "id": 19,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Uruguay&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 7,
      "resource_uri": "/api/countries/Uruguay/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/uruguay.jpg"
    },
    {
      "country_code": "BRA",
      "country_name": "Brazil",
      "flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png",
      "id": 20,
      "map_url": "https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "rank": 3,
      "resource_uri": "/api/countries/Brazil/",
      "symbol_flag": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg"
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
      "id": 1,
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
              "biography": "",
              "birth_date": "1983-07-30",
              "clubname": "Calcio Catania",
              "first_international_appearance": "",
              "full_name": "Mariano Andujar",
              "goals": 0,
              "height": 0,
              "id": 1,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Argentina/Mariano_ANDUJAR.png",
              "position": "Goalkeeper",
              "resource_uri": "/api/players/Mariano%20Andujar/",
              "shirt_number": 21,
              "sur_name": "Andujar"
            },
            {
              "biography": "",
              "birth_date": "1987-06-20",
              "clubname": "Stoke City FC",
              "first_international_appearance": "",
              "full_name": "Asmir Begovic",
              "goals": 0,
              "height": 0,
              "id": 2,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/BosniaandHerzegovina/Asmir_BEGOVIC.png",
              "position": "Goalkeeper",
              "resource_uri": "/api/players/Asmir%20Begovic/",
              "shirt_number": 1,
              "sur_name": "Begovic"
            },
            {
              "biography": "",
              "birth_date": "1985-03-08",
              "clubname": "Gaziantepspor",
              "first_international_appearance": "",
              "full_name": "Haris Medunjanin",
              "goals": 0,
              "height": 0,
              "id": 3,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/BosniaandHerzegovina/Haris_MEDUNJANIN.png",
              "position": "Midfielder",
              "resource_uri": "/api/players/Haris%20Medunjanin/",
              "shirt_number": 18,
              "sur_name": "Medunjanin"
            },
            {
              "biography": "",
              "birth_date": "1992-05-11",
              "clubname": "Atletico Madrid",
              "first_international_appearance": "",
              "full_name": "Thibaut Courtois",
              "goals": 0,
              "height": 0,
              "id": 4,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Belgium/Thibaut_COURTOIS.png",
              "position": "Goalkeeper",
              "resource_uri": "/api/players/Thibaut%20Courtois/",
              "shirt_number": 1,
              "sur_name": "Courtois"
            },
            {
              "biography": "",
              "birth_date": "1992-09-25",
              "clubname": "Swindon Town FC",
              "first_international_appearance": "",
              "full_name": "Massimo Luongo",
              "goals": 0,
              "height": 0,
              "id": 5,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Australia/Massimo_LUONGO.png",
              "position": "Midfielder",
              "resource_uri": "/api/players/Massimo%20Luongo/",
              "shirt_number": 21,
              "sur_name": "Luongo"
            },
            {
              "biography": "",
              "birth_date": "1982-08-17",
              "clubname": "Everton FC",
              "first_international_appearance": "",
              "full_name": "Phil Jagielka",
              "goals": 0,
              "height": 0,
              "id": 6,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/England/Phil_JAGIELKA.png",
              "position": "Defender",
              "resource_uri": "/api/players/Phil%20Jagielka/",
              "shirt_number": 6,
              "sur_name": "Jagielka"
            },
            {
              "biography": "",
              "birth_date": "1988-06-09",
              "clubname": "Borussia Dortmund",
              "first_international_appearance": "",
              "full_name": "Sokratis Papastathopoulos",
              "goals": 0,
              "height": 0,
              "id": 7,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Greece/Sokratis_PAPASTATHOPOULOS.png",
              "position": "Defender",
              "resource_uri": "/api/players/Sokratis%20Papastathopoulos/",
              "shirt_number": 19,
              "sur_name": "Papastathopoulos"
            },
            {
              "biography": "",
              "birth_date": "1980-12-14",
              "clubname": "Trabzonspor",
              "first_international_appearance": "",
              "full_name": "Didier Zokora",
              "goals": 0,
              "height": 0,
              "id": 8,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/IvoryCoast/Didier_ZOKORA.png",
              "position": "Defender",
              "resource_uri": "/api/players/Didier%20Zokora/",
              "shirt_number": 5,
              "sur_name": "Zokora"
            },
            {
              "biography": "",
              "birth_date": "1986-09-27",
              "clubname": "AS Saint-Etienne",
              "first_international_appearance": "",
              "full_name": "Stephane Ruffier",
              "goals": 0,
              "height": 0,
              "id": 9,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/France/Stephane_RUFFIER.png",
              "position": "Goalkeeper",
              "resource_uri": "/api/players/Stephane%20Ruffier/",
              "shirt_number": 16,
              "sur_name": "Ruffier"
            },
            {
              "biography": "",
              "birth_date": "1981-03-10",
              "clubname": "Chelsea FC",
              "first_international_appearance": "",
              "full_name": "Samuel Etoo",
              "goals": 0,
              "height": 0,
              "id": 10,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Cameroon/Samuel_ETOO.png",
              "position": "Forward",
              "resource_uri": "/api/players/Samuel%20Etoo/",
              "shirt_number": 9,
              "sur_name": "Eto'o Fils"
            },
            {
              "biography": "",
              "birth_date": "1990-06-17",
              "clubname": "Liverpool FC",
              "first_international_appearance": "",
              "full_name": "Jordan Henderson",
              "goals": 0,
              "height": 0,
              "id": 11,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/England/Jordan_HENDERSON.png",
              "position": "Midfielder",
              "resource_uri": "/api/players/Jordan%20Henderson/",
              "shirt_number": 14,
              "sur_name": "Henderson"
            },
            {
              "biography": "",
              "birth_date": "1992-04-07",
              "clubname": "Sporting CP",
              "first_international_appearance": "",
              "full_name": "William",
              "goals": 0,
              "height": 0,
              "id": 12,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Portugal/WILLIAM.png",
              "position": "Midfielder",
              "resource_uri": "/api/players/William/",
              "shirt_number": 6,
              "sur_name": "Silva Carvalho"
            },
            {
              "biography": "",
              "birth_date": "1985-08-05",
              "clubname": "Standard Liege",
              "first_international_appearance": "",
              "full_name": "Laurent Ciman",
              "goals": 0,
              "height": 0,
              "id": 13,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Belgium/Laurent_CIMAN.png",
              "position": "Defender",
              "resource_uri": "/api/players/Laurent%20Ciman/",
              "shirt_number": 23,
              "sur_name": "Ciman"
            },
            {
              "biography": "",
              "birth_date": "1988-04-12",
              "clubname": "FC Internazionale",
              "first_international_appearance": "",
              "full_name": "Ricardo Alvarez",
              "goals": 0,
              "height": 0,
              "id": 14,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Argentina/Ricardo_ALVAREZ.png",
              "position": "Midfielder",
              "resource_uri": "/api/players/Ricardo%20Alvarez/",
              "shirt_number": 19,
              "sur_name": "Alvarez"
            },
            {
              "biography": "",
              "birth_date": "1988-05-26",
              "clubname": "ACF Fiorentina",
              "first_international_appearance": "",
              "full_name": "Juan Cuadrado",
              "goals": 0,
              "height": 0,
              "id": 15,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Colombia/Juan_CUADRADO.png",
              "position": "Midfielder",
              "resource_uri": "/api/players/Juan%20Cuadrado/",
              "shirt_number": 11,
              "sur_name": "Cuadrado Bello"
            },
            {
              "biography": "",
              "birth_date": "1990-10-18",
              "clubname": "Standard Liege",
              "first_international_appearance": "",
              "full_name": "Daniel Opare",
              "goals": 0,
              "height": 0,
              "id": 16,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Ghana/Daniel_OPARE.png",
              "position": "Defender",
              "resource_uri": "/api/players/Daniel%20Opare/",
              "shirt_number": 4,
              "sur_name": "Opare"
            },
            {
              "biography": "",
              "birth_date": "1991-01-20",
              "clubname": "Vitesse Arnheim",
              "first_international_appearance": "",
              "full_name": "Alex Ibarra",
              "goals": 0,
              "height": 0,
              "id": 17,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Ecuador/Alex_IBARRA.png",
              "position": "Midfielder",
              "resource_uri": "/api/players/Alex%20Ibarra/",
              "shirt_number": 5,
              "sur_name": "Ibarra Mina"
            },
            {
              "biography": "",
              "birth_date": "1991-03-19",
              "clubname": "FC Dynamo Moscow",
              "first_international_appearance": "",
              "full_name": "Alexander Kokorin",
              "goals": 0,
              "height": 0,
              "id": 18,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Russia/Alexander_KOKORIN.png",
              "position": "Forward",
              "resource_uri": "/api/players/Alexander%20Kokorin/",
              "shirt_number": 9,
              "sur_name": "Kokorin"
            },
            {
              "biography": "",
              "birth_date": "1987-04-22",
              "clubname": "Chelsea FC",
              "first_international_appearance": "",
              "full_name": "John Obi Mikel",
              "goals": 0,
              "height": 0,
              "id": 19,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Nigeria/John_Obi_MIKEL.png",
              "position": "Midfielder",
              "resource_uri": "/api/players/John%20Obi%20Mikel/",
              "shirt_number": 10,
              "sur_name": "Mikel"
            },
            {
              "biography": "",
              "birth_date": "1989-12-31",
              "clubname": "Kuban Krasnodar",
              "first_international_appearance": "",
              "full_name": "Mohammed Rabiu",
              "goals": 0,
              "height": 0,
              "id": 20,
              "international_caps": 0,
              "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Ghana/Mohammed_RABIU.png",
              "position": "Midfielder",
              "resource_uri": "/api/players/Mohammed%20Rabiu/",
              "shirt_number": 17,
              "sur_name": "Rabiu Alhassan"
            }
          ]
        for story in expected_response:
            self.assertTrue(story in response_objects)

    def test_get_player(self) :
        expected_response = {
          "biography": "",
          "birth_date": "1983-07-30",
          "clubname": "Calcio Catania",
          "first_international_appearance": "",
          "full_name": "Mariano Andujar",
          "goals": 0,
          "height": 0,
          "id": 1,
          "international_caps": 0,
          "player_image": "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Argentina/Mariano_ANDUJAR.png",
          "position": "Goalkeeper",
          "resource_uri": "/api/players/Mariano%20Andujar/",
          "shirt_number": 21,
          "sur_name": "Andujar"
        }

        request = Request(self.url+"api/players/Mariano%20Andujar")
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




setup_test_environment()
#main()
