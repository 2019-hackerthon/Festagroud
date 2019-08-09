from django.shortcuts import render, get_object_or_404, redirect
from .models import Festa, RegisterNum, Staff, Audience
from app_festaReady.models import Accompany, Ticket, Commenta, Commenttic
from app_festaNow.models import Now, Team, Commentn, Commentt, Home, Commenth
import datetime
from django.utils import timezone

# Create your views here.

def home(request) :
    festas = Festa.objects # Festa객체 받기
    today = datetime.datetime.now() #오늘 날짜 today 변수에 담음
    
    return render(request, 'festa_home/home.html', {'festas' : festas, 'today':today})

def new(request) :
    return render(request, 'festa_home/new.html')

def create(request) :
    #RegisterNum random으로 섞고 그 중 젤 첫번째랑 festa를 match
    num = RegisterNum.objects.order_by("?").first()
    if request.method == 'POST' and request.FILES['poster']:
        festa = Festa()
        festa.number = num
        festa.name= request.POST['name']
        festa.schedule_start = request.POST['schedule_start']
        festa.schedule_end = request.POST['schedule_end']
        festa.space = request.POST['space']
        festa.purchase_link= request.POST['purchase_link']
        festa.host= request.POST['host']
        festa.contact= request.POST['contact']
        festa.detail_map = request.POST['detail_map']
        festa.poster = request.FILES['poster']
        festa.save()
        return redirect('success_create')

def success_create(request) :
    latest_festa = Festa.objects.latest('id')
    number = latest_festa.number
    return render(request, 'festa_home/success_create.html', {'number': number})

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
    false = 0
    if request.method == 'POST' :
        number = request.POST['register_num']
        number_object = RegisterNum.objects.get(register_num = number) 
        festa_object=number_object.festa
        return render(request, 'festa_home/confirm.html', {'festa':festa_object})
    return render(request, 'festa_home/confirm_login.html', {'fail': false})
        

def all_festaNow(request) :
    festas = Festa.objects
    today = datetime.datetime.now()
    return render(request, 'festa_home/all_festaNow.html', {'festa':festas, 'today':today})

def all_festaReady(request) :
    festas = Festa.objects
    today = datetime.datetime.now()
    return render(request, 'festa_home/all_festaReady.html', {'festa':festas, 'today':today})

