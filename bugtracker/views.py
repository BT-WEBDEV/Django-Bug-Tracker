from django.shortcuts import render
from tickets.models import Ticket, Priority

## Home View Severe Bugs 

def home_view(request): 
    tickets = Ticket.objects.filter(
        priorities__name__contains = 'Severe'
    )[:2]
    context = {
        "tickets": tickets
    } 
    return render(request, "index.html", context)