from django.contrib import admin
from .models import Event, EventType, EventSignup


class EventInline(admin.TabularInline):
    model = Event


class EventAdmin(admin.ModelAdmin):
    model = Event


class EventTypeAdmin(admin.ModelAdmin):
    model = EventType
    inlines = [EventInline,]


class EventSignupAdmin(admin.ModelAdmin):
    model = EventSignup


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventSignup, EventSignupAdmin)
