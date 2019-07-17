from django.shortcuts import render, get_object_or_404, redirect
from .models import Festa
import datetime

# Create your views here.

def home(request) :
    festas = Festa.objects # Festa객체 받기
    today = datetime.datetime.now() #오늘 날짜 today 변수에 담음
    return render(request, 'festa_home/home.html', {'festas' : festas, 'today':today})

def new(request) :
    return render(request, 'festa_home/new.html')

def create(request) :
    if request.method == 'POST' and request.FILES['image']:
        # today = datetime.datetime.now().strftime('%Y-%m-%d')
        festa = Festa()
        festa.name= request.POST['name']
        festa.schedule = request.POST['schedule']
        festa.space = request.POST['space']
        festa.info = request.POST['info']
        festa.image = request.FILES['image']
        festa.save()
        # if festa.schedule == today :
        #     return redirect('festa_now/' + str(festa.id))
        # else :
        #     return redirect('festa_ready/' + str(festa.id))
        return redirect('home')
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
    if request.method == 'POST' and request.FILES['image'] :
        update_festa = Festa.objects.get(id = festa_id)
        update_festa.name = request.POST['name']
        update_festa.schedule = request.POST['schedule']
        update_festa.space = request.POST['space']
        update_festa.image = request.FILES['image']
        update_festa.save()
        return redirect('home')
