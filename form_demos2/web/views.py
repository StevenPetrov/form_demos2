from django.http import HttpResponse
from django.shortcuts import render

from form_demos2.web.forms import TodoCreateForm, PersonCreateForm
from form_demos2.web.models import Person


def index(request):
    if request.method == 'GET':
        form = TodoCreateForm()
    else:
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('All is valid')
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)

def list_persons(request):
    context = {
        'persons': Person.objects.all()
    }

    return render(request, 'list_persons.html', context)

def create_person(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }

    return render(request, 'create_person.html', context)
