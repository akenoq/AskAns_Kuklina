from django.db import models
from django.utils import timezone #подключаем часовой пояс
from django.contrib.auth.models import User
from django.contrib import admin #для отображения в admin

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
        return self.user.username

# class Tag(models.Model):
#     tag_name = models.CharField(max_length=20)

# class Post(models.Model): # оперделяем модель (обьект Post является моделью - Django мохранит его в БД)
#     author = models.ForeignKey('auth.User')  # ссылка на другую модель, можлино без aith если ипортировaли
#
#     title = models.CharField(max_length=200) #текстовое поле ограниченное
#     text = models.TextField() #неограниченное текстовое поле
#
#     # raiting = models.IntegerField()
#     #tags = models.ManyToManyField(Tag)
#
#     created_date = models.DateTimeField(default=timezone.now) # =datatime.now
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self): #def - создаем функцию (метод публикации записи)
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self): #метод, возврщющий строку заголовка
#         return self.title

class QuestionManager(models.Manager):

    def hot_questions(self):
        return self.order_by('rating')

    def last_questions(self):
        return self.order_by('published_date')

    def publish(self):  # def - создаем функцию (метод публикации записи)
        self.published_date = timezone.now()
        self.save()

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Person)
    published_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True, default='')
    rating = models.IntegerField(default=0)

    objects = QuestionManager()

    def __str__(self):  # метод, возврщющий строку заголовка
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Post, on_delete = models.CASCADE) #удаляется с удалением родительского
    text = models.TextField()
    author = models.ForeignKey(Person)
    published_date = models.DateTimeField(auto_now_add = True)
    correct = models.BooleanField(default=False)

    #objects = AnswerManager()

    def __str__(self):
        return self.text

class QuestionLike(models.Model):
    user = models.ForeignKey(Person)
    question = models.ForeignKey(Post)
    like = models.BooleanField()

class AnswerLike(models.Model):
    user = models.ForeignKey(Person)
    answer = models.ForeignKey(Answer)
    like = models.BooleanField()