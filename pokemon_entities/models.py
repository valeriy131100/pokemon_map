from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Английское название'
    )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Японское название'
    )
    image = models.ImageField(
        blank=True,
        verbose_name='Изображение')
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Из кого эволюционирует',
        related_name='next_evolutions'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Покемон',
        related_name='entities'
    )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Появится'
    )
    disappeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Исчезнет'
    )
    Level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Уровень'
    )
    Health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Здоровье'
    )
    Strength = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Сила'
    )
    Defence = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Защита'
    )
    Stamina = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Выносливость'
    )
