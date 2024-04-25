#Import
import uuid
import boto3
import os
import urllib.request
import json

# From | import
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Task, Photo, FeaturedEvent
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#HTML PAGES
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def featured_event(request):
    featured_events = FeaturedEvent.objects.filter()
    return render(request, 'main_app/featuredevent.html')

#TASKS
@login_required
def tasks_index(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def tasks_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    id_list = task.featuredevents.all().values_list('id')
    featuredevents_task_doesnt_have = FeaturedEvent.objects.exclude(id__in=id_list)
    return render(request, 'tasks/detail.html', {'task': task, 'featuredevents': featuredevents_task_doesnt_have})

#ADD PHOTO
@login_required
def add_photo(request, task_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, task_id=task_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', task_id=task_id)  # Redirect to home if no photo is provided

#SIGN UP

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if user is already logged in
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# FEATURED EVENTS

@login_required
def assoc_featuredevent(request, task_id, featuredevent_id):
  Task.objects.get(id=task_id).featuredevents.add(featuredevent_id)
  return redirect('detail', task_id=task_id)

@login_required
def remove_featuredevent(request, task_id, featuredevent_id):
  Task.objects.get(id=task_id).featuredevents.remove(featuredevent_id)
  return redirect('detail', task_id=task_id)



# weather api
def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + 
                                        city + '&units=imperial&appid=5fd61e5d5dec55d26bb4982c9cf2f237').read()
        dataList = json.loads(source)
        
        data = {
            "country_code": str(dataList['sys']['country']),
            "temp": str(dataList['main']['temp']) + ' F',
            "humidity": str(dataList['main']['humidity']),
            "main": str(dataList['weather'][0]['main']),
            "wind_speed": str(dataList['wind']['speed']) + ' mph',
        }
        print(data)
    else :
        data = {}
        
    return render(request, "tasks/detail.html", data)

# Class'set
class TaskCreate(LoginRequiredMixin ,CreateView):
    model = Task
    fields = ['name', 'description', 'date', 'time']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin ,UpdateView):
    model = Task
    fields = ['description', 'date', 'time']

class TaskDelete(LoginRequiredMixin ,DeleteView):
    model = Task
    success_url = '/tasks'
    
class FeaturedEventList(LoginRequiredMixin ,ListView):
  model = FeaturedEvent

class FeaturedEventDetail(LoginRequiredMixin ,DetailView):
  model = FeaturedEvent

class FeaturedEventCreate(LoginRequiredMixin ,CreateView):
  model = FeaturedEvent
  fields = ['name', 'description', 'city', 'state']

class FeaturedEventUpdate(LoginRequiredMixin ,UpdateView):
  model = FeaturedEvent
  fields = ['description', 'city', 'state']

class FeaturedEventDelete(LoginRequiredMixin ,DeleteView):
  model = FeaturedEvent
  success_url = '/featuredevents'