
from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def for_view(request):
    context = {}
    context['message'] = "การวนซ้ำใน_Django"

    if request.method == 'POST' and request.POST.get('count') != '':
        number = int(request.POST.get('count'))
        context['count'] = list(range(1, number + 1))
    else:
        context['count'] = list(range(1, 2))

    return render(request, 'for.html', context)


def table_view(request):
    context = {}
    context['message'] = "ตารางสูตรคูณ"

    if request.method == 'POST' and request.POST.get('number') != '':
        number = int(request.POST.get('number'))
        context['number'] = number
        context['table'] = [(i, number * i) for i in range(1, 13)]
    else:
        context['table'] = []
        context['number'] = None

    return render(request, 'table.html', context)

def student(request):
    context = {}
    context['title'] = "รายชื่อนักศึกษา"
    students = models.Student.objects.all()
    context['students'] = students

    return render(request, 'student.html', context)

def subjects(request):
    context = {}
    context['title'] = "รายวิชา"

    subjects = models.Subjects.objects.all()
    context['subjects'] = subjects

    return render(request, 'subject.html', context)