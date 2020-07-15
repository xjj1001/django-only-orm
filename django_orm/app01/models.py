
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'user'
        verbose_name = u'用户表'
        verbose_name_plural = u'用户表'
    objects = models.manager


class Record(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'user_record'
        verbose_name = u'用户记录表'
        verbose_name_plural = u'用户记录表'

    objects = models.manager