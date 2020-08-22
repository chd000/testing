from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models

WORKING_AT = (
    ('GA-36', 'ГА-36'),
    ('GAC', 'ГАЦ'),
    ('CSU', 'ЦСЮ')
)


class Questions(models.Model):
    Q_TYPE = (
        ('1', 'Выберите варианты ответов'),
        ('2', 'Порядок элементов'),
    )

    quest = models.CharField('Вопросы', max_length=150)
    answers = models.TextField('Ответы')
    right_answer = models.TextField('Правильные ответы', blank=True, null=True)
    picture = models.ImageField('Изображения', upload_to='', null=True, blank=True, max_length=255)
    quest_type = models.CharField('Тип вопроса', max_length=1, choices=Q_TYPE, blank=True)
    answered_wrong = models.IntegerField('Неправильно ответили раз', default=0, blank=True, null=True)

    def __str__(self):
        return self.quest

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('У пользователя должен быть адрес электронной почты')

        user = self.model(email=self.normalize_email(email), )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(email, password=password, )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password, )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='Адрес электронной почты', max_length=255, unique=True, )
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100)
    working_at = models.CharField('Место работы', max_length=50, choices=WORKING_AT, blank=True)
    active = models.BooleanField('Активный пользователь', default=True)
    staff = models.BooleanField('Модератор', default=False)
    admin = models.BooleanField('Админ', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    class Meta:
        verbose_name = 'Пользователь сайта'
        verbose_name_plural = 'Пользователи сайта'


class ResultTable(models.Model):
    email = models.EmailField(verbose_name='Адрес электронной почты', max_length=255, )
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    working_at = models.CharField('Место работы', max_length=50, choices=WORKING_AT)
    middle_name = models.CharField('Отчество', max_length=100)
    passing_test_date = models.DateTimeField('Дата прохождения теста', auto_now_add=True, )
    right_ans_percent = models.IntegerField('Процент правильных ответов', null=True, blank=True)
    mark = models.IntegerField('Баллы')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты теста'
