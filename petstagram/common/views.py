from django.shortcuts import render, redirect

from petstagram.common.models import Like
from petstagram.photos.models import Photo


def apply_likes_count(photo):
    photo.likes_count = photo.like_set.count()
    return photo


def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def home_page(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'all_photos': photos,
    }

    return render(request, 'common/home-page.html', context=context)


def get_user_liked_current_photo(photo_id):
    return Like.objects.filter(to_photo_id=photo_id)


def like_photo(request, photo_id):
    user_liked_current_photo = get_user_liked_current_photo(photo_id)

    if user_liked_current_photo:
        user_liked_current_photo.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id,
        )

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
