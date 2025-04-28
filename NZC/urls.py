from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('pdf', views.pdf, name='pdf'),
    path('manual', views.manual, name='manual'),
    path('process_pdf', views.process_pdf, name='process_pdf'),
    path('results', views.results, name='results'),
]