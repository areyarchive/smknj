from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('guru', 'Guru'),
        ('siswa', 'Siswa'),
        ('orang_tua', 'Orang Tua'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='siswa')
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
