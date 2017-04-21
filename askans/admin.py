from django.contrib import admin

# Register your models here.

from .models import Post
admin.site.register(Post) #модель доступна на панели администрирования

from .models import Person
admin.site.register(Person)

# from .models import Question
# admin.site.register(Question)

from .models import Answer
admin.site.register(Answer)

from .models import Tag
admin.site.register(Tag)



