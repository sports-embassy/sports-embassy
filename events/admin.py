from django.contrib import admin
from .models import *


class EventDateInline(admin.TabularInline):
    model = EventDate
    extra = 3


class EventOnDateInline(admin.TabularInline):
    model = EventOnEventDate
    extra = 3


class EventAdmin(admin.ModelAdmin):
    inlines = [EventOnDateInline]


class EventDateAdmin(admin.ModelAdmin):
    inlines = [EventDateInline]


admin.site.register(EventDate)
admin.site.register(EventOnEventDate)
admin.site.register(Event, EventAdmin)
admin.site.register(SportType)
admin.site.register(SportGroup)
admin.site.register(TargetGroup)
