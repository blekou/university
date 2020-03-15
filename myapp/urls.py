from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('courses', views.courses, name='courses'),
    path('single', views.single, name='single'),
    path('elements', views.elements, name='elements'),
    path('event', views.event, name='event'),
    path('details', views.details, name='details'),
    path('admissions', views.admissions, name='admissions'),





]