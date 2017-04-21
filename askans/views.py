#подключаем определение времени
from django.utils import timezone
#пагинатор
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#404 error
from django.shortcuts import render, get_object_or_404
from django.http import Http404
#включаем модли определенные в соседнем (".") файле models.py
from .models import Post

from django.urls import reverse
from django.http import HttpResponseRedirect




def paginate(objects_list, request):

    one_page = request.GET.get('page')

    ###################################
    paginator = Paginator(objects_list, 2)  # по 2 на страницу
    ###################################

    try:
        res_page = paginator.page(one_page)
    except PageNotAnInteger: # If page is not an integer, deliver first page.
        # res_page = paginator.page(1)
        raise Http404("Incorect page number")
    except EmptyPage: # If page is out of range (e.g. 9999), deliver last page of results.
        res_page = paginator.page(paginator.num_pages)

    return res_page



# Create your views here.
def post_list(request):
    #создали переменную QuerySet: posts
    #теперь мы можем обращаться к нему, используя имя
    posts_all = Post.objects.filter().order_by('published_date')

    #page,paginator = paginate(posts_all,request)

    posts = paginate(posts_all, request)

    return render(request, 'askans/post_list.html', {'posts': posts})

    #return HttpResponseRedirect(reverse('post_list', {'posts': posts}))


def hot_list(request):
    posts = Post.objects.filter() #рейтинг orderz-by
    return render(request, 'askans/hot_list.html', {'posts':posts})

#пока пробно с post моделью
def question(request, id):
    q = get_object_or_404(Post, id=id) #QuerySet q, который пердаетм в шаблон
    return render(request, 'askans/question.html', {'q': q})

#с тэгами
def tag_list(request, tag):
    posts = Post.objects.order_by('published_date')

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