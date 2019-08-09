from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:festa_id>/ready_main', views.ready_main, name="ready_main"),
    path('<int:festa_id>/accompany/create', views.create_accompany, name="create_accompany"),
    path('<int:festa_id>/list_accompany', views.list_accompany, name="list_accompany"),
    path('<int:festa_id>/detail_accompany/<int:accompany_id>/', views.detail_accompany, name="detail_accompany"),
    path('<int:festa_id>/edit_accompany/<int:accompany_id>/', views.edit_accompany, name="edit_accompany"),
    path('<int:festa_id>/update_accompany/<int:accompany_id>/', views.update_accompany, name="update_accompany"),
    path('<int:festa_id>/delete_accompany/<int:accompany_id>/', views.delete_accompany, name = "delete_accompany"),
    path('<int:festa_id>/<int:accompany_id>/create_commenta/', views.create_commenta, name="create_commenta"),
    path('<int:festa_id>/delete_commenta/<int:accompany_id>/<int:commenta_id>', views.delete_commenta, name="delete_commenta"),

    path('<int:festa_id>/ticket', views.ticket, name="ticket"),
    path('<int:festa_id>/ticket/create', views.create_ticket, name="create_ticket"),
    path('<int:festa_id>/list_ticket', views.list_ticket, name="list_ticket"),
    path('<int:festa_id>/detail_ticket<int:ticket_id>/', views.detail_ticket, name="detail_ticket"),
    path('<int:festa_id>/edit_ticket/<int:ticket_id>/', views.edit_ticket, name="edit_ticket"),
    path('<int:festa_id>/update_ticket/<int:ticket_id>/', views.update_ticket, name="update_ticket"),
    path('<int:festa_id>/delete_ticket/<int:ticket_id>/', views.delete_ticket, name = "delete_ticket"),
    path('<int:festa_id>/comment_ticket/<int:ticket_id>', views.comment_ticket, name="comment_ticket"),

    path('<int:festa_id>/incorrect_accompany', views.incorrect_accompany, name="incorrect_accompany"),
    path('<int:festa_id>/incorrect_ticket', views.incorrect_ticket, name="incorrect_ticket"),
    path('<int:festa_id>/<int:accompany_id>/incorrect_commenta', views.incorrect_commenta, name="incorrect_commenta"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)