"""project_festa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app_festa.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_festa.views.home, name="home"),
    path('new/', app_festa.views.new, name="new"),
    path('create/', app_festa.views.create, name="create"),
    path('success_create/', app_festa.views.success_create, name="success_create"),
    path('search/', app_festa.views.search, name="search"),
    path('<int:festa_id>/delete/', app_festa.views.delete, name="delete"),
    path('<int:festa_id>/edit/', app_festa.views.edit, name="edit"),
    path('<int:festa_id>/update/', app_festa.views.update, name="update"),
    path('festa_now/<int:festa_id>/', app_festa.views.now_detail, name="now_detail"),
    path('festa_ready/<int:festa_id>/', app_festa.views.ready_detail, name="ready_detail"),
    path('confirm_login/', app_festa.views.confirm_login, name="confirm_login"),
    path('confirm/', app_festa.views.confirm, name="confirm"),
    path('festa_ready/<int:festa_id>/accompany', app_festa.views.accompany, name="accompany"),
    path('festa_ready/accompany/create', app_festa.views.create_accompany, name="create_accompany"),
    path('festa_ready/list_accompany', app_festa.views.list_accompany, name="list_accompany"),
    path('festa_ready/detail_accompany<int:accompany_id>/', app_festa.views.detail_accompany, name="detail_accompany"),
    path('festa_ready/edit_accompany/<int:accompany_id>/', app_festa.views.edit_accompany, name="edit_accompany"),
    path('festa_ready/update_accompany/<int:accompany_id>/', app_festa.views.update_accompany, name="update_accompany"),
    path('festa_ready/delete_accompany/<int:accompany_id>/', app_festa.views.delete_accompany, name = "delete_accompany"),
    path('festa_ready/<int:festa_id>/ticket', app_festa.views.ticket, name="ticket"),
    path('festa_ready/accompany/create_accompany', app_festa.views.create_ticket, name="create_ticket"),
    path('festa_ready/list_ticket', app_festa.views.list_ticket, name="list_ticket"),
    path('festa_ready/detail_ticket<int:ticket_id>/', app_festa.views.detail_ticket, name="detail_ticket"),
    path('festa_ready/edit_ticket/<int:ticket_id>/', app_festa.views.edit_ticket, name="edit_ticket"),
    path('festa_ready/update_ticket/<int:ticket_id>/', app_festa.views.update_ticket, name="update_ticket"),
    path('festa_ready/delete_ticket/<int:ticket_id>/', app_festa.views.delete_ticket, name = "delete_ticket"),

    
    path('festa_now/staff', app_festa.views.now_staff, name="now_staff"),
    path('festa_now/audience', app_festa.views.now_audience, name="now_audience"),
    # audeince
    path('festa_now/now', app_festa.views.now_now, name="now_now"),
    path('festa_now/new_now', app_festa.views.new_now, name="new_now"),
    path('<int:now_id>/delete_now/', app_festa.views.delete_now, name="delete_now"),
    path('<int:now_id>/eidt_now/', app_festa.views.edit_now, name="edit_now"),
    path('<int:now_id>/update_now/', app_festa.views.update_now, name="update_now"),
    path('create_now/', app_festa.views.create_now, name="create_now"),
    path('check_edit_now/<int:now_id>',  app_festa.views.check_edit_now, name='check_edit_now'),
    path('check_delete_now/<int:now_id>',  app_festa.views.check_delete_now, name='check_delete_now'),
    # staff
    path('festa_now/', app_festa.views.now_team, name="team_team"),
    path('festa_now/', app_festa.views.new_team, name="new_team"),
    path('<int:now_id>/delete_now/', app_festa.views.delete_team, name="delete_team"),
    path('<int:now_id>/eidt_now/', app_festa.views.edit_team, name="edit_team"),
    path('<int:now_id>/update_now/', app_festa.views.update_team, name="update_team"),
    path('create_now/', app_festa.views.create_team, name="create_team"),
    path('check_edit_now/<int:now_id>',  app_festa.views.check_edit_team, name='check_edit_team'),
    path('check_delete_now/<int:now_id>',  app_festa.views.check_delete_team, name='check_delete_team'),




] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
