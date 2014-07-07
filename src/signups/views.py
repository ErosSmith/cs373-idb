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
        
    return render_to_response("signup.html",
        locals(),context_instance=RequestContext(request))

def thankyou(request):
    return render_to_response("thankyou.html",
        locals(),context_instance=RequestContext(request))

def aboutus(request):
    return render_to_response("aboutus.html",
        locals(),context_instance=RequestContext(request))

def countries(request):
    return render_to_response("countries.html",
        locals(),context_instance=RequestContext(request))

def players(request):
    return render_to_response("players.html",
        locals(),context_instance=RequestContext(request))

def matches(request):
    return render_to_response("matches.html",
        locals(),context_instance=RequestContext(request))

def brazil(request):
    return render_to_response("brazil.html",
        locals(),context_instance=RequestContext(request))

def argentina(request):
    return render_to_response("argentina.html",
        locals(),context_instance=RequestContext(request))

def germany(request):
    return render_to_response("germany.html",
        locals(),context_instance=RequestContext(request))

def messi(request):
    return render_to_response("messi.html",
        locals(),context_instance=RequestContext(request))

def muller(request):
    return render_to_response("muller.html",
        locals(),context_instance=RequestContext(request))

def neymar(request):
    return render_to_response("neymar.html",
        locals(),context_instance=RequestContext(request))

def bra_ger(request):
    return render_to_response("bra_ger.html",
        locals(),context_instance=RequestContext(request))

def ger_usa(request):
    return render_to_response("ger_usa.html",
        locals(),context_instance=RequestContext(request))

def arg_ned(request):
    return render_to_response("arg_ned.html",
        locals(),context_instance=RequestContext(request))