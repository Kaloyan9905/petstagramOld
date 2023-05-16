from django.core.exceptions import ValidationError


def validate_file_size(image):
    if image.size > 5242880:
        raise ValidationError("The file size should be less than 5MB!")
