from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import datetime
from django.db import models
from .utils.utils import *
from django.conf import settings
from django.contrib import admin

from django.utils import timezone
class Gender(models.TextChoices):
    MALE = 'M', 'Мужской'
    FEMALE = 'F', 'Женский'

class Status(models.TextChoices):
    CREATED = 'Создан', 'Создан'
    CANCELLED = 'Отменён', 'Отменён'
    WESTORE = 'На хранении', 'На хранении'
    COMLETED = 'Завершён', 'Завершён'
    INWORK = 'Передан в работу', 'Передан в работу'
    DONE = 'Готов к получению', 'Готов к получению'
class Role(models.TextChoices):
    JUSTUSER = 'JU', 'Пользователь'
    ORDERMANAGER = 'OM', 'Менеджер по заказу'
    PRODUCTMANAGER = 'PM', 'Менеджер по товару'
    OWNER = 'OW', 'Владелец'


class User(AbstractUser):

    first_name = models.CharField('Имя', max_length=150, 
                                     validators=[validate])

    middle_name = models.CharField('Фамилия', max_length=150, 
                                blank=True, validators=[validate])

    last_name = models.CharField('Отчество', max_length=150, 
                                    blank=True, validators=[validate])
    
    phone_number = models.CharField('Телефон', max_length=127,
                                    validators=[validate_phone_number])

    gender = models.CharField('Пол', max_length=1,
                              choices=Gender.choices, blank=True)

    role = models.CharField('Роль', max_length=2,
                              choices=Role.choices, blank=True)

    photo = models.ImageField('Фото', blank=True, 
                                upload_to='avatars/', default='avatars/user.png')

    birthdate = models.DateField('Дата рождения', default=datetime.date.today, blank=True)

    # def get_first_order_date(self):
    #     return self.order_set.order_by('created_at').first().created_at
    
    # def is_client(self):
    #     try:
    #         self.clientprofile
    #         return True
    #     except:
    #         return False


class VanLength(models.Model):
    vanlength = models.CharField(max_length=64, blank=True, null=True, default=None,)
    
    class Meta:
        verbose_name = 'Длина вагона'

    def __str__(self):
        return self.vanlength


class VanType(models.Model):
    vantype = models.CharField(max_length=64, blank=True, null=True, default=None,)

    class Meta:
        verbose_name = 'Тип вагины'

    def __str__(self):
        return self.vantype


class SirviceType(models.Model):
    servicetype = models.CharField(max_length=64, blank=True, null=True, default=None,)

    class Meta:
        verbose_name = 'Тип услуги'

    def __str__(self):
        return self.servicetype


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, validators=[validate])
    typevan = models.ForeignKey(VanType, on_delete=models.CASCADE, verbose_name='Тип вагины')
    lengthvan = models.ForeignKey(VanLength, on_delete=models.CASCADE, verbose_name='Длина вагины')
    servicetype = models.ForeignKey(SirviceType, on_delete=models.CASCADE, verbose_name='Тип услуги')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('snippets:main', kwargs={"slug": self.slug})

    def __str__(self):
        return "%s, %s" % (self.price, self.name)



class HistoryOrders(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь", on_delete=models.CASCADE)
    detail = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    c_companyname = models.CharField(max_length=64, blank=True, null=True, default=None)
    c_address = models.CharField(max_length=64, blank=True, null=True, default=None)
    c_adressetc = models.CharField(max_length=64, blank=True, null=True, default=None)
    c_order_notes = models.CharField(max_length=64, blank=True, null=True, default=None)
    datecreate = models.DateTimeField('Дата создания', default=timezone.now)
    status = models.CharField('Статус', default='Ожидает подтверждения', max_length=30,
                              choices=Status.choices, blank=True)
    def __str__(self):
        return f'{self.user}|{self.user}'
    
