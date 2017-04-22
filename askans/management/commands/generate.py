import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from askans.models import Person, Question, Answer, Tag, QuestionLike, AnswerLike


class Command(BaseCommand):

    def gettext(self, n):
        gentext = random.choice(
            ["Ругается на строчку import",
             "Библиотека AFMotors не подключается к Arduino Leonardo, с Uno все работает корректно",
             "Как оказалось, в новом JS есть классы",
             "Чтобы все работало нормально, лучше использовать фреймворк",
             "Наверное, стоит прочитать книгу по алгоритмам, но все же, что мне выбрать?",
             "Неужели придется сносить базу данных и историю миграций?",
             "Никак не могу найти ошибку, но компилятор ругается на строчку"]
        ) * random.randint(1, n)
        return gentext

    def handle(self, *args, **options):

        # USER
        for u in range(0, 15):

            str1 = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
            ls = list(str1)
            # Тщательно перемешиваем список
            random.shuffle(ls)
            # Извлекаем из списка 5 произвольных значений
            str2 = ''.join([random.choice(ls) for x in range(7)])

            uu = User(
                email=str2 + "@mail.ru",
                username="user" + str2,
                password='1234567nk'
            )
            uu.save()

            pp = Person(
                user = uu,
                avatar = '/' + str(u) + '.jpg'
            )
            pp.save()

        users = Person.objects.all()

        # TAG
        for t in range(0, 15):
            try:
                ttt = Tag(name=random.choice(["ibm", "bluemix", "python", "arduino", "c++", "patterns", "javascript", "raspberry", "django", "html"]))
                ttt.save()
            except Exception:
                pass
        tags = Tag.objects.all()

        # QUESTIONS
        for q in range(0, 50):
            qq = Question(
                title=random.choice(
                    ["В чем может быть ошибка?",
                     "Как подключить библиотеку Arduino Leonardo?",
                     "Как подключить библиотеку С++?",
                     "Как избежать html инъекций?",
                     "В новом JS есть классы?",
                     "Какие алгоритмы сортировки лучше использовать?"
                     "Почему не работают миграции?",
                     "Когда будем готовы к хакатону?"]
                ) + str(q) + '?',

                text=self.gettext(20),
                author=random.choice(users)
            )

            with transaction.atomic():
                qq.save()

            for i in range(0, random.randint(0, 3)):
                qq.tags.add(random.choice(tags))

        questions = Question.objects.all()

        # ANSWER
        for i in range(0, 100):
            Answer(
                text=self.gettext(10),
                question=random.choice(questions),
                author=random.choice(users)
            ).save()
        answers = Answer.objects.all()

        # QLIKE
        for i in range(0, 200):
            ll = QuestionLike(
                question=random.choice(questions),
                user=random.choice(users),
                like=bool(random.randint(0, 1))
            )
            ll.save()

            if ll.like:
                ll.question.rating += 1
            else:
                ll.question.rating -= 1
            ll.question.save()

        # ALIKE
        for i in range(0, 200):
            ll = AnswerLike(
                answer=random.choice(answers),
                user=random.choice(users),
                like=bool(random.randint(0, 1))
            )
            ll.save()
            if ll.like:
                ll.answer.rating += 1
            else:
                ll.answer.rating -= 1
            ll.answer.save()