from django.shortcuts import render, get_object_or_404, redirect
from .models import Festa
from django.utils import timezone

# Create your views here.

def home(request) :
    festas = Festa.objects
    return render(request, 'festa_home/home.html', {'festas' : festas})

def new(request) :
    return render(request, 'festa_home/new.html')

def create(request) :
    if request.method == 'POST' and request.FILES['image']:
        festa = Festa()
        festa.name= request.POST['name']
        festa.schedule = timezone.datetime.now()
        festa.space = request.POST['space']
        festa.image = request.FILES['image']
        festa.save()
    return redirect('/' + str(festa.id))


def detail(request, festa_id) :
    festa_detail = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_home/detail.html', {'festa': festa_detail})