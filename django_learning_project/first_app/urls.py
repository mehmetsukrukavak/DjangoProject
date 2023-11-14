from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("python/", views.python_course, name="python"),
    path("java/", views.java_course, name="java"),
    path("<str:courseItem>/", views.choose_course, name="course")
]