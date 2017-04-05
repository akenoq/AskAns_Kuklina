from django.db import models
from django.utils import timezone #подключаем часовой пояс
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        null = True
    )

    ####какие еще поля
    avatar = models.ImageField(
        upload_to = './uploads/avatars/%Y/%m/%d/%H/',
        max_length = 100,
        default = 'ava.jpg'
    )

    def __str__(self):  # метод, возврщющий строку заголовка
        return self.title



class Post(models.Model): # оперделяем модель (обьект Post является моделью - Django мохранит его в БД)
    author = models.ForeignKey('auth.User')  # ссылка на другую модель
	
#    q_id = models.AutoField(primary_key=True) #нельзя просто делать изменения в существующей модели
    
    title = models.CharField(max_length=200) #текстовое поле ограниченное
    text = models.TextField() #неограниченное текстовое поле
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #def - создаем функцию (метод публикации записи)
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #метод, возврщющий строку заголовка
        return self.title