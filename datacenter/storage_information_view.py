import datetime
import pytz
from datetime import datetime
from django.utils import timezone
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.db import models


def storage_information_view(request):
    left_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    
    for left_visit in left_visits:
        difference = Visit.get_duration(left_visit)
        formed_duration = Visit.format_duration(left_visit)
        visit_info = {
            'who_entered': left_visit.passcard,
            'entered_at': left_visit.entered_at,
            'duration': formed_duration,
            }
        non_closed_visits.append(visit_info)


    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
