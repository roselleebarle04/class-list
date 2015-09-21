from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf

from models import Student

def list_students(request):
	student_list = Student.objects.all().filter(is_active=True)
	totaldb = student_list.count()
	return render(request, 'students/home.html', {
		'total_students': totaldb,
		'students': student_list,
	})

def add_student(request):
	if request.method == "POST":
		id_number = request.POST.get('id_number', '')
		first_name = request.POST.get('first_name', '')
		last_name = request.POST.get('last_name','')
		student = Student(id_number=id_number, first_name=first_name, last_name=last_name)
		student.save()
	return HttpResponseRedirect('/')

def update_student(request, student_id):
	student_list = Student.objects.all().filter(is_active=True)
	totaldb = student_list.count()
	student = Student.objects.get(pk=student_id)

	if request.method == "POST":
		id_number = request.POST.get('id_number', '')
		first_name = request.POST.get('first_name', '')
		last_name = request.POST.get('last_name','')
		student.id_number = id_number
		student.first_name = first_name
		student.last_name = last_name
		student.save()
		return HttpResponseRedirect('/')

	return render(request, 'students/update_form.html', {
		'student' : student,
		'total_students': totaldb,
		'student_id' : student_id,
		'students': student_list,
	})

def drop_student(request, student_id):
	student = Student.objects.get(pk=student_id)
	student.is_active = False
	student.save()
	return HttpResponseRedirect('/')