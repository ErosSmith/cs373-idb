from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

from .forms import SignUpForm
# Create your views here.
def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request,'Thanks, you have been successfully added!')
        return HttpResponseRedirect('/thank-you/')
        
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))

def thankyou(request):

        
    return render_to_response("thankyou.html",locals(),context_instance=RequestContext(request))

def aboutus(request):

        
    return render_to_response("aboutus.html",locals(),context_instance=RequestContext(request))

def countries(request):

        
    return render_to_response("countries.html",locals(),context_instance=RequestContext(request))

def players(request):

        
    return render_to_response("players.html",locals(),context_instance=RequestContext(request))

def matches(request):

        
    return render_to_response("matches.html",locals(),context_instance=RequestContext(request))