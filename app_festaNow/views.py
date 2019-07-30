from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from app_festa.models import Festa, RegisterNum
from app_festaReady.models import Accompany, Ticket, Commenta, Commenttic
from app_festaNow.models import Now, Team, Commentn, Commentt, Home, Commenth, ReservationNum
import datetime
from django.utils import timezone


# Create your views here.
def now_staff(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/staff/staff.html', {'festa':festa})

def now_audience(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/audience/audience.html', {'festa':festa})

## festa.now_audience_festnow게시판
def now_now(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    nows = Now.objects
    return render(request, 'festa_now/audience/now.html', {'nows': nows, 'festa': festa})

def new_now(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/audience/new_now.html', {'festa':festa})

def detail_now(request, festa_id, now_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    now = Now.objects.get(pk=now_id)
    comments_list = Commentn.objects.filter(now = now_id)
    return render(request, 'festa_now/audience/detail_now.html', {'now' : now, 'comments':comments_list, 'festa':festa })    

def delete_now(request, festa_id, now_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    delete_now = get_object_or_404(Now, pk=now_id)
    delete_now.delete()
    return redirect('/festa_now/{}/audience/now'.format(festa.id))
    

def edit_now(request, festa_id, now_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    edit_now = Now.objects.get(pk=now_id)
    return render(request, 'festa_now/audience/edit_now.html', {'now': edit_now, 'festa':festa})


def update_now(request, festa_id, now_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    update_now = Now.objects.get(id = now_id)
    update_now.title = request.POST["title"]
    update_now.writer = request.POST['writer']
    update_now.body = request.POST['body']
    update_now.save()
    return redirect('/festa_now/{}/audience/now'.format(festa.id))

def create_now(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        now = Now()
        now.title = request.POST['title']
        now.body = request.POST['body']
        now.writer = request.POST['writer']
        now.pub_date = timezone.datetime.now()
        now.save()
        return redirect('/festa_now/{}/audience/detail_now/{}'.format(festa.id, now.id))
    return render(request, 'festa_now/audience/now.html', {'festa':festa})

## festa.now_staff_팀별게시판
def now_team(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    teams = Team.objects
    return render(request, 'festa_now/staff/team.html', {'teams': teams, 'festa': festa})

def new_team(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/staff/new_team.html', {'festa':festa})

def detail_team(request, festa_id, team_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    team = Team.objects.get(pk=team_id)
    comments_list = Commentt.objects.filter(team = team_id)
    return render(request, 'festa_now/staff/detail_team.html', {'team' : team, 'comments': comments_list, 'festa': festa})    

def delete_team(request, festa_id, team_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    delete_team = get_object_or_404(Team, pk=team_id)
    delete_team.delete()
    return redirect('/festa_now/{}/staff/team'.format(festa.id))

def edit_team(request, festa_id, team_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    edit_team = Team.objects.get(pk=team_id)
    return render(request, 'festa_now/staff/edit_team.html', {'team': edit_team, 'festa':festa})


def update_team(request, festa_id, team_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    update_team = Team.objects.get(id = team_id)
    update_team.title2 = request.POST["title"]
    update_team.writer2 = request.POST['writer']
    update_team.body2 = request.POST['body']
    update_team.save()
    return redirect('/festa_now/{}/staff/team'.format(festa.id))

def create_team(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        team = Team()
        team.title2 = request.POST['title']
        team.body2 = request.POST['body']
        team.writer2 = request.POST['writer']
        team.pub_date2 = timezone.datetime.now()
        team.save()
        return redirect('/festa_now/{}/staff/detail_team/{}'.format(festa.id, team.id))
    return render(request, 'festa_now/staff/team.html', {'festa': festa})

## 댓글 
def comment_now(request, festa_id, now_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    comment = Commentn()
    comment.writer_now = request.POST['writer']
    comment.content_now = request.POST['content']
    comment.now = get_object_or_404(Now, pk=now_id)
    comment.save()
    return redirect('/festa_now/{}/audience/now'.format(festa.id))

def comment_team(request, festa_id, team_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    comment = Commentt()
    comment.writer_team = request.POST['writer']
    comment.content_team = request.POST['content']
    comment.team = get_object_or_404(Team, pk=team_id)
    comment.save()
    return redirect('/festa_now/{}/staff/team'.format(festa.id))

def comment_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    comment = Commenth()
    comment.writer_home = request.POST['writer']
    comment.content_home = request.POST['content']
    comment.home = get_object_or_404(Home, pk=home_id)
    comment.save()
    return redirect('detail_home', home_id)

##집가자
def audience_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    homes = Home.objects
    return render(request, 'festa_now/audience/home.html', {'homes':homes, 'festa':festa})

def staff_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    homes = Home.objects
    return render(request, 'festa_now/staff/home.html', {'homes':homes, 'festa': festa})    

def new_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/new_home.html')

def detail_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    home = Home.objects.get(pk=home_id)
    comments_list = Commenth.objects.filter(home = home_id)
    return render(request, 'festa_now/detail_home.html', {'home' : home, 'comments' : comments_list, 'festa': festa})   

def delete_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    delete_home = get_object_or_404(Home, pk=home_id)
    delete_home.delete()
    return redirect('home')

def edit_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    edit_home = Home.objects.get(pk=home_id)
    return render(request, 'festa_now/edit_home.html', {'home': edit_home, 'festa': festa})


def update_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    update_home = Home.objects.get(id = home_id)
    update_home.title = request.POST["title"]
    update_home.writer = request.POST['writer']
    update_home.body = request.POST['body']
    update_home.region = request.POST['region']
    update_home.save()
    return redirect('home')

def create_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        home = Home()
        home.title = request.POST['title']
        home.body = request.POST['body']
        home.writer = request.POST['writer']
        home.region = request.POST['region']
        home.pub_date = timezone.datetime.now()
        home.save()
        return redirect('home')
    return render(request, 'festa_now/deatil_home.html', {'festa':festa})


##staff audience now 로그인

def audience_login(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/audience/login.html', {'festa': festa})

def staff_login(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/staff/login.html', {'festa': festa})

def confirm_now(request, festa_id) :
    festa = get_object_or_404(Festa, pk = festa_id)
    first = request.POST['reservation_name']
    second = request.POST["reservation_num"]
    num_object = ReservationNum.objects.get(reservation_num = second)
    name_object = ReservationNum.objects.get(reservation_name = first)
    first = name_object
    second = num_object
    return render(request, 'festa_now/audience/audience.html', {'festa':festa})

def confirm_now2(request, festa_id) :
    festa = get_object_or_404(Festa, pk = festa_id)
    first = request.POST['reservation_name']
    second = request.POST["reservation_num"]
    num_object = ReservationNum.objects.get(reservation_num = second)
    name_object = ReservationNum.objects.get(reservation_name = first)
    first = name_object
    second = num_object
    return render(request, 'festa_now/staff/staff.html', {'festa':festa})


def staff_map(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/staff/map.html', {'festa':festa})

def audience_map(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/audience/map.html', {'festa':festa})



