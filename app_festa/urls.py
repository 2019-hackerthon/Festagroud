from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('success_create/', views.success_create, name="success_create"),
    path('search/', views.search, name="search"),
    path('<int:festa_id>/delete/', views.delete, name="delete"),
    path('<int:festa_id>/edit/', views.edit, name="edit"),
    path('<int:festa_id>/update/', views.update, name="update"),
    path('festa_now/<int:festa_id>/', views.now_detail, name="now_detail"),
    path('festa_ready/<int:festa_id>/', views.ready_detail, name="ready_detail"),
    path('confirm_login/', views.confirm_login, name="confirm_login"),
    path('confirm/', views.confirm, name="confirm"),
    path('all_festaNow/', views.all_festaNow, name="all_festaNow"),
    path('all_festaReady/', views.all_festaReady, name="all_festaReady"),
    
    path('staff_notice/', views.staff_notice, name="staff_notice"),
    path('staff_new/', views.staff_new, name="staff_new"),
    path('staff_edit/<int:staff_id>', views.staff_edit, name="staff_edit"),
    path('staff_update/<int:staff_id>', views.staff_update, name="staff_update"),
    path('staff_create/', views.staff_create, name="staff_create"),
    path('staff_delete/<int:staff_id>', views.staff_delete, name="staff_delete"),
    path('staff_detail/<int:staff_id>', views.staff_detail, name="staff_detail"),
    


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)