import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#Views


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def tasks_index(request):
    return render(request, 'tasks/index.html')

@login_required
def tasks_detail(request):
    return render(request, 'tasks/detail.html')

@login_required
def add_photo(request, featured_event_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, featured_event_id=featured_event_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
            return redirect('home')  # Redirect to home in case of error
        else:
            return redirect('home')  # Redirect to home after successful upload
    else:
        return redirect('home')  # Redirect to home if no photo is provided


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
    else:
        form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



# Class'set

class TaskCreate(LoginRequiredMixin ,CreateView):
  model = Task
  fields = ['name', 'description']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin ,UpdateView):
  model = Task
  fields = ['name', 'description']

class TaskDelete(LoginRequiredMixin ,DeleteView):
  model = Task
  success_url = '/tasks/'