from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),   
    path('for/', views.for_view, name='for'),
    path('table/', views.table_view, name='table'),
    path('student/', views.student, name='student'),
    path('subject/', views.subjects, name='subject'),
]