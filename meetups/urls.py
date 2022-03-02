from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('meetups/', views.meetups, name="meetups"),
    path('meetup/<str:pk>/', views.meetup, name="meetup"),
    path('create-meetup/', views.create_meetup, name="create_meetup"),
    path('update-meetup/<str:pk>/', views.update_meetup, name="update_meetup"),
    path('delete-meetup/<str:pk>/', views.delete_meetup, name="delete_meetup"),
    path('attend-meetup/<str:pk>/', views.attend_meetup, name="attend_meetup"),
    path('cancel-attending/<str:pk>/', views.cancel_attend_meetup, name="cancel_attending"),
]