from django.test import TestCase
from wc_app.models import *

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
    	country_test_dict1 = {'Brazil': ['BRA', 5]}

        Country.objects.create(country_name="Brazil", country_code=country_test_dict1[0], rank = country_test_dict1[1])
        """Animals that can speak are correctly identified"""
        Country_Brazil = Country.objects.get(country_name="Brazil")
        self.assertEqual(Country_Brazil.country_name, "Brazil")
        self.assertEqual(Country_Brazil.country_code, "BRA")
        self.assertEqual(Country_Brazil.rank, 5)
        

    def test_country_model2(self):
		#Dictionary Key: Country Name
		#Dictionary Value: [Country_code, country_rank]
		country_test_dict2 = {'Brazil': ['BRA', 5], ['Italy': 'ITA',7]}

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
		 s = open("/u/aseal134/Software _Eng/Projects/cs373-idb/world_cup/wc_app.json")
	     country_test_dic = json.load(s)
	     s.close()

	     for country in country_test_dic.keys():
	     	Country.objects.create(country_name=country, country_code=country_test_dic[country][0], rank = country_test_dic[country][1])

	     for current_country in country_test_dic.keys():
	     	temp_country = Country.objects.get(country_name=current_country)
	     	self.assertEqual(temp_country.country_name, current_country)
	    	self.assertEqual(temp_country.country_code, country_test_dic[country][0])
	    	self.assertEqual(temp_country.rank, country_test_dic[country][1])

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
    	player_test_dict1 = {'Andrea Barzagli': ['Barzagli', 'Italy', 'Juventus FC', 'Defender', '1981-05-08']}

    	c1 = Country.objects.get(country_name = player_test_dict1[2])

        Player.objects.create(country=c1, sur_name= player_test_dict1[0],full_name = "Andrea Barzagli" ,clubname = player_test_dict1[2], position = player_test_dict1[3], birth_date =player_test_dict1[4])
        
        player_get = Player.objects.get(full_name = "Andrea Barzagli")
        self.assertEqual(player_get.country, player_test_dict1[2])
        self.assertEqual(player_get.sur_name, player_test_dict1[0])
        self.assertEqual(player_get.full_name, "Andrea Barzagli")
        self.assertEqual(player_get.clubname, player_test_dict1[2])
        self.assertEqual(player_get.position, player_test_dict1[3])
        self.assertEqual(player_get.birth_date, player_test_dict1[4])


        def test_player_model2(self):
    	#Dictionary Key: Player full name
    	#Dictionary Value: [sur_name, country,Clubname,Position,Birthdate]
    	player_test_dict1 = {'Andrea Barzagli': ['Barzagli', 'Italy', 'Juventus FC', 'Defender', '1981-05-08'],'Yoshito Okubo': ['Okubo', 'Japan', 'Kawasaki Frontale', 'Forward', '1982-06-09']}

    	c1 = Country.objects.get(country_name = player_test_dict1["Andrea Barzagli"][2])
    	c2 = Country.objects.get(country_name = player_test_dict1["Yoshito Okubo"][2])

    	player1_name= "Andrea Barzagli"
    	player2_name= "Yoshito Okubo"

        Player.objects.create(country=c1, sur_name= player_test_dict1[player1_name][0],full_name = "Andrea Barzagli" ,clubname = player_test_dict1[player1_name][2], position = player_test_dict1[player1_name][3], birth_date =player_test_dict1[player1_name][4])
        Player.objects.create(country=c2, sur_name= player_test_dict1[player2_name][0],full_name = "Yoshito Okubo" ,clubname = player_test_dict1[player2_name][2], position = player_test_dict1[player2_name][3], birth_date =player_test_dict1[player2_name][4])
        

        player_get = Player.objects.get(full_name = [player1_name])
        self.assertEqual(player_get.country, player_test_dict1[player1_name][2])
        self.assertEqual(player_get.sur_name, player_test_dict1[player1_name][0])
        self.assertEqual(player_get.full_name, player1_name)
        self.assertEqual(player_get.clubname, player_test_dict1[player1_name][2])
        self.assertEqual(player_get.position, player_test_dict1[player1_name][3])
        self.assertEqual(player_get.birth_date, player_test_dict1[player1_name][4])

        
        player_get = Player.objects.get(full_name = player2_name)
        self.assertEqual(player_get.country, player_test_dict1[player2_name][2])
        self.assertEqual(player_get.sur_name, player_test_dict1[player2_name][0])
        self.assertEqual(player_get.full_name, player2_name)
        self.assertEqual(player_get.clubname, player_test_dict1[player2_name][2])
        self.assertEqual(player_get.position, player_test_dict1[player2_name][3])
        self.assertEqual(player_get.birth_date, player_test_dict1[player2_name][4])

        def test_player_model3(self):
			#Dictionary Key: Player full name
			#Dictionary Value: [sur_name, country,Clubname,Position,Birthdate]
			
			player_test_diction = {'Andrea Barzagli': ['Barzagli', 'Italy', 'Juventus FC', 'Defender', '1981-05-08']}

			c1 = Country.objects.get(country_name = player_test_dict1[2])

		    Player.objects.create(country=c1, sur_name= player_test_dict1[0],full_name = "Andrea Barzagli" ,clubname = player_test_dict1[2], position = player_test_dict1[3], birth_date =player_test_dict1[4])
		    
		    player_get = Player.objects.get(full_name = "Andrea Barzagli")
		    self.assertEqual(player_get.country, player_test_dict1[2])
		    self.assertEqual(player_get.sur_name, player_test_dict1[0])
		    self.assertEqual(player_get.full_name, "Andrea Barzagli")
		    self.assertEqual(player_get.clubname, player_test_dict1[2])
		    self.assertEqual(player_get.position, player_test_dict1[3])
		    self.assertEqual(player_get.birth_date, player_test_dict1[4])

