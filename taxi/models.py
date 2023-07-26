from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> models.CharField:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self) -> models.CharField:
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=63,
        unique=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "driver",
        verbose_name_plural = "drivers"