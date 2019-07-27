from django.shortcuts import render, get_object_or_404, redirect
from .models import Festa, RegisterNum
from .models import Accompany, Ticket
from .models import Now, Team, Commentn, Commentt, Home, Commenta, Commenttic, Commenth
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
    if request.method == 'POST' and request.FILES['poster']:
        festa = Festa()
        festa.name= request.POST['name']
        festa.schedule = request.POST['schedule']
        festa.space = request.POST['space']
        festa.purchase_link= request.POST['purchase_link']
        festa.host= request.POST['host']
        festa.contact= request.POST['contact']
        # festa.map = request.POST['map]
        festa.precautions= request.POST['precautions']
        festa.notice = request.POST['notice']
        festa.poster = request.FILES['poster']
        festa.save()
        return redirect('success_create')

def success_create(request) :
    reginumber = RegisterNum.objects.order_by("?").first()
    return render(request, 'festa_home/success_create.html', {'number':reginumber})

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
    festa = Festa.objects.all()
    register_num = RegisterNum.objects.all()
    rm = request.POST['register_num']
    all_number=[] #배열만듦
    for object in register_num :
        all_number.append(object)
    if 'rm' in all_number :
        return render(request, 'festa_home/confirm.html', {'confirm_festa':confirm_festa})
    else :
        return render(request, 'festa_home/home.html', {'all_number':all_number})

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


def now_staff(request):
    return render(request, 'festa_now/staff/staff.html')

def now_audience(request):
    return render(request, 'festa_now/audience/audience.html')

## festa.now_audience_festnow게시판
def now_now(request):
    nows = Now.objects
    return render(request, 'festa_now/audience/now.html', {'nows': nows})

def new_now(request):
    return render(request, 'festa_now/audience/new_now.html')

def detail_now(request, now_id):
    now = Now.objects.get(pk=now_id)
    comments_list = Commentn.objects.filter(now = now_id)
    return render(request, 'festa_now/audience/detail_now.html', {'now' : now, 'comments':comments_list })    

def delete_now(request, now_id):
    delete_now = get_object_or_404(Now, pk=now_id)
    delete_now.delete()
    return redirect('now_now')
    

def edit_now(request, now_id):
    edit_now = Now.objects.get(pk=now_id)
    return render(request, 'festa_now/audience/edit_now.html', {'now': edit_now})


def update_now(request, now_id):
        update_now = Now.objects.get(id = now_id)
        update_now.title = request.POST["title"]
        update_now.writer = request.POST['writer']
        update_now.body = request.POST['body']
        update_now.save()
        return redirect('now_now')

def create_now(request):
    if request.method=="POST":
        now = Now()
        now.title = request.POST['title']
        now.body = request.POST['body']
        now.writer = request.POST['writer']
        now.pub_date = timezone.datetime.now()
        now.save()
        return redirect('now_now')
    return render(request, 'festa_now/audience/now.html')

## festa.now_staff_팀별게시판
def now_team(request):
    teams = Team.objects
    return render(request, 'festa_now/staff/team.html', {'teams': teams})

def new_team(request):
    return render(request, 'festa_now/staff/new_team.html')

def detail_team(request, team_id):
    team = Team.objects.get(pk=team_id)
    comments_list = Commentt.objects.filter(team = team_id)
    return render(request, 'festa_now/staff/detail_team.html', {'team' : team, 'comments': comments_list })    

def delete_team(request, team_id):
    delete_team = get_object_or_404(Team, pk=team_id)
    delete_team.delete()
    return redirect('now_team')

def edit_team(request, team_id):
    edit_team = Team.objects.get(pk=team_id)
    return render(request, 'festa_now/staff/edit_team.html', {'team': edit_team})


def update_team(request, team_id):
        update_team = Team.objects.get(id = team_id)
        update_team.title2 = request.POST["title"]
        update_team.writer2 = request.POST['writer']
        update_team.body2 = request.POST['body']
        update_team.save()
        return redirect('now_team')

def create_team(request):
    if request.method=="POST":
        team = Team()
        team.title2 = request.POST['title']
        team.body2 = request.POST['body']
        team.writer2 = request.POST['writer']
        team.pub_date2 = timezone.datetime.now()
        team.save()
        return redirect('now_team')
    return render(request, 'festa_now/staff/team.html')

## 댓글 
def comment_now(request, now_id):
    comment = Commentn()
    comment.writer_now = request.POST['writer']
    comment.content_now = request.POST['content']
    comment.now = get_object_or_404(Now, pk=now_id)
    comment.save()
    return redirect('detail_now', now_id)

def comment_team(request, team_id):
    comment = Commentt()
    comment.writer_team = request.POST['writer']
    comment.content_team = request.POST['content']
    comment.team = get_object_or_404(Team, pk=team_id)
    comment.save()
    return redirect('detail_team', team_id)

def comment_home(request, home_id):
    comment = Commenth()
    comment.writer_home = request.POST['writer']
    comment.content_home = request.POST['content']
    comment.home = get_object_or_404(Home, pk=home_id)
    comment.save()
    return redirect('detail_home', home_id)
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


##집가자
def audience_home(request):
    homes = Home.objects
    return render(request, 'festa_now/audience/home.html', {'homes':homes})

def staff_home(request):
    homes = Home.objects
    return render(request, 'festa_now/staff/home.html', {'homes':homes})    

def new_home(request):
    return render(request, 'festa_now/new_home.html')

def detail_home(request, home_id):
    home = Home.objects.get(pk=home_id)
    comments_list = Commenth.objects.filter(home = home_id)
    return render(request, 'festa_now/detail_home.html', {'home' : home, 'comments' : comments_list})   

def delete_home(request, home_id):
    delete_home = get_object_or_404(Home, pk=home_id)
    delete_home.delete()
    return redirect('home')

def edit_home(request, home_id):
    edit_home = Home.objects.get(pk=home_id)
    return render(request, 'festa_now/edit_home.html', {'home': edit_home})


def update_home(request, home_id):
        update_home = Home.objects.get(id = home_id)
        update_home.title = request.POST["title"]
        update_home.writer = request.POST['writer']
        update_home.body = request.POST['body']
        update_home.region = request.POST['region']
        update_home.save()
        return redirect('home')

def create_home(request):
    if request.method=="POST":
        home = Home()
        home.title = request.POST['title']
        home.body = request.POST['body']
        home.writer = request.POST['writer']
        home.region = request.POST['region']
        home.pub_date = timezone.datetime.now()
        home.save()
        return redirect('home')
    return render(request, 'festa_now/deatil_home.html')





