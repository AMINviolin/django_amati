from django.shortcuts import render
from .models import Courses
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def Maincourse(request,cat=None,teacher=None):
    if cat:
        courses = Courses.objects.filter(category__name=cat)
    elif teacher:
        courses = Courses.objects.filter(teacher__info__username = teacher)
    elif request.GET.get('search'):
        courses = Courses.objects.filter(content__contains=request.GET.get('search'))
    else:
        courses = Courses.objects.filter(status = True)


    courses = Paginator(courses,3)
    first_page = 1
    last_page = courses.num_pages
    try:
        page_number = request.GET.get('page')
        courses = courses.get_page(page_number)

    except EmptyPage:
        courses = courses.get_page(1)

    except PageNotAnInteger:
        courses = courses.get_page(1)



    context = {
        'maincourse': courses,
        'first_page':first_page,
        'last_page':last_page,
    }
    return render(request,"courses/courses.html",context=context)