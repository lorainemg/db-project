from django.shortcuts import render_to_response, redirect, render

def base(request):
    return redirect(home)

def home(request):
    return render(request, "index.html", {'open': True})

