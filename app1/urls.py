
from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('staffing/', views.staffing, name='staffing'),
    path('pharmastaffing/', views.pharmastaffing, name='pharmastaffing'),
    path('mobiledevelopment/',views.md,name='md'),
    path('webdevelopment/',views.web,name='web'),
    path('digitalmarketing/',views.digital,name='digital'),
    path('architectures/',views.arch,name='archtec'),
    path('careers/', views.careers, name='career'),
    path('contact/', views.contacts, name='con'),








]