from django.db import models
from datetime import datetime
from django.template import VariableDoesNotExist
from django.utils import timezone
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)     

    
    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


    def get_duration(visit):
        now = timezone.localtime()
        entered_at_time = timezone.localtime(visit.entered_at)
        leaved_at_time = timezone.localtime(visit.leaved_at)
        if visit.leaved_at:
            duration = (leaved_at_time - entered_at_time).total_seconds()
        else:
            duration = (now - entered_at_time).total_seconds()
        return duration
        

    def format_duration(visit):
        difference = visit.get_duration()
        minutes = (difference % 3600) // 60
        hours = difference // 3600
        return f'{hours}:{minutes}'


    def is_visit_long(visit, minutes=60):
        difference = visit.get_duration()
        difference < minutes
        return False
        
