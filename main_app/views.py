from curses.ascii import HT
from django.shortcuts import render, redirect

from django.http import HttpResponse
# import model
from .models import Widget
from django.views.generic.edit import CreateView, DeleteView

# define create view
class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'
  success_url = '/'

# Define the home view
def home(request):
  widgets = Widget.objects.all()
  return render(request, 'index.html', {'widgets': widgets})

# define delete
class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'


