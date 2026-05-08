from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from .models import User
from .forms import UserRegisterForm, UserLoginForm

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Akun berhasil dibuat! Silakan login.')
        return response

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:home')
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Selamat datang, {user.username}!')
            return redirect('core:home')
        else:
            messages.error(request, 'Username atau password salah.')
            return render(request, 'accounts/login.html', {'form': UserLoginForm()})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Anda telah logout.')
    return redirect('core:home')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
