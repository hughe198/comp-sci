from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistationForm, login_form
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            auth_account = authenticate(email = email, password = raw_password)
            login(request,auth_account)
            return redirect('home')
        else:
            context['registration_form'] = form
            return render(request,'teacher_signup.html', context)

    else:
        form = RegistationForm()
        context['registration_form'] = form
        return render(request,'teacher_signup.html', context)


def logout_view(request):
    logout(request)
    return redirect("home")

def login_view(request):
    context = {}
    user =  request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = login_form(request.POST)
        if form.is_valid:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email = email, password = password)

            if user:
                login(request, user)
                return redirect("student_home")
    else:
        form = login_form()

    context['login_form'] = form
    return render(request, 'login.html',context)
