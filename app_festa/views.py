from django.shortcuts import render, get_object_or_404, redirect
from .models import Festa
from .models import Accompany, Ticket
import datetime

# Create your views here.

def home(request) :
    festas = Festa.objects # Festa객체 받기
    today = datetime.datetime.now() #오늘 날짜 today 변수에 담음
    return render(request, 'festa_home/home.html', {'festas' : festas, 'today':today})

def new(request) :
    return render(request, 'festa_home/new.html')

def create(request) :
    if request.method == 'POST' and request.FILES['poster']:
        festa = Festa()
        festa.name= request.POST['name']
        festa.schedule = request.POST['schedule']
        festa.space = request.POST['space']
        festa.purchase_link= request.POST['purchase_link']
        festa.host= request.POST['host']
        festa.contact= request.POST['contact']
        festa.precautions= request.POST['precautions']
        festa.notice = request.POST['notice']
        festa.poster = request.FILES['poster']
        festa.save()
        return redirect('success_create')

def success_create(request) :
    return render(request, 'festa_home/success_create.html')

def now_detail(request, festa_id) :
    festa_detail = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/detail.html', {'festa': festa_detail})

def ready_detail(request, festa_id) :
    festa_detail = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_ready/detail.html', {'festa': festa_detail})


def delete(request, festa_id) :
    delete_festa = Festa.objects.get(id = festa_id)
    delete_festa.delete()
    return redirect('home')

def edit(request, festa_id) :
    edit_festa = Festa.objects.get(id = festa_id)
    return render(request, 'festa_home/edit.html', {'festa' : edit_festa})

def update(request, festa_id) :
    if request.method == 'POST' and request.FILES['poster'] :
        update_festa = Festa.objects.get(id = festa_id)
        update_festa.name = request.POST['name']
        update_festa.schedule = request.POST['schedule']
        update_festa.space = request.POST['space']
        update_festa.image = request.FILES['poster']
        update_festa.save()
        return redirect('home')
  
def search(request) :
    all_festa = Festa.objects.all()
    keyword = request.GET.get('search_bar')
    search_festa=[]
    # festa이름이 keyword포함하면 search_festa list에 해당 festa추가
    for object in all_festa.filter(name__icontains = keyword) :
        search_festa.append(object)
    return render(request, 'festa_home/search.html', {'search_festa': search_festa})

def confirm_login(request) :
    return render(request, 'festa_home/confirm_login.html')

def confirm(request) :
    confirm_festa = Festa.objects.all()
    return render(request, 'festa_home/confirm.html', {'confirm_festa':confirm_festa})

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
    return render(request, 'festa_ready/detail_accompany.html', {'accompany':accompany})

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
    return render(request, 'festa_ready/detail_ticket.html', {'ticket':ticket})

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