from django.db.models import Model
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
 

def passcard_info_view(request, passcode):
    employee_passcard = get_object_or_404(Passcard, passcode=passcode)
    employee_visits = Visit.objects.filter(passcard=employee_passcard)
    this_passcard_visits = []

    
    for employee_visit in employee_visits:
        suspicion = visit.is_visit_long()
        difference = visit.get_duration()
        formed_duration = visit.format_duration()
        passcard_visit = {
            'entered_at': employee_visit.entered_at,
            'duration': formed_duration,
            'is_strange': suspicion
            }
        this_passcard_visits.append(passcard_visit)

        
    context = {
        'passcard': employee_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
