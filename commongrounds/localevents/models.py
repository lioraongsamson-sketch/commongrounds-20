from django.db import models
from django.urls import reverse
from accounts.models import Profile


class EventType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Event Type'
        verbose_name_plural = 'Event Types'
        ordering = ['name']


class Event(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        EventType,
        on_delete=models.SET_NULL,
        null=True,
        related_name='event',
        blank=True,
    )

    organizer = models.ManyToManyField(
        'accounts.Profile',
        related_name='organized_event',
        blank=True,
    )

    event_image = models.ImageField(
        upload_to='images/', default='.media/images/csci_default_img.png')
    description = models.TextField()
    location = models.CharField()
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    event_capacity = models.PositiveIntegerField(null=True)
    STATUS_OPTIONS = [("Available", "Available"), ("Full", "Full"),
                      ("Done", "Done"), ("Cancelled", "Cancelled")]

    status = models.CharField(choices=STATUS_OPTIONS, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('localevents:event_detail', args=[str(self.id)])

    def update_status(self):
        if self.event_signup.count() >= self.event_capacity:
            self.status = 'Full'
        elif self.status == 'Full':
            self.status = 'Available'
        self.save()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-created_on']


class EventSignup(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='event_signup'
    )

    user_registrant = models.ForeignKey(
        'accounts.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user_event_signup',
    )

    new_registrant = models.CharField(blank=True)
