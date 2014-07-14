from django.shortcuts import render
from wc_app import *
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
from django.http import HttpResponse


def countries(request):
	context = RequestContext(request)

	countries = Country.objects.all()
	context_dict = {'title': 'Countries', 'items': countries}
	return render_to_response('countries.html', context_dict, context)