"""aaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
#from django.http import HttpResponse
from askans import views

###НУЖНО???###
#from askans import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #??????url(r'^my/', askans.urls),

	#не работает такой способ
	#url(r'^blog/', include('askans.urls'))

    #вывод главной страницы берет из вьюшки постлист
    url(r'^$', views.post_list, name='post_list'),
    url(r'^hot/$', views.hot_list, name='hot_list'), #дописать фильтрацию по тэгу во view
    url(r'^tag/(?P<tag_name>.+)/$', views.tag_list, name='tag_list'),  # \w буквы и цифры . все символы
    #############################по мануалу##################################
	#url(r'^$', views.index_list, name='index_list'), #корень сайта
    ###############################################################

#	url(r'^ask/'.views.ask, name='ask'),
	url(r'^question/(?P<id>[0-9]+)/$', views.question, name='question'), #http://127.0.0.1:8000/question/12345('+'=>...)/, а представление передается в качестве переменной q_id

    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^ask/$', views.ask, name='ask'),

    url(r'^logout/$', views.logout, name='logout'),

    url(r'^settings/$', views.settings, name='settings'),
    #############################не выходило##################################

    # url(r'^like_question/$', views.like_question, name = 'like_question'),
    # url(r'^like_answer/$', views.like_answer, name = 'like_answer'),
    # url(r'^correct/$', views.correct_answer, name = 'correct')

    url(r'^summa/$', views.summa, name = 'summa'),
    url(r'^summa2/', views.summa2, name = 'summa2')

#???	url(r'^tag/(?P<tag>[0-9]+)/$') ??
#	url(r'^settings', view.settings, name='settings'),
#	url(r'^login', view.login, name='login'),
#	url(r'^register', view.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)