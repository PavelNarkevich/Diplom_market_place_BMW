from django.contrib.auth.models import User
from django.db import models


class Series(models.Model):
    number = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.number

    objects = models.Manager()

    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"


class BodyType(models.Model):
    body = models.CharField(max_length=50, unique=True)

    objects = models.Manager()

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = "Body Type"
        verbose_name_plural = "Body Type"


class EngineType(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "EngineType"


class Transmission(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Transmission"


class Country(models.Model):
    name = models.CharField(
        max_length=15,
        unique=True
    )

    objects = models.Manager()

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
    model = models.CharField(max_length=15)

    photo = models.ImageField(
        upload_to='car_photo/',
        null=True,
        blank=True
    )

    objects = models.Manager()

    def __str__(self):
        return (f"{self.series}"
                f" {self.body} "
                f"{self.body_type}"
                f" {self.engine_code}"
                f" {self.transmission} "
                f"{self.country} "
                f"{self.model}"
                )

    class Meta:
        verbose_name = "Cars"
        verbose_name_plural = "Cars"


class CarElement(models.Model):
    name = models.CharField(max_length=70)
    photo = models.ImageField(
        upload_to='car_element/',
        blank=True,
        null=True
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "car element"
        verbose_name_plural = "car element"


class Component(models.Model):
    name = models.CharField(max_length=70)
    element = models.ForeignKey(
        CarElement,
        on_delete=models.CASCADE,
        related_name="elem"
    )
    car = models.ForeignKey(
        Cars,
        on_delete=models.CASCADE,
        default=None
    )
    photo = models.ImageField(
        upload_to="component/",
        blank=True,
        null=True
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.name} {self.car}'

    class Meta:
        verbose_name = "component"
        verbose_name_plural = "component"


class Details(models.Model):
    name = models.CharField(max_length=70)
    brand = models.CharField(max_length=70)
    number = models.CharField(max_length=70)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    photo = models.ImageField(
        upload_to="details/",
        blank=True,
        null=True,
    )
    component = models.ForeignKey(
        Component,
        on_delete=models.CASCADE,
        related_name="component"
    )
    car = models.ForeignKey(
        Cars,
        on_delete=models.CASCADE,
        default=None
    )
    quantity = models.IntegerField()
    description = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    update_at = models.DateTimeField(auto_now=True)

    object = models.Manager()

    def __str__(self):
        return f"{self.name} {self.number}"

    class Meta:
        verbose_name = "Details"
        verbose_name_plural = "Details"


class Basket(models.Model):
    status_choice = [
        ('P', 'Pending'),
        ('O', 'Ordered'),
    ]

    quantity = models.IntegerField(default=0)
    items = models.ForeignKey(
        Details,
        on_delete=models.CASCADE,
        related_name="basket1",
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    shopper = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=1,
        choices=status_choice,
        default='P'
    )
    object = models.Manager()

    def __str__(self):
        return f'{self.shopper} {self.items}  {self.quantity} {self.price}'

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Basket"
