from django.db import models
from django.conf import settings
from catalog.models import Product
from django.utils import timezone
from catalog.models import User
class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(Product, verbose_name="Пост", on_delete=models.CASCADE)
    data = models.DateTimeField('дата', default=timezone.now)
    value = models.PositiveIntegerField(default=0)


    def __str__(self) -> str:
        return f"{self.user}|{self.post}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = 'Корзина'


