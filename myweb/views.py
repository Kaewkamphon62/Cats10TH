from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Choice

# Create your views here.

def welcome(req):
    return render(req, 'myweb/welcome.html')

def myhtml(req):
    return render(req, 'myweb/myhtml.html')

def home(req):
    return render(req, 'myweb/home.html')

def login_user(req):
    if req.method == 'POST':
        user = User.objects.get(username=req.POST['username'])
        user = authenticate(username=user.username, password=req.POST['password'])
        if user:
            login(req, user)
            return redirect('/home')

        else:
            return render(req, 'myweb/login.html')

    else:
        return render(req, 'myweb/login.html')

def logout_user(req):
    logout(req)
    return redirect("/home")

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = UserCreationForm()
    return render(request, 'myweb/register.html', {'form': form})


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'myweb/detail.html', { 'question': question, 'choices': choices})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)