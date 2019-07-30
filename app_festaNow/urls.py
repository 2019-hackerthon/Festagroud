from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('staff/staff', views.now_staff, name="now_staff"),
    path('audience/audience', views.now_audience, name="now_audience"),
    
    path('audience/detail_now/<int:now_id>', views.detail_now, name="detail_now"),
    path('audience/now', views.now_now, name="now_now"),
    path('audience/new_now', views.new_now, name="new_now"),
    path('audience/delete_now/<int:now_id>', views.delete_now, name="delete_now"),
    path('audience/edit_now/<int:now_id>', views.edit_now, name="edit_now"),
    path('audience/update_now/<int:now_id>', views.update_now, name="update_now"),
    path('audience/create_now/', views.create_now, name="create_now"),
    path('audience/comment_now/<int:now_id>', views.comment_now, name="comment_now"),
    path('audience/home', views.audience_home, name="audience_home"),

    path('staff/detail_team/<int:team_id>', views.detail_team, name="detail_team"),
    path('staff/team', views.now_team, name="now_team"),
    path('staff/new_team', views.new_team, name="new_team"),
    path('staff/delete_team/<int:team_id>', views.delete_team, name="delete_team"),
    path('staff/edit_team/<int:team_id>', views.edit_team, name="edit_team"),
    path('staff/update_team/<int:team_id>', views.update_team, name="update_team"),
    path('staff/create_team/', views.create_team, name="create_team"),
    path('staff/comment_team/<int:team_id>', views.comment_team, name="comment_team"),
    path('staff/home', views.staff_home, name="staff_home"),

    path('detail_home/<int:home_id>', views.detail_home, name="detail_home"),
    path('new_home', views.new_home, name="new_home"),
    path('delete_home/<int:home_id>', views.delete_home, name="delete_home"),
    path('edit_home/<int:home_id>', views.edit_home, name="edit_home"),
    path('update_home/<int:home_id>', views.update_home, name="update_home"),
    path('create_home/', views.create_home, name="create_home"),
    path('comment_home/<int:home_id>', views.comment_home, name="comment_home"),

    path('confirm_now/', views.confirm_now, name="confirm_now"),
    path('<int:festa_id>/audience_login', views.audience_login, name="audience_login"),
    path('confirm_now2/', views.confirm_now2, name="confirm_now2"),
    path('<int:festa_id>/staff_login/', views.staff_login, name="staff_login"),

    path('audience_map/', views.audience_map, name="audience_map"),
    path('staff_map/', views.staff_map, name="staff_map"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)