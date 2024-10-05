from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm

def login_user(request):
    return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home-page')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Account created for {username}")
            return redirect("home-page")
    else:
        form = UserCreationForm()
        context = {
            "form": form,
            "titulo": "Registro",
            "tituloPagina": "Registro de Usuário",
            "textoBotao": "Registro",
        }
        return render(request, "registration/register.html", context)


def SignUpView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional actions here, like sending a welcome email
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Resenhas/home-page")
    else:
        form = UserCreationForm()
        context = {
            "form": form,
            "titulo": "Registro",
            "tituloPagina": "Registro de Usuário",
            "textoBotao": "Registro",
        }
        return render(request, "registration/login.html", context)