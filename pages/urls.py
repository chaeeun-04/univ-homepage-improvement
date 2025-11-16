from django.urls import path

from . import views



urlpatterns = [

path('', views.index, name='index'),





path('timetable/', views.timetable_view, name='master_timetable'),

path('graduation/', views.graduation_view, name='graduation_requirements'),

path('forms/', views.forms_view, name='forms_archive'),

path('cafeteria/', views.cafeteria_view, name='cafeteria_menu'),

path('matching/', views.matching, name='matching'),



path('track/<str:menu_name_pk>/', views.track_menu_click, name='track_click'),

]