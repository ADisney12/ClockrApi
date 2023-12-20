from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello_world, name="index"),
    path("create_user", views.create_user, name ="createUser")
]