from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100) #博客标题
    category = models.CharField(max_length= 50 , blank=True) #博客标签
    date_time =models.DateField(auto_now_add= True) #博客时间
    content = models.TextField(blank= True,null=True)  #博客内容

    def __str__(self):
        return self.title

    class Meta: #按时间降序
        ordering = ['-date_time']