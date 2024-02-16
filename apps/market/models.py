from django.contrib.auth.models import User
from django.db import models


class SocialNetwork(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Social Network'
        verbose_name_plural = 'Social Networks'


class WorkTime(models.Model):
    day = models.CharField(max_length=15)
    time = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return f'{self.day} {self.time}'

    class Meta:
        verbose_name = 'WorkTime'
        verbose_name_plural = 'WorkTimes'


class Company(models.Model):
    about_company = models.TextField(max_length=5000)
    address = models.CharField(max_length=150)
    work_phone = models.CharField(max_length=40)
    social_network = models.ManyToManyField(
        SocialNetwork,
        related_name='social'
    )
    work_time = models.ManyToManyField(
        WorkTime,
        related_name='worktime'
    )
    logo = models.ImageField(
        blank=True,
        null=True,
        upload_to='logo/'
    )

    objects = models.Manager()

    def __str__(self):
        return self.about_company

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,

    )

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
