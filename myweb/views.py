from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def catwelcome(req):
    return render(req, 'myweb/catwelcome.html')

def cathome(req):
    return render(req, 'myweb/cathome.html')

def catcats(req):
    return render(req, 'myweb/catcats.html')

def bootswatch(req):
    return render(req, 'myweb/bs.sketchy.html')

def detail(request, question_id):
    return render(request, 'myweb/detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)