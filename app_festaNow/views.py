from django.shortcuts import render, get_object_or_404, redirect
from app_festa.models import Festa, RegisterNum, Staff
from app_festaReady.models import Accompany, Ticket, Commenta, Commenttic
from app_festaNow.models import Now, Team, Commentn, Commentt, Home, Commenth, ReservationNum, Lost_Found, Commentlf
import datetime
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.

##################### staff_main이랑 audience_main으로 대체함#####################################
# def now_staff(request, festa_id):
#     staffs = Staff.objects
#     festa = get_object_or_404(Festa, pk = festa_id)
#     return render(request, 'festa_now/staff/staff.html', {'festa':festa, 'staffs':staffs})

# def now_audience(request, festa_id):
#     festa = get_object_or_404(Festa, pk = festa_id)
#     return render(request, 'festa_now/audience/audience.html', {'festa':festa})
#################################################################################################

########## festa_now/staff, audience/main(공지사항)+login ##########
def audience_login(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/audience/login.html', {'festa': festa})

def staff_login(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/staff/login.html', {'festa': festa})

def audience_main(request, festa_id) :
    if request.method == 'POST' :
        festa = get_object_or_404(Festa, pk = festa_id)
        first = request.POST['reservation_name']
        second = request.POST["reservation_num"]
        num_object = ReservationNum.objects.get(reservation_num = second)
        name_object = ReservationNum.objects.get(reservation_name = first)
        first = name_object
        second = num_object
        return render(request, 'festa_now/audience/audience_main.html', {'festa':festa})
    else :
        festa = get_object_or_404(Festa, pk = festa_id)
        return render(request, 'festa_now/audience/audience_main.html', {'festa':festa})

def staff_main(request, festa_id) :
    if request.method == 'POST':
        festa = get_object_or_404(Festa, pk = festa_id)
        first = request.POST['reservation_name']
        second = request.POST["reservation_num"]
        num_object = ReservationNum.objects.get(reservation_num = second)
        name_object = ReservationNum.objects.get(reservation_name = first)
        first = name_object
        second = num_object
        return render(request, 'festa_now/staff/staff_main.html', {'festa':festa})
    else :
        festa = get_object_or_404(Festa, pk = festa_id)
        return render(request, 'festa_now/staff/staff_main.html', {'festa':festa})

########## festa_now/audience/festnow게시판 ##########
def now_now(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    nows = Now.objects.filter(festa = festa.id)
    paginator = Paginator(nows, 5)
    page = request.GET.get('page')
    now_list = paginator.get_page(page)
    return render(request, 'festa_now/audience/now.html', {'nows': nows, 'now_list': now_list,'festa': festa})


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
    if request.method == 'POST' :
        update_now = Now.objects.get(id = now_id)
        update_now.title = request.POST["title"]
        update_now.writer = request.POST['writer']
        update_now.post_type = request.POST['post_type']
        update_now.body = request.POST['body']
        update_now.save()
        return redirect('detail_now', festa.id, update_now.pk)

def create_now(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        now = Now()
        now.festa = get_object_or_404(Festa, pk = festa_id)
        now.title = request.POST['title']
        now.body = request.POST['body']
        now.post_type = request.POST['post_type']
        now.writer = request.POST['writer']
        now.pub_date = timezone.datetime.now()
        now.save()
        return redirect('detail_now', festa.id, now.pk)
    return render(request, 'festa_now/audience/now.html', {'festa':festa})

########## festa_now/audience/map ##########
def audience_map(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/audience/map.html', {'festa':festa})

########## festa_now/staff/map ##########
def staff_map(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/staff/map.html', {'festa':festa})

########## festa_now/staff/팀별게시판 ##########
def now_team(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    teams = Team.objects.filter(festa = festa.id)
    paginator = Paginator(teams, 5)
    page = request.GET.get('page')
    team_list = paginator.get_page(page)
    return render(request, 'festa_now/staff/team.html', {'teams': teams,'team_list':team_list ,'festa': festa})

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
    update_team.post_type = request.POST['post_type']
    update_team.body2 = request.POST['body']
    update_team.save()
    return redirect('detail_team', festa.id, update_team.pk)

def create_team(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        team = Team()
        team.festa = get_object_or_404(Festa, pk = festa_id)
        team.title2 = request.POST['title']
        team.body2 = request.POST['body']
        team.writer2 = request.POST['writer']
        team.post_type = request.POST['post_type']
        team.pub_date2 = timezone.datetime.now()
        team.save()
        return redirect('detail_team', festa.id, team.pk)
    return render(request, 'festa_now/staff/team.html', {'festa': festa})

########## festa_now/audience/home(집가자 게시판) ##########
def audience_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    homes = Home.objects.filter(festa = festa.id)
    paginator = Paginator(homes, 5)
    page = request.GET.get('page')
    home_list = paginator.get_page(page)
    return render(request, 'festa_now/audience/home/audience_home.html', {'homes':homes, 'home_list':home_list, 'festa':festa})
def a_new_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/audience/home/new_home.html',{'festa': festa})

def a_detail_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    home = Home.objects.get(pk=home_id)
    comments_list = Commenth.objects.filter(home = home_id)
    return render(request, 'festa_now/audience/home/detail_home.html', {'home' : home, 'comments' : comments_list, 'festa': festa})   

def a_delete_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    delete_home = get_object_or_404(Home, pk=home_id)
    delete_home.delete()
    return redirect('audience_home', festa_id)

def a_edit_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    edit_home = Home.objects.get(pk=home_id)
    return render(request, 'festa_now/audience/home/edit_home.html', {'home': edit_home, 'festa': festa})


def a_update_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    update_home = Home.objects.get(id = home_id)
    update_home.title = request.POST["title"]
    update_home.writer = request.POST['writer']
    update_home.body = request.POST['body']
    update_home.region = request.POST['region']
    update_home.save()
    return redirect('a_detail_home', festa.id, update_home.pk)

def a_create_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        home = Home()
        home.festa = get_object_or_404(Festa, pk = festa_id)
        home.title = request.POST['title']
        home.body = request.POST['body']
        home.writer = request.POST['writer']
        home.region = request.POST['region']
        home.pub_date = timezone.datetime.now()
        home.save()
        return redirect('a_detail_home', festa.id, home.pk)
    return render(request, 'festa_now/audience/home/deatil_home.html', {'festa':festa})

########## festa_now/audience/lost_found(찾아가라 게시판) ##########
def audience_lost_found(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    lost_founds = Lost_Found.objects.filter(festa = festa.id)
    paginator = Paginator(lost_founds, 5)
    page = request.GET.get('page')
    lostfounds_list = paginator.get_page(page)
    return render(request, 'festa_now/audience/lost_found/audience_lost_found.html', {'lost_founds':lost_founds, 'lostfounds_list' : lostfounds_list, 'festa':festa})

def a_new_lost_found(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/audience/lost_found/new_lost_found.html',{'festa': festa})

def a_detail_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    lost_found = Lost_Found.objects.get(pk=lost_found_id)
    comments_list = Commentlf.objects.filter(lost_found = lost_found_id)
    return render(request, 'festa_now/audience/lost_found/detail_lost_found.html', {'lost_found' : lost_found, 'comments' : comments_list, 'festa': festa})   

def a_delete_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    delete_lost_found = get_object_or_404(Lost_Found, pk=lost_found_id)
    delete_lost_found.delete()
    return redirect('audience_lost_found', festa_id)

def a_edit_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    edit_lost_found = Lost_Found.objects.get(pk=lost_found_id)
    return render(request, 'festa_now/audience/lost_found/edit_lost_found.html', {'lost_found': edit_lost_found, 'festa': festa})


def a_update_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    update_lost_found = Lost_Found.objects.get(id =lost_found_id)
    update_lost_found.title = request.POST["title"]
    update_lost_found.writer = request.POST['writer']
    update_lost_found.body = request.POST['body']
    update_lost_found.post_type = request.POST['post_type']
    update_lost_found.image = request.FILES['image']
    update_lost_found.save()
    return redirect('a_detail_lost_found', festa.id, update_lost_found.pk)

def a_create_lost_found(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        lost_found = Lost_Found()
        lost_found.festa = get_object_or_404(Festa, pk = festa_id)
        lost_found.title = request.POST['title']
        lost_found.body = request.POST['body']
        lost_found.writer = request.POST['writer']
        lost_found.post_type = request.POST['post_type']
        lost_found.image = request.FILES['image']
        lost_found.pub_date = timezone.datetime.now()
        lost_found.save()
        return redirect('a_detail_lost_found', festa.id, lost_found.pk)
    return render(request, 'festa_now/audience/lost_found/deatil_lost_found.html', {'festa':festa})

########## festa_now/staff/lost_found(찾아가라 게시판) ##########
def staff_lost_found(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    lost_founds = Lost_Found.objects.filter(festa = festa.id)
    paginator = Paginator(lost_founds, 5)
    page = request.GET.get('page')
    lostfounds_list = paginator.get_page(page)
    return render(request, 'festa_now/staff/lost_found/staff_lost_found.html', {'lost_founds':lost_founds, 'lostfounds_list' : lostfounds_list,'festa':festa})
    
def s_new_lost_found(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/staff/lost_found/new_lost_found.html',{'festa': festa})

def s_detail_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    lost_found = Lost_Found.objects.get(pk=lost_found_id)
    comments_list = Commentlf.objects.filter(lost_found = lost_found_id)
    return render(request, 'festa_now/staff/lost_found/detail_lost_found.html', {'lost_found' : lost_found, 'comments' : comments_list, 'festa': festa})   

def s_delete_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    delete_lost_found = get_object_or_404(Lost_Found, pk=lost_found_id)
    delete_lost_found.delete()
    return redirect('staff_lost_found', festa_id)

def s_edit_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    edit_lost_found = Lost_Found.objects.get(pk=lost_found_id)
    return render(request, 'festa_now/staff/lost_found/edit_lost_found.html', {'lost_found': edit_lost_found, 'festa': festa})


def s_update_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    update_lost_found = Lost_Found.objects.get(id =lost_found_id)
    update_lost_found.title = request.POST["title"]
    update_lost_found.writer = request.POST['writer']
    update_lost_found.body = request.POST['body']
    update_lost_found.post_type = request.POST['post_type']
    update_lost_found.image = request.FILES['image']
    update_lost_found.save()
    return redirect('s_detail_lost_found', festa.id, update_lost_found.pk)

def s_create_lost_found(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        lost_found = Lost_Found()
        lost_found.festa = get_object_or_404(Festa, pk = festa_id)
        lost_found.title = request.POST['title']
        lost_found.body = request.POST['body']
        lost_found.writer = request.POST['writer']
        lost_found.post_type = request.POST['post_type']
        lost_found.image = request.FILES['image']
        lost_found.pub_date = timezone.datetime.now()
        lost_found.save()
        return redirect('s_detail_lost_found', festa.id, lost_found.pk)
    return render(request, 'festa_now/staff/lost_found/deatil_lost_found.html', {'festa':festa})


########## festa_now/staff/home(집가자 게시판) ###########
def staff_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    homes = Home.objects.filter(festa = festa.id)
    paginator = Paginator(homes, 5)
    page = request.GET.get('page')
    home_list = paginator.get_page(page)
    return render(request, 'festa_now/staff/home/staff_home.html', {'homes':homes,'home_list':home_list ,'festa': festa})    

def s_new_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_now/staff/home/new_home.html',{'festa': festa})

def s_detail_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    home = Home.objects.get(pk=home_id)
    comments_list = Commenth.objects.filter(home = home_id)
    return render(request, 'festa_now/staff/home/detail_home.html', {'home' : home, 'comments' : comments_list, 'festa': festa})   

def s_delete_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    delete_home = get_object_or_404(Home, pk=home_id)
    delete_home.delete()
    return redirect('staff_home', festa_id)

def s_edit_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    edit_home = Home.objects.get(pk=home_id)
    return render(request, 'festa_now/staff/home/edit_home.html', {'home': edit_home, 'festa': festa})


def s_update_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    update_home = Home.objects.get(id = home_id)
    update_home.title = request.POST["title"]
    update_home.writer = request.POST['writer']
    update_home.body = request.POST['body']
    update_home.region = request.POST['region']
    update_home.save()
    return redirect('s_detail_home', festa.id, update_home.pk)

def s_create_home(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        home = Home()
        home.festa = get_object_or_404(Festa, pk = festa_id)
        home.title = request.POST['title']
        home.body = request.POST['body']
        home.writer = request.POST['writer']
        home.region = request.POST['region']
        home.pub_date = timezone.datetime.now()
        home.save()
        return redirect('s_detail_home', festa.id, home.pk)
    return render(request, 'festa_now/staff/home/deatil_home.html', {'festa':festa})

########## festa_now/staff+audience/festanow게시판, 팀별게시판, 집가자게시판 댓글들 ##########
def comment_now(request, festa_id, now_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    comment = Commentn()
    comment.writer_now = request.POST['writer']
    comment.content_now = request.POST['content']
    comment.now = get_object_or_404(Now, pk=now_id)
    comment.save()
    return redirect('detail_now', festa_id, now_id)

def comment_team(request, festa_id, team_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    comment = Commentt()
    comment.writer_team = request.POST['writer']
    comment.content_team = request.POST['content']
    comment.team = get_object_or_404(Team, pk=team_id)
    comment.save()
    return redirect('detail_team', festa_id, team_id)

def s_comment_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    comment = Commenth()
    comment.writer_home = request.POST['writer']
    comment.content_home = request.POST['content']
    comment.home = get_object_or_404(Home, pk=home_id)
    comment.save()
    return redirect('s_detail_home', festa_id, home_id)

def a_comment_home(request, festa_id, home_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    comment = Commenth()
    comment.writer_home = request.POST['writer']
    comment.content_home = request.POST['content']
    comment.home = get_object_or_404(Home, pk=home_id)
    comment.save()
    return redirect('a_detail_home', festa_id, home_id)

def a_comment_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    comment = Commentlf()
    comment.writer_lost_found = request.POST['writer']
    comment.content_lost_found = request.POST['content']
    comment.lost_found = get_object_or_404(Lost_Found, pk=lost_found_id)
    comment.save()
    return redirect('a_detail_lost_found', festa_id, lost_found_id)

def s_comment_lost_found(request, festa_id, lost_found_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    comment = Commentlf()
    comment.writer_lost_found = request.POST['writer']
    comment.content_lost_found = request.POST['content']
    comment.lost_found = get_object_or_404(Lost_Found, pk=lost_found_id)
    comment.save()
    return redirect('s_detail_lost_found', festa_id, lost_found_id)


