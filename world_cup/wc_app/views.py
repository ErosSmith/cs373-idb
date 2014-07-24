from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from wc_app.models import *
# Create your views here.
from django.http import HttpResponse
from itertools import chain
import string

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html',context)

def countries(request):
	context = RequestContext(request)

	countries = Country.objects.all().order_by('country_name')
	context_dict = {
		'title': 'Countries',
		'items': countries,
	}
	return render_to_response('countries.html', context_dict, context)


def country(request, c_name):
    context = RequestContext(request)

    # try:
    country = Country.objects.get(country_name=c_name)

    #make the list so that it sort based on specific position they played
    pos_list = ['Goalkeeper', 'Defender', 'Midfielder','Forward']
    # player = Player.objects.all().filter(country = country).order_by('position')
    players = Player.objects.all().filter(country = country)
    g = players.filter(position=pos_list[0]).order_by('shirt_number')
    d = players.filter(position=pos_list[1]).order_by('shirt_number')
    m = players.filter(position=pos_list[2]).order_by('shirt_number')
    f = players.filter(position=pos_list[3]).order_by('shirt_number')

    ordered_players = list(chain(g,d,m,f))
    l = [(x.full_name).replace(' ', '_') for x in ordered_players]
    z = zip(ordered_players, l)
    # print(type(players))
    country_dict = {
    	'country': country.country_name,
        'rank': country.rank,
        "players" : ordered_players,
        "mapurl" : country.map_url,
        'flagurl' : country.flag,
        'wow_urls' : z
    }

    # print(country_dict['title'])

    return render_to_response('country.html', country_dict, context)
    # except:
    #     print("Error 404")


def players(request):
    context = RequestContext(request)
    players = Player.objects.all().order_by('country__country_name', 'shirt_number')
    l = [(x.full_name).replace(' ', '_') for x in players]
    z = zip(players, l)
    players_dict = {
        'title' : 'Players',
        'items': players,
        'wow_urls' : z
    }
    return render_to_response ('players.html', players_dict, context)


def player(request, p_name):
    context = RequestContext(request)
    # p_name = p_name
    print(p_name)
    x = p_name.replace('_',' ')
    print(x)
    player = Player.objects.get(full_name = x)

    player_dic = {
        "full_name" : player.full_name,
        "country" : player.country,
        "sur_name" : player.sur_name,
        "clubname" : player.clubname,
        "position" : player.position,
        "birth_date" : player.birth_date 
    }

    return render_to_response('player.html', player_dic, context)

def matches(request):
    context = RequestContext(request)
    matches = Match.objects.all()
    matches_dict = {
        'matches': matches,
    }
    return render_to_response('matches.html',matches_dict,context)

def match(request, id):
    context = RequestContext(request)

    match = Match.objects.get(pk=id)

    match_dic = {
        "country_A"  : match.country_A,
        "country_B"  : match.country_B,
        "winner"     : match.winner,
        "score"      : match.score,
        "location"   : match.location,
        "match_date" : match.match_date,
        "match_num"  : match.match_num,
        "merge_flag" : match.merge_flag,
        "map_location" : match.map_location,
        "highlight_url" : match.highlight_url
    }


    return render_to_response('match.html',match_dic,context)


def aboutus(request):
    context = RequestContext(request)
    aboutus_dict = {
        'GDC_location': "https://www.google.com/maps/embed/v1/place?q=Gates-Dell+Complex+Austin+Texas+USA&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ"
    }
    return render_to_response('aboutus.html',aboutus_dict,context)


# def test(request):
#     context = RequestContext(request)
#     return render_to_response('test.html',context)