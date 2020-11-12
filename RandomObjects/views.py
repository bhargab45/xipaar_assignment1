
from django.http import HttpResponse
from django.shortcuts import render
from .models import randomobjects
import random


def index(request):
	objects = list(randomobjects.objects.all())
	recent_story = random.sample(objects,10)
	return render(request, 'index.html', {'objects': objects , 'recent_story':recent_story,})
