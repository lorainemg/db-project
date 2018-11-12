from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from students.models import Career, Turn, AssignTurn, Student, Secretary
from django import forms
from students.forms import Form
import datetime

def form(request):
	turn = Turn.objects.exclude(pk__in=AssignTurn.objects.all()).order_by('date', 'time')[0]
	return render(request, 'Main/form.html', {'careers': Career.objects.all(), 'turn': turn})

# def find(request): 
#     return render(request, 'find.html') 
 
def turns(request):
	if request.method == 'POST': 
		data = Form(request.POST)
		if data.is_valid():
			save_student(data.cleaned_data, data)
			avalaible_turns = Turn.objects.exclude(pk__in=AssignTurn.objects.all()).order_by('date', 'time')
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
		turn = int(request.POST['turn']) - 1
		av_turns = Turn.objects.exclude(pk__in=AssignTurn.objects.all()).order_by('date', 'time')
		secretary = Secretary.objects.all()[0]
		new_turn = AssignTurn(turn=av_turns[turn], secretary=secretary)
		new_turn.save()
		return HttpResponseRedirect('/home/')
	return HttpResponseRedirect('/form/')

def buscar(request): 
	if request.method == 'POST': 
		#return HttpResponse('post')
		search = name(request.POST)
		if search.is_valid():
			cd = search.cleaned_data
			q = cd['q']
			st = Student.objects.filter(first_name__icontains = q)
			return render(request, 'results.html',  {'students': st, 'query': q})
		else:
			return HttpResponse('post fail')
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		st = Student.objects.filter(first_name__icontains = q)
		return render(request, 'results.html',  {'students': st, 'query': q})
	else: 
		return render(request, 'find.html', {'error': True}) 

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

