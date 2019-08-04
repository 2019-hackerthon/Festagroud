from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:festa_id>/audience/detail_now/<int:now_id>', views.detail_now, name="detail_now"),
    path('<int:festa_id>/audience/now', views.now_now, name="now_now"),
    path('<int:festa_id>/audience/new_now', views.new_now, name="new_now"),
    path('<int:festa_id>/audience/delete_now/<int:now_id>', views.delete_now, name="delete_now"),
    path('<int:festa_id>/audience/edit_now/<int:now_id>', views.edit_now, name="edit_now"),
    path('<int:festa_id>/audience/update_now/<int:now_id>', views.update_now, name="update_now"),
    path('<int:festa_id>/audience/create_now', views.create_now, name="create_now"),
    path('<int:festa_id>/audience/comment_now/<int:now_id>', views.comment_now, name="comment_now"),
    path('<int:festa_id>/audience/map', views.audience_map, name="audience_map"),
    path('<int:festa_id>/audience/home', views.audience_home, name="audience_home"),
    path('<int:festa_id>/audience/detail_home/<int:home_id>', views.a_detail_home, name="a_detail_home"),
    path('<int:festa_id>/audience/new_home', views.a_new_home, name="a_new_home"),
    path('<int:festa_id>/audience/delete_home/<int:home_id>', views.a_delete_home, name="a_delete_home"),
    path('<int:festa_id>/audience/edit_home/<int:home_id>', views.a_edit_home, name="a_edit_home"),
    path('<int:festa_id>/audience/update_home/<int:home_id>', views.a_update_home, name="a_update_home"),
    path('<int:festa_id>/audience/create_home/', views.a_create_home, name="a_create_home"),
    path('<int:festa_id>/audience/comment_home/<int:home_id>', views.a_comment_home, name="a_comment_home"),

    path('<int:festa_id>/staff/detail_team/<int:team_id>', views.detail_team, name="detail_team"),
    path('<int:festa_id>/staff/team', views.now_team, name="now_team"),
    path('<int:festa_id>/staff/new_team', views.new_team, name="new_team"),
    path('<int:festa_id>/staff/delete_team/<int:team_id>', views.delete_team, name="delete_team"),
    path('<int:festa_id>/staff/edit_team/<int:team_id>', views.edit_team, name="edit_team"),
    path('<int:festa_id>/staff/update_team/<int:team_id>', views.update_team, name="update_team"),
    path('<int:festa_id>/staff/create_team/', views.create_team, name="create_team"),
    path('<int:festa_id>/staff/comment_team/<int:team_id>', views.comment_team, name="comment_team"),
    path('<int:festa_id>/staff/map', views.staff_map, name="staff_map"),
    path('<int:festa_id>/staff/home', views.staff_home, name="staff_home"),
    path('<int:festa_id>/staff/detail_home/<int:home_id>', views.s_detail_home, name="s_detail_home"),
    path('<int:festa_id>/staff/new_home', views.s_new_home, name="s_new_home"),
    path('<int:festa_id>/staff/delete_home/<int:home_id>', views.s_delete_home, name="s_delete_home"),
    path('<int:festa_id>/staff/edit_home/<int:home_id>', views.s_edit_home, name="s_edit_home"),
    path('<int:festa_id>/staff/update_home/<int:home_id>', views.s_update_home, name="s_update_home"),
    path('<int:festa_id>/staff/create_home/', views.s_create_home, name="s_create_home"),
    path('<int:festa_id>/staff/comment_home/<int:home_id>', views.s_comment_home, name="s_comment_home"),

    path('<int:festa_id>/audience/audience_main', views.audience_main, name="audience_main"),
    path('<int:festa_id>/audience_login', views.audience_login, name="audience_login"),
    path('<int:festa_id>/staff/staff_main', views.staff_main, name="staff_main"),
    path('<int:festa_id>/staff_login', views.staff_login, name="staff_login"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)