from django.shortcuts import render

#подключаем определение времени
from django.utils import timezone

#404 error
from django.shortcuts import render, get_object_or_404

#включаем модли определенные в соседнем (".") файле models.py
from .models import Post

# Create your views here.
def post_list(request):
    #создали переменную QuerySet: posts
    #теперь мы можем обращаться к нему, используя имя
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'askans/post_list.html', {'posts': posts})
# return HttpResponse('Hello,world!');

def hot_list(request):
    posts = Post.objects.filter() #рейтинг orderz-by
    return render(request, 'askans/hot_list.html', {'post':posts})

#пока пробно с post моделью
def question(request, id):
    q = get_object_or_404(Post, id=id) #QuerySet q, который пердаетм в шаблон
    return render(request, 'askans/question.html', {'q': q})

#с тэгами
def tag_list(request, tag):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'askans/tag_list.html', {'posts': posts})
################################доделать#####################################
def login(request):
    return render(request, 'askans/login.html')

def signup(request):
    return render(request, 'askans/signup.html')

def ask (request):
    return render(request, 'askans/ask.html')
#####################################################################
def index_list(request):
    return render(request, 'askans/index_list.html')