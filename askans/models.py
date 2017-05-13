from django.db import models
from django.utils import timezone #подключаем часовой пояс
from django.contrib.auth.models import User
from django.contrib import admin #для отображения в admin
from django.core.urlresolvers import reverse
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

class QuestionManager(models.Manager):

    def hot_questions(self):
        return self.order_by('-rating')

    def last_questions(self):
        return self.order_by('published_date')

    def publish(self):  # def - создаем функцию (метод публикации записи)
        self.published_date = timezone.now()
        self.save()

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Person)
    published_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True, default='')
    rating = models.IntegerField(default=0)

    objects = QuestionManager()

    def get_absolute_url(self):
        return reverse('question', kwargs={'id': self.id})

    def __str__(self):  # метод, возврщющий строку заголовка
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE) #удаляется с удалением родительского
    text = models.TextField()
    author = models.ForeignKey(Person)
    published_date = models.DateTimeField(auto_now_add = True)
    correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    #objects = AnswerManager()

    def __str__(self):
        return self.text

class QuestionLike(models.Model):
    user = models.ForeignKey(Person)
    question = models.ForeignKey(Question)
    like = models.BooleanField()

class AnswerLike(models.Model):
    user = models.ForeignKey(Person)
    answer = models.ForeignKey(Answer)
    like = models.BooleanField()