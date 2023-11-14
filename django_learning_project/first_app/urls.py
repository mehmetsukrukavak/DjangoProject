from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("python/", views.python_course, name="python"),
    path("java/", views.java_course, name="java"),
    path("<int:num1>/", views.course_number_view, name="coursenumberview"),
    path("<str:courseItem>/", views.choose_course, name="course"),
    path("<int:num1>/<int:num2>/", views.multiply, name="multiply"),
    path("<int:num1>/", views.course_number_view, name="coursenumberview")

]