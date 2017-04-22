#подключаем определение времени
from django.utils import timezone
#пагинатор
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#404 error
from django.shortcuts import render, get_object_or_404
from django.http import Http404
#включаем модли определенные в соседнем (".") файле models.py
from .models import Question

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

    # текущая страница
    index = res_page.number - 1
    max_index = len(paginator.page_range)
    # границы диапазона
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # новый диапазон
    page_range = paginator.page_range[start_index:end_index]

    return res_page, page_range



# Create your views here.
def post_list(request):
    #создали переменную QuerySet: posts
    #теперь мы можем обращаться к нему, используя имя
    posts_all = Question.objects.filter().order_by('published_date')

    #page,paginator = paginate(posts_all,request)

    posts, page_range = paginate(posts_all, request)

    return render(request, 'askans/post_list.html', {'page': posts, 'page_range': page_range})

    #return HttpResponseRedirect(reverse('post_list', {'posts': posts}))


def hot_list(request):
    posts = Question.objects.filter() #рейтинг orderz-by
    return render(request, 'askans/hot_list.html', {'posts':posts})

#пока пробно с post моделью
def question(request, id):
    q = get_object_or_404(Question, id=id) #QuerySet q, который пердаетм в шаблон
    return render(request, 'askans/question.html', {'q': q})

#с тэгами
def tag_list(request, tag):
    posts = Question.objects.order_by('published_date')

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