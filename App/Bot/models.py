from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models





class MatchingStrings(models.Model):
     string = models.CharField(max_length=100)
     ticket = models.ForeignKey('Tickets', on_delete=models.CASCADE, related_name='matchings')

     class Meta:
        verbose_name = "Соответствие"
        verbose_name_plural = "Соответствия"
        ordering = ['string']
        db_table = 'matching_strings'


class Tickets(models.Model):
    user_telegram_id = models.IntegerField()
    user_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"
        ordering = ['user_name']
        db_table = 'tickets'


class Channels(models.Model):
     name = models.CharField(max_length=100)
     channel_id = models.CharField(max_length=100, null = False)

     class Meta:
        verbose_name = "Канал"
        verbose_name_plural = "Каналы"
        ordering = ['name']
        db_table = 'channels'


    