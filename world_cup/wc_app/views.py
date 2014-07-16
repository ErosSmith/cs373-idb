from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from wc_app.models import *
# Create your views here.
from django.http import HttpResponse


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
    print(country.country_name)
    country_dict = {
    	'country': country.country_name,
        'rank': country.rank,
    }

    # print(country_dict['title'])

    return render_to_response('country.html', country_dict, context)
    # except:
    #     print("Error 404")