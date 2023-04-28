from django.shortcuts import render


def login_user(request):
    return render(request, 'account/login-page.html')


def register_user(request):
    return render(request, 'account/register-page.html')


def delete_page(request, pk):
    return render(request, 'account/profile-delete-page.html')


def details_page(request, pk):
    return render(request, 'account/profile-details-page.html')


def edit_page(request, pk):
    return render(request, 'account/profile-edit-page.html')
