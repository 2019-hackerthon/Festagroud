from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:festa_id>/accompany', views.accompany, name="accompany"),
    path('accompany/create', views.create_accompany, name="create_accompany"),
    path('list_accompany', views.list_accompany, name="list_accompany"),
    path('detail_accompany<int:accompany_id>/', views.detail_accompany, name="detail_accompany"),
    path('edit_accompany/<int:accompany_id>/', views.edit_accompany, name="edit_accompany"),
    path('update_accompany/<int:accompany_id>/', views.update_accompany, name="update_accompany"),
    path('delete_accompany/<int:accompany_id>/', views.delete_accompany, name = "delete_accompany"),
    path('comment_accompany/<int:accompany_id>', views.comment_accompany, name="comment_accompany"),

    path('<int:festa_id>/ticket', views.ticket, name="ticket"),
    path('accompany/create_accompany', views.create_ticket, name="create_ticket"),
    path('list_ticket', views.list_ticket, name="list_ticket"),
    path('detail_ticket<int:ticket_id>/', views.detail_ticket, name="detail_ticket"),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name="edit_ticket"),
    path('update_ticket/<int:ticket_id>/', views.update_ticket, name="update_ticket"),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name = "delete_ticket"),
    path('comment_ticket/<int:ticket_id>', views.comment_ticket, name="comment_ticket"),

    path('incorrect_accompany', views.incorrect_accompany, name="incorrect_accompany"),
    path('incorrect_ticket', views.incorrect_ticket, name="incorrect_ticket"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)