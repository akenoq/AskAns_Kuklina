from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from askans.models import Question, User, Person, Tag, Answer
from askans.my import normalString


# class UserForm(forms.ModelForm): #модельформа, прописываем поля, есть таблица соответствия полей подлей и форм => form.save()
#     #в обычной форме метод save() из модели
#
#     password = forms.CharField(widget=forms.PasswordInput, help_text=u'Введите пароль')


# class Meta:
#     model = User
#     fields = ['username','email','password'] #exclude = [] - все поля, которые нужны или явно перечислть

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Login',
        'id': 't1'
    }), required='True')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 't2'
    }), required='True')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        self.user = authenticate(username=username, password=password)

        if self.user is None:
            raise forms.ValidationError('Incorrect login or password')


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Login'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat password'
    }))

    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={
    }))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Login is already exists!')
        if normalString(username) == False:
            raise forms.ValidationError('Prohibited char!')
        return username

    def clean_repeat_password(self):
        data = self.cleaned_data
        if data['password'] != data['repeat_password']:
            raise forms.ValidationError('Different passwords!')
        return data['repeat_password']

    def clean_email(self):
        email = self.cleaned_data['email']
        # if not email
        #     raise forms.ValidationError('Not email format')
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


class AskForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Enter the title here'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control input-lg', 'placeholder': 'Enter your question here', 'rows': 20}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Enter tags separated by comma'}))

    def save(self, user_id):
        data = self.cleaned_data
        profile_id = User.objects.get(id=user_id).person.id
        question = Question(title=data['title'], text=data['text'], author_id=profile_id)
        question.save()
        tags = self.cleaned_data['tags'].split(',')
        for new_tag in tags:
            if new_tag[0] == ' ':
                new_tag = new_tag[1:]
            tag = Tag.objects.filter(name=new_tag)
            if len(tag) == 0:
                tag = Tag(name=new_tag)
                tag.save()
            else:
                tag = tag[0]

            tag.save()
            question.tags.add(tag)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control input-lg', 'placeholder': 'Enter your answer here', 'rows': 5, }))

    def save(self, question_id, user_id):
        data = self.cleaned_data
        profile_id = User.objects.get(id=user_id).person.id
        answer = Answer(text=data['text'], question_id=question_id, author_id=user_id)
        print(answer.text)
        print(answer.question.title)
        answer.save()


class SettingsForm(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg' })).disabled

    email = forms.EmailField(widget=forms.EmailInput(attrs={ 'class': 'form-control input' }))

    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={ 'class': 'form-control input' }))

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if self.fields['username'].has_changed(initial=self.initial['username'], data=username):
    #         if User.objects.filter(username=username).exists():
    #             raise forms.ValidationError('Login already exists!')
    #     return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if self.fields['email'].has_changed(initial=self.initial['email'], data=email):
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email already exists!')
        return email

    def save(self, user_id):
        data = self.cleaned_data
        profile_id = User.objects.get(id=user_id).person.id
        user = Person.objects.get(id = profile_id)
        # user.username = data['username']
        user.email = data['email']
        if data['avatar'] is not None:
            user.avatar = data['avatar']
        user.save()
