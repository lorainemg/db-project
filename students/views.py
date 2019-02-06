from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from students.models import Career, Turn, Student, Secretary #, AssignTurn
from django import forms
from students.forms import Form
import datetime

def form(request):
	"Vista que se usa para crear el formulario."
	turn = Turn.objects.filter(assign=False)
	# Se le envia al template: todas las carreras para que las muestre y los turnos disponibles.
	return render(request, 'Main/form.html', {'careers': Career.objects.all(), 'turn': turn})

def turns(request):
	"""
	Vista que se usa al aceptar el formulario del estudiante, por lo que se guardan sus datos 
	y luego se muestra el template para que elija los turnos disponibles.
	"""
	# if request.method == 'POST': 
		# data = Form(rturnequest.POST)
		# if data.is_valid():
			# _save_student(data.cleaned_data, data)
	avalaible_turns = Turn.objects.filter(assign=False).order_by('date', 'time', 'secretary')
	return render(request, 'Main/turns.html', {'turns': avalaible_turns})
		# else:
		#  	return render(request, 'Main/form.html', {'careers': Career.objects.all(), 'form': data})
 

def _save_student(cl_data, data):
	"""
	Obtiene los datos del formulario, crea un nuevo objeto estudiante y 
	lo salva en la BD.
	"""
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
	"""
	Vista que se llama al salvar la fecha seleccionada por el estudiante.
	"""
	if request.method == 'POST' and 'turn' in request.POST: 
		idx = int(request.POST['turn']) - 1
		av_turns = Turn.objects.filter(assign=False).order_by('date', 'time', 'secretary')
		turn = av_turns[idx]
		turn.assign = True
		turn.save()
		return HttpResponseRedirect('/home/')
	return HttpResponseRedirect('/turn/')


def declaration(request):
	"Vista llamada para acceder al formulario de la declaración jurada."
	return render(request, 'Main/declaration.html')


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