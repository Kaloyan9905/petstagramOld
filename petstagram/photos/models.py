from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size


class Photo(models.Model):
    DESC_MAX_LEN = 300
    DESC_MIN_LEN = 10
    LOCATION_MAX_LEN = 30

    photo = models.ImageField(
        null=False,
        blank=True,
        upload_to='mediafiles/pet-photos',
        validators=[
            validate_file_size,
        ],
    )

    description = models.TextField(
        null=True,
        blank=True,
        max_length=DESC_MAX_LEN,
        validators=[
            MinLengthValidator(DESC_MIN_LEN)
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

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
