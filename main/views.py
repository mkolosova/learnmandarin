from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title':'Main page of the site', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is incorrect'


    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        # myuser = authenticate(request)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')

    return render(request, 'main/signup.html')

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "main/index.html", {'fname': fname})

        else:
            messages.error(request, "Incorrect credentials")
            return redirect('home')

    return render(request, 'main/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def hsk1(request):
    return render(request, 'main/hsk1.html')

def hsk2(request):
    return render(request, 'main/hsk2.html')

def hsk3(request):
    return render(request, 'main/hsk3.html')

def hsk4(request):
    return render(request, 'main/hsk4.html')

def hsk5(request):
    return render(request, 'main/hsk5.html')

def hsk6(request):
    return render(request, 'main/hsk6.html')








