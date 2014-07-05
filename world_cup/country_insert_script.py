# import json
#import sys
# import django
from wc_app.models import *


# def load_json():
#     s = open("/home/kimyu92/Desktop/world_cup/wc_app/fifa_player_country.json")
#     dic = json.load(s)
#     s.close()
#     return dic

# #makes a dic country as the key and the value is a list of the rank and the country code
# def load_country_rank_code(dic):
#     country_dic = {}
#     count = 0
#     for outer_item in dic:
#         item = outer_item["teamname"]

#         if(item not in country_dic):
#             country_dic[item] = outer_item["countrycode"]
#             #print(outer_item["countrycode"], end=" ")
#             #print(outer_item["teamname"])
#             count+=1


#     print("couint: " + str(count))
#     return country_dic

# def make_dic_for_model(country_dic):
# dic = load_json()
# country_dic = load_country_rank_code(dic)
alist = ["AA", "BB"]
adict = {'Brazil': 'BRA', 'Italy': 'ITA', 'USA': 'USA', 'Costa Rica': 'CRC', 'France': 'FRA', 'Argentina': 'ARG', 'Cameroon': 'CMR', 'Nigeria': 'NGA', 'Ecuador': 'ECU', 'Ghana': 'GHA', 'Australia': 'AUS', 'Iran': 'IRN', 'Algeria': 'ALG', 'Korea Republic': 'KOR', 'Germany': 'GER', 'Bosnia and Herzegovina': 'BIH', 'Chile': 'CHI', 'Belgium': 'BEL', 'Spain': 'ESP', 'Netherlands': 'NED', 'Croatia': 'CRO', 'Switzerland': 'SUI', 'Honduras': 'HON', "Côte d'Ivoire": 'CIV', 'Russia': 'RUS', 'England': 'ENG', 'Portugal': 'POR', 'Mexico': 'MEX', 'Uruguay': 'URU', 'Colombia': 'COL', 'Greece': 'GRE', 'Japan': 'JPN'}
for key in adict:
    q = 0
    q =Country(country_name=key, country_code=adict[key], rank = 0)
    q.save()
# save()

