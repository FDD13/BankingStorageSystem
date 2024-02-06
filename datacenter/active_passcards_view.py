from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()


def active_passcards_view(request):
    all_active_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': all_active_passcards,
    }
    print(all_active_passcards)
    return render(request, 'active_passcards.html', context)


