from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from wc_app.models import *
# Create your views here.
from django.http import HttpResponse
from itertools import chain

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


def country(request, id):
    context = RequestContext(request)

    # try:
    country = Country.objects.get(pk=id)

    #make the list so that it sort based on specific position they played
    pos_list = ['Goalkeeper', 'Defender', 'Midfielder','Forward']
    # player = Player.objects.all().filter(country = country).order_by('position')
    players = Player.objects.all().filter(country = country)
    g = players.filter(position=pos_list[0]).order_by('shirt_number')
    d = players.filter(position=pos_list[1]).order_by('shirt_number')
    m = players.filter(position=pos_list[2]).order_by('shirt_number')
    f = players.filter(position=pos_list[3]).order_by('shirt_number')

    ordered_players = list(chain(g,d,m,f))
    
    # print(type(players))
    country_dict = {
    	'country': country.country_name,
        'rank': country.rank,
        "players" : ordered_players
    }

    # print(country_dict['title'])

    return render_to_response('country.html', country_dict, context)
    # except:
    #     print("Error 404")


def players(request):
    context = RequestContext(request)
    players = Player.objects.all().order_by('country__country_name', 'shirt_number')
    players_dict = {
        'title' : 'Players',
        'items': players,
    }
    return render_to_response ('players.html', players_dict, context)


def player(request,id):
    context = RequestContext(request)

    player = Player.objects.get(pk=id)

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

def match(request,num):
    context = RequestContext(request)

    match = Match.objects.get(match_num= num)

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

def test(request):
    context = RequestContext(request)
    return render_to_response('test.html',context)