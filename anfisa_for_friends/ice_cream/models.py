from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(default=100, 
                                                    verbose_name='Порядок отображения')
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    
    class Meta:
        verbose_name = 'топинг'
        verbose_name_plural = 'Топинги'


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256,
        help_text='Уникальное название обёртки, не более 256 символов')

    class Meta:
        verbose_name = 'обёртка'
        verbose_name_plural = 'Обёртки'

class IceCream(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'мороженое'
