from django.contrib import admin

# Register your models here.

from .models import Post
admin.site.register(Post) #модель доступна на панели администрирования

from .models import Person
admin.site.register(Person) #модель доступна на панели администрирования


