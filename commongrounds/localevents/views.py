from .models import Event, EventSignup
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from accounts.mixins import RoleRequiredMixin, LocalEventsNotLoggedInMixin
from .forms import EventForm, EventUpdateForm, EventSignupForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404


class EventListView(ListView):
    model = Event
    template_name = "events_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_events = Event.objects.all()

        if self.request.user.is_authenticated:
            profile = self.request.user.profile

            created_events = context['created_events'] = all_events.filter(
                organizer=profile)
            signed_up_events = context['signed_up_events'] = all_events.filter(
                event_signup__user_registrant=profile)

            created = [event.pk for event in created_events]
            signed_up = [event.pk for event in signed_up_events]
            all_user_events = created + signed_up
            context["all_events"] = all_events.exclude(pk__in=all_user_events)

        else:
            context["all_events"] = all_events

        return context


class EventDetailView(DetailView):
    model = Event
    template_name = "event.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_events = Event.objects.all()

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            context['signed_up_events'] = all_events.filter(
                event_signup__user_registrant=profile)

        return context

    def post(self, request, *args, **kwargs):
        this_event = self.get_object()

        if not request.user.is_authenticated:
            return redirect('localevents:event_signup', pk=this_event.pk)

        EventSignup.objects.create(
            event=this_event,
            user_registrant=request.user.profile
        )
        this_event.update_status()
        this_event.save()
        return redirect('localevents:event_list')


class EventSignupView(CreateView):  # LocalEventsNotLoggedInMixin,
    model = EventSignup
    form_class = EventSignupForm
    template_name = "event_signup.html"

    def dispatch(self, request, *args, **kwargs):
        self.event_signup = get_object_or_404(
            Event, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        saved_signup = form.save(commit=False)
        saved_signup.event = self.event_signup
        saved_signup.save()
        self.event_signup.save()
        self.event_signup.update_status()
        return redirect('localevents:event_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = self.event_signup
        return context


class EventCreateView(RoleRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "event_create.html"
    success_url = reverse_lazy('localevents:event_list')
    required_role = "Event Organizer"

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial["organizer"] = self.request.user.profile
        return initial

    def form_valid(self, form):
        saved_form = super().form_valid(form)
        self.object.organizer.add(self.request.user.profile)
        return saved_form


class EventUpdateView(RoleRequiredMixin, UpdateView):
    model = Event
    form_class = EventUpdateForm
    template_name = "event_update.html"
    required_role = "Event Organizer"

    def form_valid(self, form):
        event = form.save(commit=False)
        event.update_status()
        event.save()
        return redirect('localevents:event_detail', pk=event.pk)
