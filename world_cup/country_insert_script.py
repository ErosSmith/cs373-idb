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
adict = {"Brazil":[  "BRA",3,"https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png","https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/bra.gif",
      "https://www.youtube.com/watch?v=6E_Lav_N-Ho"
   ],
   "Italy":[  
      "ITA",
      9,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/italy.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/italy.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Italy&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/ita.gif",
      "https://www.youtube.com/watch?v=NofTWmHkDg8"
   ],
   "USA":[  
      "USA",
      13,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/usa.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/usa.jpg",
      "https://www.google.com/maps/embed/v1/place?q=USA&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/usa.gif",
      "https://www.youtube.com/watch?v=YJty7rg3eds"
   ],
   "Costa Rica":[  
      "CRC",
      28,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/costa_rica.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/costa_rica.jpg",
      "https://www.google.com/maps/embed/v1/place?q=CostaRica&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/crc.gif",
      "https://www.youtube.com/watch?v=H1R8R0via38"
   ],
   "France":[  
      "FRA",
      17,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/france.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/france.jpg",
      "https://www.google.com/maps/embed/v1/place?q=France&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/fra.gif",
      "https://www.youtube.com/watch?v=pCEvxlHMcDg"
   ],
   "Argentina":[  
      "ARG",
      5,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/argentina.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/argentina.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Argentina&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/arg.gif",
      "https://www.youtube.com/watch?v=MsNLpGHC6MM"
   ],
   "Cameroon":[  
      "CMR",
      52,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/cameroon.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/cameroon.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Cameroon&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/cmr.gif",
      "https://www.youtube.com/watch?v=ygntRxCUqrQ"
   ],
   "Nigeria":[  
      "NGA",
      44,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/nigeria.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/nigeria.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Nigeria&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/nga.gif",
      "https://www.youtube.com/watch?v=fetWGB62rOI"
   ],
   "Ecuador":[  
      "ECU",
      26,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ecuador.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ecuador.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Ecuador&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/ecu.gif",
      "https://www.youtube.com/watch?v=TClfl0PoTzQ"
   ],
   "Ghana":[  
      "GHA",
      37,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ghana.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ghana.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Ghana&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/gha.gif",
      "https://www.youtube.com/watch?v=5zQgjAESpZE"
   ],
   "Australia":[  
      "AUS",
      62,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/australia.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/australia.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Australia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/aus.gif",
      "https://www.youtube.com/watch?v=2gn6VWRWkzY"
   ],
   "Iran":[  
      "IRN",
      43,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/iran.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/iran.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Iran&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/irn.gif",
      "https://www.youtube.com/watch?v=8Ia6ea9fSLA"
   ],
   "Algeria":[  
      "ALG",
      22,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/algeria.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/algeria.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Algeria&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/alg.gif",
      "https://www.youtube.com/watch?v=Yp41xOAY0EE"
   ],
   "Korea Republic":[  
      "KOR",
      57,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/korea.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/korea.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Korea&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/kor.gif",
      "https://www.youtube.com/watch?v=OUkb2-vKFkU"
   ],
   "Germany":[  
      "GER",
      2,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/germany.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/germany.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Germany&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/ger.gif",
      "https://www.youtube.com/watch?v=RoSOGoolFGs"
   ],
   "Bosnia and Herzegovina":[  
      "BIH",
      21,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/bosnia_and_herzegovina.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/bosnia_and_herzegovina.jpg",
      "https://www.google.com/maps/embed/v1/place?q=BosniaandHerzegovina&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/bih.gif",
      "https://www.youtube.com/watch?v=aXp0uMQ9eI4"
   ],
   "Chile":[  
      "CHI",
      14,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/chile.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/chile.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Chile&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/chi.gif",
      "https://www.youtube.com/watch?v=_bnOs1Av5nw"
   ],
   "Belgium":[  
      "BEL",
      11,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/belgium.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/belgium.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Belgium&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/bel.gif",
      "https://www.youtube.com/watch?v=4iBEwofrgLY"
   ],
   "Spain":[  
      "ESP",
      1,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/Spain.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/spain.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Spain&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/esp.gif",
      "https://www.youtube.com/watch?v=p6CtWn89CgU"
   ],
   "Netherlands":[  
      "NED",
      15,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/netherlands.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/netherlands.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Netherlands&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/ned.gif",
      "https://www.youtube.com/watch?v=BJt7Bm_xiRg"
   ],
   "Croatia":[  
      "CRO",
      18,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/croatia.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/croatia.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Croatia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/cro.gif",
      "https://www.youtube.com/watch?v=n_0Yz0-nrSQ"
   ],
   "Switzerland":[  
      "SUI",
      6,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/switzerland.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/switzerland.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Switzerland&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/sui.gif",
      "https://www.youtube.com/watch?v=lIrKW0_gPdY"
   ],
   "Honduras":[  
      "HON",
      33,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/honduras.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/honduras.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Honduras&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/hon.gif",
      "https://www.youtube.com/watch?v=IZsYf0Ov8g0"
   ],
   "Ivory Coast":[  
      "CIV",
      23,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/ivory_coast.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/ivory_coast.jpg",
      "https://www.google.com/maps/embed/v1/place?q=IvoryCoast&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/civ.gif",
      "https://www.youtube.com/watch?v=4mop073orrI"
   ],
   "Russia":[  
      "RUS",
      19,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/russia.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/russia.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Russia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/rus.gif",
      "https://www.youtube.com/watch?v=pNii1Iy02Jc"
   ],
   "England":[  
      "ENG",
      10,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/england.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/england.jpg",
      "https://www.google.com/maps/embed/v1/place?q=England&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/eng.gif",
      "https://www.youtube.com/watch?v=-6q5xn84kGU"
   ],
   "Portugal":[  
      "POR",
      4,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/portugal.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/portugal.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Portugal&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/por.gif",
      "https://www.youtube.com/watch?v=DSyYg_N3zcw"
   ],
   "Mexico":[  
      "MEX",
      20,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/mexico.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/mexico.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Mexico&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/mex.gif",
      "https://www.youtube.com/watch?v=wK2CcP5rSNo"
   ],
   "Uruguay":[  
      "URU",
      7,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/uruguay.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/uruguay.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Uruguay&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/uru.gif",
      "https://www.youtube.com/watch?v=eELyHuqYlsU"
   ],
   "Colombia":[  
      "COL",
      8,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/colombia.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/colombia.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Colombia&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/col.gif",
      "https://www.youtube.com/watch?v=67813ps8cR4"
   ],
   "Greece":[  
      "GRE",
      12,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/greece.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/greece.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Greece&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/gre.gif",
      "https://www.youtube.com/watch?v=C-PRYMOvpSA"
   ],
   "Japan":[  
      "JPN",
      46,
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/japan.png",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/japan.jpg",
      "https://www.google.com/maps/embed/v1/place?q=Japan&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ",
      "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/team_logos/jpn.gif",
      "https://www.youtube.com/watch?v=cR37y8EtLRs"
   ]
}
for key in adict:
    q = 0
    q =Country(country_name=key, country_code=adict[key][0], rank = adict[key][1], flag=adict[key][2], symbol_flag=adict[key][3], map_url=adict[key][4], team_logo_url=adict[key][5], team_video_url=adict[key][6])
    q.save()
# save()

