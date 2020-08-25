from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.ticket_index, name="ticket_index"),
    path("<int:pk>/", views.ticket_detail, name="ticket_detail"), 
    path("new/", views.new_ticket, name="new_ticket"),
    path("<int:pk>/edit/", views.edit_ticket, name="edit_ticket"), 
    path("<int:pk>/delete/", views.delete_ticket, name="delete_ticket"),
    path("<int:pk>/completed/", views.completed_ticket, name="completed_ticket"),
    path("finished/", views.completed_index, name="completed_index"),
    path("<priority>/", views.ticket_priority, name="ticket_priority"),
    path("<category>/", views.ticket_category, name="ticket_category"),
]