from django.urls import path, include

from petstagram.accounts.views import register_user, login_user, details_page, edit_page, delete_page

urlpatterns = (
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('profile/', include([
        path('<int:pk>', details_page, name='details page'),
        path('<int:pk>/edit/', edit_page, name='edit page'),
        path('<int:pk>/delete/', delete_page, name='delete page')
    ]))
)
