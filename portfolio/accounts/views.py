from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as login_user

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('accounts:login')
    form = RegisterForm()
    return render(request, 'register.html', {'form':form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password, "salam 1")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("salam 2")
            login_user(request, user)
            return redirect('core:home')
    form = LoginForm()
    return render(request, 'login.html', {'form':form})