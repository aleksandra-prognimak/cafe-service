from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from cafe_service import settings


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="dishes"
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes"
    )

    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self):
        return f"{self.name} ({self.dish_type}, ${self.price})"


class Cook(AbstractUser):
    MIN_YEARS_OF_EXPERIENCE = 0
    MAX_YEARS_OF_EXPERIENCE = 80

    years_of_experience = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(MIN_YEARS_OF_EXPERIENCE),
            MaxValueValidator(MAX_YEARS_OF_EXPERIENCE),
        ]
    )

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
