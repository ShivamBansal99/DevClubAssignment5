from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,redirect,get_object_or_404
from .models import Notes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login
import datetime

def index(request):
    current_user = request.user
    latest_notes = current_user.Notes_set.all()
    context = {'latest_notes':latest_notes}
    return render(request, 'notes/js1.htm',context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/notes/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def addnote(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_user = request.user 
            newNote = Notes.objects.create(user=current_user,note=request.POST.get('list'),pub_date=datetime.datetime.now())
            return redirect('/notes/')
        else:
            current_user = request.user
            latest_notes = Notes.objects.select_related().filter(user = current_user)
            context = {'latest_notes':latest_notes}
            return render(request, 'notes/js1.htm',context)
    else:
        return render(request, 'notes/unauth.html')

def removenote(request, note_id):
    noterem = get_object_or_404(Notes, pk = note_id)
    noterem.delete()
    current_user = request.user
    latest_notes = Notes.objects.select_related().filter(user = current_user)
    context = {'latest_notes':latest_notes}
    return render(request, 'notes/js1.htm',context)
