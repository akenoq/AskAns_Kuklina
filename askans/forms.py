from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from askans.models import Question, User, Person


# class UserForm(forms.ModelForm): #модельформа, прописываем поля, есть таблица соответствия полей подлей и форм => form.save()
#     #в обычной форме метод save() из модели
#
#     password = forms.CharField(widget=forms.PasswordInput, help_text=u'Введите пароль')


# class Meta:
#     model = User
#     fields = ['username','email','password'] #exclude = [] - все поля, которые нужны или явно перечислть

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Login'
    }),required='True')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }),required='True')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        self.user = authenticate(username=username, password=password)

        if self.user is None:
            raise forms.ValidationError('Incorrect login or password')


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Login'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))

    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password'
    }))

    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={
    }))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Login is already exists!')
        return username

    def clean_repeat_password(self):
        data = self.cleaned_data
        if data['password'] != data['repeat_password']:
            raise forms.ValidationError('Different passwords!')
        return data['repeat_password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Email is already exists!')
        return email

    def save(self):
        data = self.cleaned_data
        username = data['username']
        email = data['email']
        password = data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        if self.cleaned_data['avatar'] is not None:
            profile = Person(user=user, avatar=self.cleaned_data['avatar'])
            profile.save()
        else:
            profile = Person(user=user)
            profile.save()