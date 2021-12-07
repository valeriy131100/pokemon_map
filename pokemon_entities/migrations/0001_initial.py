# Generated by Django 3.1.13 on 2021-12-07 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Английское название')),
                ('title_jp', models.CharField(blank=True, max_length=200, null=True, verbose_name='Японское название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('previous_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.pokemon', verbose_name='Из кого эволюционирует')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('appeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Появится')),
                ('disappeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Исчезнет')),
                ('Level', models.IntegerField(blank=True, null=True, verbose_name='Уровень')),
                ('Health', models.IntegerField(blank=True, null=True, verbose_name='Здоровье')),
                ('Strength', models.IntegerField(blank=True, null=True, verbose_name='Сила')),
                ('Defence', models.IntegerField(blank=True, null=True, verbose_name='Защита')),
                ('Stamina', models.IntegerField(blank=True, null=True, verbose_name='Выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Покемон')),
            ],
        ),
    ]
