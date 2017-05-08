#подключаем определение времени
from django.contrib.auth import authenticate
from django.utils import timezone
#пагинатор
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#404 error
from django.shortcuts import render, get_object_or_404
from django.http import Http404
#включаем модли определенные в соседнем (".") файле models.py
from django.views import View

from askans import forms
from askans.forms import LoginForm, SignUpForm
from .models import Question, Answer
from django.shortcuts import redirect
from django.contrib import auth

from django.urls import reverse

from django.http import HttpResponse, JsonResponse


def paginate(objects_list, request):

    one_page = request.GET.get('page', 1)

    ###################################
    paginator = Paginator(objects_list, 5)  # по 2 на страницу
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

def post_list(request):
    #создали переменную QuerySet: posts
    #теперь мы можем обращаться к нему, используя имя
    posts_all = Question.objects.last_questions()

    #page,paginator = paginate(posts_all,request)

    posts, page_range = paginate(posts_all, request)

    return render(request, 'askans/post_list.html', {'page': posts, 'page_range': page_range})

    #return HttpResponseRedirect(reverse('post_list', {'posts': posts}))

def hot_list(request):
    posts_all = Question.objects.hot_questions()
    posts, page_range = paginate(posts_all, request)
    return render(request, 'askans/hot_list.html', {'page': posts, 'page_range': page_range})

#пока пробно с post моделью
def question(request, id):
    q = get_object_or_404(Question, id=id) #QuerySet q, который пердаетм в шаблон
    answers = Answer.objects.filter(question__id=id)

    posts, page_range = paginate(answers, request)

    return render(request, 'askans/question.html', {'q': q, 'page': posts, 'page_range': page_range})

#с тэгами
def tag_list(request,tag_name=None):
    posts = Question.objects.last_questions()
    return render(request, 'askans/tag_list.html', {'posts': posts})
################################доделать############################
def login(request):

    # if request.method == 'POST':
    #     login = request.POST.get('login')
    #     password = request.POST.get('password')
    #     url = request.POST.get('continue','/')
    #     sessid = do_login(login, password)
    #     if sessid:
    #         response = HttpResponseRedirect(url)
    #         import datetime
    #         from datetime import timedelta
    #         response.set_cookie('sessid', sessid,
    #                             domain='.askans.ru',
    #                             httponly=True
    #                             )
    #         return response
    #     else:
    #         error = u'Неверный логин/пароль'
    #     return render(request, login, {'error': error})

    user = request.user
    if user.is_authenticated():
        print('User is_authenticated')
        print(user.username)
        return redirect('post_list')

    next_page = request.GET.get('next')
    if next_page is None:
        next_page = 'post_list'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth.login(request, form.user)
            print(form.user.username)
            return redirect(next_page) #возврат на предыдущую страницу
    else:
        form = forms.LoginForm()

    return render(request, 'askans/login.html', {'form': form})


def signup(request):
    user = request.user

    if user.is_authenticated():
        return redirect('post_list')

    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            auth.login(request, user)

            ####################
            # username = request.POST['username']
            # password = request.POST['password']
            # u = authenticate(request, username=username, password=password)
            # auth.login(request, u)
            ####################

            return redirect('post_list')
    else:
        form = forms.SignUpForm()

    return render(request, 'askans/signup.html', {
        'form': form,
    })

def ask(request):
    return render(request, 'askans/ask.html')
#####################################################################
def index_list(request):
    return render(request, 'askans/index_list.html')

def logout(request):

    print(request.get_host())
    auth.logout(request)
    next_page = request.GET.get('next')
    if next_page:
        return redirect(next_page)
    else:
        return redirect('login')



            # class UserFormView(View):
#     form_class = UserForm
#     return render()