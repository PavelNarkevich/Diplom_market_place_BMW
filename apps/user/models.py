from django.contrib.auth.models import User
from apps.catalog.models import Cars

from django.db import models


class Garage(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    cars = models.ManyToManyField(
        Cars,
        null=True,
        blank=True,
    )

    object = models.Manager()

    def __str__(self):
        return f"{self.user} - {self.cars}"

    class Meta:
        verbose_name = "Garage"
        verbose_name_plural = "Garage"
