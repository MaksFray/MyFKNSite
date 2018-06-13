from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse



# Модель категории
from user_shop.models import UserProfiler


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])


# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Класс", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Ник")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Скрин персонажа")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Привязан к аккаунту")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])


class Comment(models.Model):
    class Meta:
        db_table = "comments"
        ordering = ['article_id']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'


    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Фото")
    article_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата комментария', auto_now_add=True)

    def __str__(self):
        return self.content[0:200]

