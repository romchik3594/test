from django.db import models

class IoT(models.Model):
    tempre = models.CharField('Температура', max_length=10)
    gas = models.CharField('СО2', max_length=10)
    punch = models.CharField('Удры', max_length=10)
    liq = models.CharField('Влажность', max_length=10)
    light1 = models.CharField('Свет1', max_length=5)
    light2 = models.CharField('Свет2', max_length=5)
    light3 = models.CharField('Свет3', max_length=5)
    light4 = models.CharField('Свет4', max_length=5)
    

    
    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

