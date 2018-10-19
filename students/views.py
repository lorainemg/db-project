from django.shortcuts import render, render_to_response
from students.models import Career
from django import forms


def form(request):
    return render(request, 'form.html', {'careers': Career.objects.all()})
