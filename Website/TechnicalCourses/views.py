from django.shortcuts import render
from django.http import HttpResponse

def Courses(reques):
    return HttpResponse('<h1>This is my Home Page</h1>')

def Details(request,course_id):
    return HttpResponse('<h2>These are course details for course_id:' + str(course_id)+'</h2>')


