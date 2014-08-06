from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from wc_app.models import *
# Create your views here.
from django.http import HttpResponse
from itertools import chain
import string

import watson
import re

def splitParagraph(paragraph):
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList

def search(request):
    context = RequestContext(request)
    
    query = ""
    query_words = []
    #if there exist a 'q' property in get and that 'q' has something other than white space assign that value to query
    if ('q' in request.GET) and request.GET['q'].strip():
        query = request.GET['q']
    
    #split query on white space
    query_words = query.split()
    
    #get the resesults using the entire query together
    and_results = watson.search(query, ranking=True)

    for i in and_results:
        print(i.url)
        print(i)

    results = list(and_results)

    #add on each individual result to the and results
    for wd in query_words:
        or_results = list(watson.search(wd, ranking=True))
        for r in or_results:
            if not r in results:
                results.append(r)
    
    snippets = []
    
    
    for i in range(0, len(results)):
        final_sentence = ""

        sentences = splitParagraph(results[i].content)

        #First highlight terms in sentences matching the phrase
        for s in list(sentences):
            if(s.lower().find(query.lower()) != -1):
                sentences.remove(s)
                s = s.lower().replace(query.lower(), "<B class='search_term'>"+query.lower()+"</B>")
                final_sentence += "..." + s
                break

        #Then highlight the separate words of a query separately
        for q_wd in query_words:
            for s in list(sentences):
                if (s.lower().find(q_wd.lower()) != -1):
                    sentences.remove(s)
                    s = s.lower().replace(q_wd.lower(), "<B class='search_term'>"+q_wd.lower()+"</B>")
                    final_sentence += "..." + s
                    break

        final_sentence += "..."
        snippets.append(final_sentence)

    zipped = None
    if len(results) > 0:
        zipped = zip(results, snippets)
    length_results = len(results)
    # for i in results:
    #     print(i.url)

    return render_to_response('search.html', {"query": query, "length_results": length_results, "results": zipped}, context)




def home(request):
    context = RequestContext(request)
    return render_to_response('home.html',context)


def countries(request):
    context = RequestContext(request)
    try:
        countries = Country.objects.all().order_by('country_name')
        l = [(x.country_name).replace(' ', '_') for x in countries]
        z = zip(countries, l)
        context_dict = {
            'title': 'Countries',
            'wow_urls' : z
        }
        return render_to_response('countries.html', context_dict, context)
    except:
        return handler404(request)


def country(request, c_name):
    context = RequestContext(request)
    try:
        x = c_name.replace('_',' ')
        # try:
        country = Country.objects.get(country_name=x)

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
            'wow_urls' : z,
            'team_logo_url' : country.team_logo_url,
            'team_video_url' : country.team_video_url,
            'article' : country.article
        }

        # print(country_dict['title'])
        return render_to_response('country.html', country_dict, context)
    except:
        return handler404(request)


def players(request):
    context = RequestContext(request)
    
    try:
        players = Player.objects.all().order_by('country__country_name', 'shirt_number')
        l = []
        l2 = []
        for x in players:
            l += [(x.full_name).replace(' ', '_')]
            l2 += [(x.country.country_name).replace(' ', '_')]

        z = zip(players, l, l2)

        players_dict = {
            'title' : 'Players',
            'wow_urls' : z,
        }
        return render_to_response ('players.html', players_dict, context)
    except:
        return handler404(request)



def player(request, p_name):
    context = RequestContext(request)
    # p_name = p_name
    # print(p_name)
    # print(x)
    try:
        x = p_name.replace('_',' ')

        player = Player.objects.get(full_name = x)
        country_url = (player.country.country_name).replace(' ', '_')
        player_dic = {
            "full_name" : player.full_name,
            "country" : player.country,
            "sur_name" : player.sur_name,
            "clubname" : player.clubname,
            "position" : player.position,
            "birth_date" : player.birth_date, 
            "birth_date" : player.birth_date, 
            "player_image" : player.player_image,
            #
            "international_caps" : player.international_caps,
            "goals" : player.goals,
            "height" : player.height,
            "first_international_appearance" : player.first_international_appearance,
            "biography" : player.biography,
            "c_url" : country_url
        }

        return render_to_response('player.html', player_dic, context)
    except:
        return handler404(request)



def matches(request):
    context = RequestContext(request)

    try:
        matches = Match.objects.all()
        matches_dict = {
            'matches': matches,
        }
        return render_to_response('matches.html',matches_dict,context)
    except:
        return handler404(request)



def match(request, id):
    context = RequestContext(request)

    try:
        match = Match.objects.get(pk=id)
        a = match.country_A.country_name.replace(' ', '_') 
        b = match.country_B.country_name.replace(' ', '_')

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
            "highlight_url" : match.highlight_url,
            "a_url" : a,
            "b_url" : b
        }

        return render_to_response('match.html',match_dic,context)
    except:
        return handler404(request)


def aboutus(request):
    context = RequestContext(request)

    try:
        aboutus_dict = {
            'GDC_location': "https://www.google.com/maps/embed/v1/place?q=Gates-Dell+Complex+Austin+Texas+USA&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ"
        }
        return render_to_response('aboutus.html',aboutus_dict,context)
    except:
        return handler404(request)



#Error 404 page
def handler404(request):
    return render(request, '404.html')

# def test(request):
#     context = RequestContext(request)
#     return render_to_response('test.html',context)
