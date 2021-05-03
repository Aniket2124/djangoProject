from django.shortcuts import render
from django.http import HttpResponse, Http404
from.models import Allcourses
from django.template import loader
def Courses(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('TechnicalCourses/Courses.html')
    context={
        'ac': ac,

    }
    return HttpResponse(template.render(context,request))

def Details(request,course_id):
    try:
        course=Allcourses.objects.get(pk=course_id)
    except Allcourses.DoesNotExist:
        raise Http404("course not avaible")

    return render(request,'TechnicalCourses/Details.html',{'course': course})


