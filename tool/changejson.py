import json
import sys

country_codes = {'NGA': 'Nigeria', 'BEL': 'Belgium', 'NED': 'Netherlands', 'SUI': 'Switzerland', 'CRC': 'Costa Rica', 'CIV': "Côte d'Ivoire", 'KOR': 'Korea Republic', 'COL': 'Colombia', 'GER': 'Germany', 'USA': 'USA', 'BIH': 'Bosnia and Herzegovina', 'ESP': 'Spain', 'POR': 'Portugal', 'CRO': 'Croatia', 'CMR': 'Cameroon', 'ECU': 'Ecuador', 'FRA': 'France', 'ENG': 'England', 'HON': 'Honduras', 'CHI': 'Chile', 'URU': 'Uruguay', 'AUS': 'Australia', 'GRE': 'Greece', 'IRN': 'Iran', 'JPN': 'Japan', 'ALG': 'Algeria', 'ITA': 'Italy', 'ARG': 'Argentina', 'RUS': 'Russia', 'MEX': 'Mexico', 'BRA': 'Brazil', 'GHA': 'Ghana'}

def load_json():
	s = open("fifa_player_country.json")
	dic = json.load(s)
	return dic

def load_matche_date():
	s = open("all_matches_data.json")
	match_data_dic = json.load(s)
	return match_data_dic

#makes a dic country as the key and the value is a list of the rank and the country code
def load_country_rank_code(dic):
	country_dic = {}
	count = 0
	for outer_item in dic:
		item = outer_item["teamname"]

		if(item not in country_dic):
			# print (outer_item["countrycode"])
			 country_dic[outer_item["countrycode"]] = item
			#print(outer_item["countrycode"], end=" ")
			#print(outer_item["teamname"])
	#print(country_dic)
	return country_dic


# webname
# playerletter
# surname
# countrycode
# idclub
# shirtname
# idcupseason
# teamname
# clubname
# idplayer
# birthdate
# idteam
# fieldpos
# webnamealt
# bibnum

#country,  2nd key full name, sur_name, country, clubname, position, birthdate 
def load_player_info(dic):
	player_dic = {}
	count = 0

	for outer_item in dic:
		# if(outer_item["webname"] in player_dic):
			# print(player_dic[outer_item["webname"]])
			# print("counflciting name" + outer_item["webname"])
		# print(outer_item["webname"])

		position = ""

		if(outer_item["fieldpos"] == 1):
			position = "Goalkeeper"
		elif(outer_item["fieldpos"] == 2):
			position = "Defender"
		elif(outer_item["fieldpos"] == 3):
			position = "Midfielder"
		else:
			position = "Forward"


		full_name = change_to_lower_case(outer_item["webname"])
		surname = change_to_lower_case(outer_item["surname"]) 	
		player_dic[full_name] = [surname, outer_item["teamname"], outer_item["clubname"], position, outer_item["birthdate"][0:10]]
		count+=1

	#print("dic size: "+ str(count) +str(len(player_dic.keys())))
	#print("player count: " + str(count))

	#print(player_dic)
	return player_dic

#Items in the data collected
# status
# match_number
# home_team
# away_team
# winner_code
# winner
# away_team_events
# datetime
# location
# home_team_events


# {'country': 'Brazil', 'code': 'BRA', 'goals': 3}
# {'country': 'Croatia', 'code': 'CRO', 'goals': 1}


#key match number : [match_number, home_team, home_team_score, away_team, away_team_score, winner, location, datetime] 
#country a , country b, score of each 
def load_match_info(match_data_dic):
	match_dic = {}
	count = 0
	for outer_item in match_data_dic:

		#add to dic if it finds 
		if(outer_item["status"] == "completed"):
			if(outer_item["home_team"]["code"] in country_codes):
				match_dic[country_codes[outer_item["home_team"]["code"]]+"-"+ country_codes[outer_item["away_team"]["code"]]] = [outer_item["match_number"], 
				country_codes[outer_item["home_team"]["code"]], 
				outer_item["home_team"]["goals"], 
				country_codes[outer_item["away_team"]["code"]], 
				outer_item["away_team"]["goals"], 
				outer_item["winner"], 
				outer_item["location"], 
				outer_item["datetime"][0:10]]
			else:
				assert(1 == 0)
	
	print(match_dic)
	return match_dic

# def make_dic_for_model(country_dic):
# 	for key in country_dic:
# 		q = Country(country_name = key, country_code = country_dic[key], rank = 0)
# 		q.save()

def change_to_lower_case(name):
	fixed_name = ""
	count = 1 
	split_name = name.split()
	for item in split_name:
		chang_name = item.lower()
		upper_name = chang_name[0].upper() + chang_name[1: len(chang_name)]

		if(count == len(split_name)):
			fixed_name+=upper_name
		else: 
			fixed_name=fixed_name + upper_name + " "

		count+=1

	return fixed_name


#pre process 1st two steps
def run_prog():
	dic = load_json()
	#country_dic = load_country_rank_code(dic)
	player_dic = load_player_info(dic)
	#match_data_dic = load_matche_date()
	#load_match_info(match_data_dic)

	print("{", end=" ")
	for player in player_dic:
		print('"' + player + '" :' + str(player_dic[player]) + ',', end=" ")

	print("}", end=" ")

run_prog()

