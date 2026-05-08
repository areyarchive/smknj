from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib import messages
from .models import Program, News, Profile, ContactMessage

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programs'] = Program.objects.filter(is_active=True)[:6]
        context['news'] = News.objects.filter(is_published=True)[:3]
        context['profile'] = Profile.objects.first()
        return context

class ProfileView(TemplateView):
    template_name = 'core/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

class ProgramListView(ListView):
    model = Program
    template_name = 'core/program_list.html'
    context_object_name = 'programs'
    
    def get_queryset(self):
        return Program.objects.filter(is_active=True)

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'core/program_detail.html'
    context_object_name = 'program'
    slug_url_kwarg = 'slug'

class NewsListView(ListView):
    model = News
    template_name = 'core/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 6
    
    def get_queryset(self):
        return News.objects.filter(is_published=True)

class NewsDetailView(DetailView):
    model = News
    template_name = 'core/news_detail.html'
    context_object_name = 'news'
    slug_url_kwarg = 'slug'
    
    def get_queryset(self):
        return News.objects.filter(is_published=True)

class ContactView(CreateView):
    model = ContactMessage
    template_name = 'core/contact.html'
    fields = ['name', 'email', 'phone', 'subject', 'message']
    success_url = '/contact/'
    
    def form_valid(self, form):
        messages.success(self.request, 'Pesan Anda telah terkirim! Kami akan segera menghubungi Anda.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
