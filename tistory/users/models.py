from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(models.Model):
    email = models.EmailField(verbose_name='이메일', max_length=30, unique=True)
    username = models.CharField(verbose_name='이름', max_length=30)
    password = models.CharField(verbose_name='비밀번호', max_length=30)
    registered_dttm = models.DateTimeField(verbose_name='등록일', auto_now_add=True)
    user_level = models.CharField(max_length=30, verbose_name='사용자 권한', choices=(('normal_user', '일반사용자'), ('admin', '관리자')))

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'blog_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'