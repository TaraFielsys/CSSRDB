
from django.urls import path
from . import views

urlpatterns = [
    path('analysis.html', views.analysis, name='analysis'),
    path('index.html', views.index, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('documentation.html', views.documentation, name='documentation'),
    path('gallery.html', views.gallery, name='gallery'),
    path('result.html',  views.result, name='result'),
    path('', views.home, name='home'),
    path('api/analyze/', views.analyze, name='analyze'), 
]
