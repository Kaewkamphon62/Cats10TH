from django.shortcuts import render , redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Choice, top10cat, inputcat
from django.contrib import messages
from .forms import inputcatform

# Create your views here.

def welcome(req):
    return render(req, 'myweb/welcome.html')

#################################################################################################################

def myhtml(req):
    return render(req, 'myweb/myhtml.html')

#################################################################################################################

def inputshow(req): 

    if (req.user.is_anonymous == True):
        return redirect("/login")
    else:
        if req.method == 'POST':
            namecat = req.POST.get('namecat')
            detail = req.POST.get('detail')
            imglink = req.POST.get('imglink')
            form = inputcatform(req.POST)

            if form.is_valid():
                a = form.save()
                a.save()
                return redirect("/home")
        else:
            form = inputcatform()
            context = {'form': form}
            return render(req, 'myweb/inputshow.html', context)
        return render(req, 'myweb/inputshow.html')

#################################################################################################################

def home(req):
    showinputcats = inputcat.objects.all()
    showcats = {'showinputcats': showinputcats}
    return render(req, 'myweb/home.html', showcats)

#################################################################################################################

def topcats(req):
    topcats = top10cat.objects.all()
    return render(req, 'myweb/topcats.html' ,{'topcats':topcats})

#################################################################################################################

def login_user(req):

    #เมื่อล็อคอินไม่สำเร็จ
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
            
            #ตรวจสอบชื่อผู้ใช้ที่ไม่มีและรหัสผ่านไม่ถูกต้อง
            user_check = [User.objects.all().filter(username = req.POST.get('username'))]
            str_user_check = str(user_check)
            nouser = '[<QuerySet []>]'

            if str_user_check == nouser:
                messages.info(req, "ชื่อผู้ใช้ไม่มีอยู่ในระบบ",extra_tags='check')
            else:
                messages.info(req, "รหัสผ่านไม่ถูกต้อง",extra_tags='check')

        context = {}
        return render(req, 'myweb/login.html', context)

#################################################################################################################

def logout_user(req):
    logout(req)
    return redirect("/home")

#################################################################################################################

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

            #ตรวจสอบการสมัครให้ตรงตามเงื่อนไข
            user_check = [User.objects.all().filter(username = response.POST.get('username'))]
            str_user_check = str(user_check)
            username_check = '[<QUERYSET []>]'
            

                #รหัสผ่านของคุณต้องมีอักขระอย่างน้อย 8 ตัว 1_1
            if len(password1) < 8 or len(password2) < 8:
                messages.info(response, '!!!', extra_tags='password1_1')
                #รหัสผ่านของคุณต้องไม่เป็นตัวเลขทั้งหมด 1_2
            if password1.isdecimal() == True or password2.isdecimal() == True:                                        #รหัสผ่านของคุณต้องไม่เป็นตัวเลขทั้งหมด
                messages.info(response, '!!!', extra_tags='password1_2')
                #รหัสผ่านต้องเหมือนกันทั้ง 2
            if password1 != password2:
                messages.info(response, 'PASSWORD ไม่ตรงกัน!!!', extra_tags='password2')
                #ตรวจสอบชื่อผู้ใช้ถ้าซ้ำกับในระบบ
            if username_check != str_user_check:
                messages.info(response, 'มีชื่อผู้ใช้นี้มีอยู่ในระบบอยู่แล้ว', extra_tags='username_check')

    context = {'form':form}
    return render(response, "myweb/register.html", {"form":form})

#################################################################################################################

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'myweb/detail.html', { 'question': question, 'choices': choices})

#################################################################################################################

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#################################################################################################################

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#################################################################################################################