from django.db import models
from helpers.models import BaseModel
from users.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=255, verbose_name='제목',blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = '게시글'

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='게시글')
    content = models.TextField(verbose_name='댓글내용')

    def __str__(self):
        return '%s %s' %(self.id, self.user)
    
    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글'