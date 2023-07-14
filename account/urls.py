from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign-up"),
    path("sign-in/", views.sign_in, name="sign-in"),
    path("sign-out/", views.sign_out, name="sign-out"),
    path("reset-password/", views.reset_password, name="reset-password"),
    path("verify-email/<uidb64>/", views.account_activate_view, name="activate"),
    path("new-password/<uidb64>/", views.new_password_view, name="new-password"),
]
