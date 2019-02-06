from django.shortcuts import render_to_response, redirect, render

def base(request):
    "Se llama inicialmente, redirije al usuario a home"
    return redirect(home)

def home(request):
    "Vista que se llama al estar en la página principal"
    return render(request, "Main/index.html", {'open': True})

