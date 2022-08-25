from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название товара',
        help_text='введите название товара',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена товара',
        help_text='Добавьте цену товара',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор объявления',
        help_text='Выберите автора объявления',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания объявления',
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=1000,
        verbose_name='Описание товара',
        help_text='Введите описание товара',
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='фото',
        help_text='Разместите фото для объявления',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'
        ordering = ('-created_at',)


class Comment(models.Model):
    text = models.CharField(
        max_length=2000,
        verbose_name='Комментарий',
        help_text='Оставьте свой комментарий здесь',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
        help_text='Выберите автора комментария',
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Объявления',
        help_text='Объявление, к которому относится комментарий',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания комментария',
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_at',)
