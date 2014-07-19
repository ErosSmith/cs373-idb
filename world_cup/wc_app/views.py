from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from wc_app.models import *
# Create your views here.
from django.http import HttpResponse

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html',context)

def countries(request):
	context = RequestContext(request)

	countries = Country.objects.all()
	context_dict = {
		'title': 'Countries',
		'items': countries,
	}
	return render_to_response('countries.html', context_dict, context)


def country(request, id):
    context = RequestContext(request)

    # try:
    country = Country.objects.get(pk=id)
    player = Player.objects.all().filter(country = country)
    print(country.country_name)
    country_dict = {
    	'country': country.country_name,
        'rank': country.rank,
        "players" : player
    }

    # print(country_dict['title'])

    return render_to_response('country.html', country_dict, context)
    # except:
    #     print("Error 404")

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
    }


    return render_to_response('match.html',match_dic,context)

def test(request):
    context = RequestContext(request)
    return render_to_response('test.html',context)