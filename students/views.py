from django.shortcuts import render, render_to_response

def form(request):
    return render(request, 'form.html')