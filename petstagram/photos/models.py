from django.core.validators import MinLengthValidator
from django.db import models


class Photo(models.Model):
    DESC_MAX_LEN = 300
    LOCATION_MAX_LEN = 30
    LOCATION_MIN_LEN = 10

    photo = models.ImageField(
        null=False,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
        max_length=DESC_MAX_LEN,
        validators=[
            MinLengthValidator(LOCATION_MIN_LEN)
        ],
    )

    location = models.TextField(
        null=True,
        blank=True,
        max_length=LOCATION_MAX_LEN,
    )

    date_of_publication = models.DateField(
        null=False,
        blank=False,
        auto_now=True,
    )
