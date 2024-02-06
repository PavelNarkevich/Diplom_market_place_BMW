from django.db import models


class Series(models.Model):
    number = models.IntegerField(max_length=10, unique=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"


class BodyType(models.Model):
    body = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = "Body Type"
        verbose_name_plural = "Body Type"


class EngineType(models.Model):
    type = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Engine Type"


class Transmission(models.Model):
    type = models.CharField(
        max_length=30,
        unique=True
    )

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Transmission"


class Country(models.Model):
    name = models.CharField(
        max_length=15,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"


class Cars(models.Model):
    series = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
    )
    body_type = models.ForeignKey(
        BodyType,
        on_delete=models.CASCADE,
    )
    body = models.CharField(max_length=40)
    engine_type = models.ForeignKey(
        EngineType,
        on_delete=models.CASCADE
    )
    engine_code = models.CharField(max_length=20)
    transmission = models.ForeignKey(
        Transmission,
        on_delete=models.CASCADE,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )