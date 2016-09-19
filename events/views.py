from django.shortcuts import render, get_object_or_404
from django.forms import ModelChoiceField
from django.http import HttpResponse
from .models import *


def index(request):
    events = Event.objects.all()
    sport_group_form = ModelChoiceField(queryset=SportGroup.objects.all())
    context = {
        'events': events,
        'sport_group_form': sport_group_form
    }
    return render(request, 'events/index.html', context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/detail.html', {'event': event})

