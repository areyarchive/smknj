from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('profil/', views.ProfileView.as_view(), name='profile'),
    path('program/', views.ProgramListView.as_view(), name='program_list'),
    path('program/<slug:slug>/', views.ProgramDetailView.as_view(), name='program_detail'),
    path('berita/', views.NewsListView.as_view(), name='news_list'),
    path('berita/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
