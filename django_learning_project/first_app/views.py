from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
course_dictionary = {
    "python": "Python Course Page",
    "java": "Java Course Page",
    "kotlin": "Kotlin Course Page",
    "swift": "Swift Course Page",
}


def index(request):
    return HttpResponse("This is first Django project, first index")


def python_course(request):
    return HttpResponse("Python Course Page")


def java_course(request):
    return HttpResponse("Java Course Page")


def choose_course(request, courseItem):
    try:
        course = course_dictionary[courseItem]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("Not Found!!! Please look another course!")
        # raise Http404("Not Found!!! Please look another course!")
    # return HttpResponse(course_dictionary.get(courseItem, "Not Found!"))


def multiply(request, num1, num2):
    return HttpResponse(f"{num1} * {num2} = {num1 * num2}")


def course_number_view(request, num1):
    course_list = list(course_dictionary.keys())
    try:
        course = course_list[num1]
        page_to_go= reverse("course", args=[course])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("Not Found!!! Please look another course!")
    '''
        if num1 == 10:
        return HttpResponseRedirect("/kotlin")
    else:
        HttpResponseNotFound("Not Found!!! Please look another course!")
    '''
