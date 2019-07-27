from django.shortcuts import render, get_object_or_404, redirect
from app_festa.models import Festa, RegisterNum
from app_festaReady.models import Accompany, Ticket, Commenta, Commenttic
from app_festaNow.models import Now, Team, Commentn, Commentt, Home, Commenth
import datetime
from django.utils import timezone


# Create your views here.
def accompany(request, festa_id) :
    festa_detail = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_ready/accompany.html', {'festa': festa_detail})

def list_accompany(request):
    accompanies = Accompany.objects
    return render(request, 'festa_ready/list_accompany.html', {'accompanies':accompanies})

def create_accompany(request):
    if request.method=="POST":
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        area = request.POST.get('area')
        description = request.POST.get('description')
        accompany = Accompany(title=title, writer=writer, area=area, description=description)
        accompany.save()
        return redirect('list_accompany')        
    return render(request, 'festa_ready/create_accompany.html')

def detail_accompany(request, accompany_id):
    accompany = Accompany.objects.get(pk=accompany_id)
    comments_list = Commenta.objects.filter(accompany = accompany_id)
    return render(request, 'festa_ready/detail_accompany.html', {'accompany':accompany, 'comments': comments_list})

def edit_accompany(request, accompany_id):
    accompany = Accompany.objects.get(pk=accompany_id)
    return render(request, 'festa_ready/edit_accompany.html', {'accompany': accompany})

def update_accompany(request, accompany_id):
    if request.method == "POST":
        accompany = Accompany.objects.get(id = accompany_id)
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        area = request.POST.get('area')
        description = request.POST.get('description')
        accompany.title = title
        accompany.writer = writer
        accompany.area = area
        accompany.description = description
        accompany.save()
        return redirect('detail_accompany', accompany.pk)

def delete_accompany(request,accompany_id):
    if request.method == "POST":
        accompany = Accompany.objects.get(pk = accompany_id)
        accompany.delete()
        return redirect('list_accompany')


def ticket(request, festa_id) :
    festa_detail = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_ready/ticket.html', {'festa': festa_detail})

def list_ticket(request):
    tickets = Ticket.objects
    return render(request, 'festa_ready/list_ticket.html', {'tickets':tickets})

def create_ticket(request):
    if request.method=="POST":
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        deal_type = request.POST.get('deal_type')
        description = request.POST.get('description')
        ticket = Ticket(title=title, writer=writer, deal_type=deal_type, description=description)
        ticket.save()
        return redirect('list_ticket')        
    return render(request, 'festa_ready/create_ticket.html')

def detail_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    comments_list = Commenttic.objects.filter(ticket = ticket_id)
    return render(request, 'festa_ready/detail_ticket.html', {'ticket':ticket, 'comments': comments_list})


def edit_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'festa_ready/edit_ticket.html', {'ticket': ticket})

def update_ticket(request, ticket_id):
    if request.method == "POST":
        ticket = Ticket.objects.get(id = ticket_id)
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        deal_type = request.POST.get('deal_type')
        description = request.POST.get('description')
        ticket.title = title
        ticket.writer = writer
        ticket.deal_type = deal_type
        ticket.description = description
        ticket.save()
        return redirect('detail_ticket', ticket.pk)

def delete_ticket(request,ticket_id):
    if request.method == "POST":
        ticket = Ticket.objects.get(pk = ticket_id)
        ticket.delete()
        return redirect('list_ticket')

def comment_accompany(request, accompany_id):
    comment = Commenta()
    comment.writer_accompany = request.POST['writer']
    comment.content_accompany = request.POST['content']
    comment.accompany = get_object_or_404(Accompany, pk=accompany_id)
    comment.save()
    return redirect('detail_accompany', accompany_id)

def comment_ticket(request, ticket_id):
    comment = Commenttic()
    comment.writer_ticket = request.POST['writer']
    comment.content_ticket = request.POST['content']
    comment.ticket = get_object_or_404(Ticket, pk=ticket_id)
    comment.save()
    return redirect('detail_ticket', ticket_id)

