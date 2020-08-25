from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket, Comment, Category, Priority
from .forms import CommentForm, TicketForm
from django.http import HttpResponseRedirect


# Create your views here.

##############################################################################3

# NEW TICKET

@login_required(login_url='/accounts/login/')
def new_ticket(request): 
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save()
            ticket.save()
            context = {
                'ticket' : ticket
            }
            return HttpResponseRedirect('/tickets')
        else: 
            form = TicketForm()
    context = {
        "form": form,
    }
    return render(request, 'new_ticket.html', context)

######################################################################

# TICKET INDEX - AN OVERVIEW OF ACTIVE TICKETS

@login_required(login_url='/accounts/login/')
def ticket_index(request):
    tickets = Ticket.objects.filter(
        completed = False
    )
    context = {
        'tickets': tickets
    }
    return render(request, 'ticket_index.html', context)

#####################################################################

# TICKET DETAIL - AN INDEPTH LOOK OF A TICKET 

@login_required(login_url='/accounts/login/')
def ticket_detail(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    
    # COMMENT FORM IN TICKET DETAIL VIEW
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=ticket
            )
            comment.save()
    
    comments = Comment.objects.filter(post=ticket)
    context = {
        'ticket': ticket,
        "comments": comments,
        "form": form,
    }
    return render(request, 'ticket_detail.html', context)

##################################################################################

# EDIT TICKET 

@login_required(login_url='/accounts/login/')
def edit_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    form = TicketForm(instance=ticket)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            ticket.save()
            context = {
                'ticket' : ticket
            }
            return HttpResponseRedirect('/tickets')
        else: 
            form = TicketForm(instance=ticket)
    context = {
        "form": form,
    }
    return render(request, 'edit_ticket.html', context)

##################################################################################

# DELETE TICKET

@login_required(login_url='/accounts/login/')
def delete_ticket (request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return HttpResponseRedirect('/tickets')
    context = {
        'ticket' : ticket
    }
    return render(request, 'delete_ticket.html', context)


##################################################################################

# COMPLETED TICKET

@login_required(login_url='/accounts/login/')
def completed_ticket (request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.set_completion()
        return HttpResponseRedirect('/tickets')
    context = {
        'ticket' : ticket
    }
    return render(request, 'completed_ticket.html', context)



##################################################################################

# TICKET CATEGORY INDEX 

@login_required(login_url='/accounts/login/')
def ticket_category(request, category):
    tickets = Ticket.objects.filter(
        categories__name__contains = category
    )
    context = {
        "category": category, 
        "tickets": tickets
    }
    return render(request, 'ticket_category.html', context)


##################################################################################

# COMPLETED TICKETS INDEX 

@login_required(login_url='/accounts/login/')
def completed_index(request): 
    tickets = Ticket.objects.filter(
        completed = True
    )
    context = {
        "tickets": tickets
    } 
    return render(request, 'completed_index.html', context)


##################################################################################

# TICKET PRIORITY INDEX

@login_required(login_url='/accounts/login/')
def ticket_priority(request, priority):
    tickets = Ticket.objects.filter(
        priorities__name__contains = priority
    )
    context = {
        "priority": priority, 
        "tickets": tickets
    }
    return render(request, 'ticket_priority.html', context)