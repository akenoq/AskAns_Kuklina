#подключаем определение времени
import math
from django.contrib.auth import authenticate
from django.utils import timezone
#пагинатор
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#404 error
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404
#включаем модли определенные в соседнем (".") файле models.py
from django.views import View

from askans import forms
from askans.forms import LoginForm, SignUpForm, AnswerForm, SettingsForm
from .models import Question, Answer, Tag
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

def tag_list(request, tag_name):
    t = get_object_or_404(Tag, name = tag_name)
    posts_all = Question.objects.tag_questions(t.name)
    posts, page_range = paginate(posts_all, request)
    return render(request, 'askans/tag_list.html', {'page': posts, 'page_range': page_range, 'tag_name':t.name })

#пока пробно с post моделью
def question(request, id):
    q = get_object_or_404(Question, id=id) #QuerySet q, который пердаетм в шаблон

    answers = Answer.objects.filter(question__id=id)  # __
    posts, page_range = paginate(answers, request)

    user = request.user

    if request.method == 'POST':
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            # новый ответ в переменную, чтобы дальше найти совпадение в кверисете
            # и вернуть id совпавшего ответа => он и является якорем
            new_ans = form.save(id, user.id)
            answers = Answer.objects.filter(question__id=id)
            i = 1
            for ans in answers:
                if ans == new_ans:
                    ans_id = ans.id
                    break
                i = i + 1
            page = math.ceil(i / 5)  # определяем страницу
            ans_id = None
            paginator = Paginator(answers, 3)
            return redirect('/question/{}?page={}#ans_{}'.format(id, page, ans_id))
    else:
        form = forms.AnswerForm()

    return render(request, 'askans/question.html', {'q': q, 'page': posts, 'page_range': page_range, 'form': form})

# #с тэгами
# def tag_list(request,tag_name=None):
#     posts = Question.objects.last_questions()
#     return render(request, 'askans/tag_list.html', {'posts': posts})
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
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
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
    user = request.user
    if not user.is_authenticated():
        return redirect('login')
    if request.method == 'POST':
        form = forms.AskForm(request.POST)
        if form.is_valid():
            question = form.save(user.id)
            return redirect(question.get_absolute_url())
    else:
        form = forms.AskForm()
    return render(request, 'askans/ask.html', {'form': form})


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


def settings(request):
    user = request.user

    if not user.is_authenticated():
        return redirect('post_list')

    data = {'email': user.email} #данные юзера

    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES, initial=data)
        if form.is_valid():
            form.save(user.id)
    else:
        form = forms.SignUpForm(initial= data)

    return render(request, 'askans/settings.html', {
        'form': form
    })


class ClassJSON:
    def createFields(self):
        self.massNames = [];
        self.massValues = [];
        self.n = 0;
    def addElement(self, name,value):
        self.massNames.append(name);
        self.massValues.append(value);
        self.n += 1;
    def getStringJSON(self):
        s = "{";
        for i in range(0,self.n):
            name = self.massNames[i];
            value = self.massValues[i];
            s += ('"' + name + '":"' + value + '"');
            if(i != self.n - 1):
                s += ", ";
        s += "}";
        return s;

def summa(request):
    return render(request, 'askans/zzzSumma.html')

def summa2(request):
    s = request.GET.get('t1')
    mass = []
    mass = s.split("@")

    a = int(mass[0])
    b = int(mass[1])
    sum = a + b

    obj = ClassJSON();
    obj.createFields();

    obj.addElement("summa", str(sum));
    obj.addElement("status", "Yes");
    ss = obj.getStringJSON();

    print(ss);

    return HttpResponse(ss)






    #     class UserFormView(View):
#     form_class = UserForm
#     return render()