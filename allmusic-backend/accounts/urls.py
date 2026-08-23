from django.urls import path

from .views import (
    login_view,
    signup_view,
    check_device,
)


urlpatterns = [

    path(
        "login/",
        login_view,
        name="login"
    ),

    path(
        "signup/",
        signup_view,
        name="signup"
    ),

    path(
        "check-device/",
        check_device,
        name="check_device"
    ),

]