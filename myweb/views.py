from django.shortcuts import render , redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Choice
from django.contrib import messages

# Create your views here.

def welcome(req):
    return render(req, 'myweb/welcome.html')

def myhtml(req):
    return render(req, 'myweb/myhtml.html')

def home(req):
    return render(req, 'myweb/home.html')

def login_user(req):
    if req.user.is_authenticated:
        return redirect('/home')
    else:
        if req.method == 'POST':
            username = req.POST.get('username')
            password = req.POST.get('password')

            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                return redirect('/home')
            else:
                messages.info(req, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')

        context = {}
        return render(req, 'myweb/login.html', context)


def logout_user(req):
    logout(req)
    return redirect("/home")


def register_user(response):
    if response.user.is_authenticated:
        return redirect('/home')

    else: 
        form = RegisterForm()
        if response.method == "POST":
            username = response.POST.get('username')
            email = response.POST.get('email')
            password1 = response.POST.get('password1')
            password2 = response.POST.get('password2')

            form = RegisterForm(response.POST)

            if form.is_valid():
                form.save()

                return redirect("/login")
            
            elif len(password1) < 8 or len(password2) < 8:
                messages.info(response, 'รหัสผ่านของคุณต้องมี 8 ตัวอย่างต่ำ')
                
            elif password1 != password2:
                messages.info(response, 'รหัสผ่านของคุณทั้ง 2 อันต้องเหมือนกัน')
                
            else:
                messages.info(response, 'รหัสผ่านของคุณต้องไม่ใช่ตัวเลขทั้งหมด')
            

    context = {'form':form}
    return render(response, "myweb/register.html", {"form":form})


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'myweb/detail.html', { 'question': question, 'choices': choices})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)