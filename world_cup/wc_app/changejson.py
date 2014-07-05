import json
import sys
from wc_apps.models import Country, Player, Match 


def load_json():
    s = open("/home/kimyu92/Desktop/world_cup/wc_app/fifa_player_country.json")
    dic = json.load(s)
    return dic

#makes a dic country as the key and the value is a list of the rank and the country code
def load_country_rank_code(dic):
    country_dic = {}
    count = 0
    for outer_item in dic:
        item = outer_item["teamname"]

        if(item not in country_dic):
            country_dic[item] = outer_item["countrycode"]
            #print(outer_item["countrycode"], end=" ")
            #print(outer_item["teamname"])
            # count+=1


    #print("couint: " + str(count))
    return country_dic

def make_dic_for_model(country_dic):
    for key in country_dic:
        q = Country(country_name = key, country_code = country_dic[key], rank = 0)
        q.save()

#pre process 1st two steps
def run_prog():
    dic = load_json()
    country_dic = load_country_rank_code(dic)
    make_dic_for_model(country_dic)



run_prog()

