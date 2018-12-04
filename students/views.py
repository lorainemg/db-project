from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from students.models import Career, Turn, Student, Secretary #, AssignTurn
from django import forms
from students.forms import Form
import datetime

def form(request):
	turn = Turn.objects.filter(assign=False)
	return render(request, 'Main/form.html', {'careers': Career.objects.all(), 'turn': turn})

def declaration(request):
	return render(request, 'Main/declaration.html')
 
def turns(request):
	print('here')
	if request.method == 'POST': 
		data = Form(request.POST)
		if data.is_valid():
			save_student(data.cleaned_data, data)
			avalaible_turns = Turn.objects.filter(assign=False).order_by('date', 'time', 'secretary')
			return render(request, 'Main/turns.html', {'turns': avalaible_turns})
		else:
		 	return render(request, 'Main/form.html', {'careers': Career.objects.all(), 'form': data})

def save_student(cl_data, data):
	ci = int(cl_data['ci'])
	first_name = cl_data['nombre']
	last_name = cl_data['pApellido'] + ' ' + cl_data['sApellido']
	address = cl_data['calle']
	city = cl_data['prov']
	email =  cl_data['email']
	sex = data.sex[int(cl_data['colorSexo']) - 1][1][0]
	tel = cl_data['tel']
	s = Student(CI=ci, first_name=first_name, last_name=last_name, address=address, 
				city=city, email=email, sex=sex, telephone_number=tel)
	s.save()

def save_turn(request):	
	if request.method == 'POST' and 'turn' in request.POST: 
		idx = int(request.POST['turn']) - 1
		av_turns = Turn.objects.filter(assign=False).order_by('date', 'time', 'secretary')
		turn = av_turns[idx]
		turn.assign = True
		turn.save()
		return HttpResponseRedirect('/home/')
	return HttpResponseRedirect('/turn/')


def confirmation(request):
	if request.method == 'POST': 
		data = Form(request.POST)
		if data.is_valid():
			return HttpResponse(
				data.sex[int(data.cleaned_data['colorSexo']) - 1][1] + " " +
				data.color[int(data.cleaned_data['colorRadio']) - 1][1] + " " +
				data.ocupation[int(data.cleaned_data['ocupacionRadio']) - 1][1] + " " +
				data.vinculo[int(data.cleaned_data['vinculaRadio']) - 1][1] + " " +
				data.sector[int(data.cleaned_data['sectorRadio']) - 1][1])
		else:
			return render(request, 'test.html', {'form': data}) 