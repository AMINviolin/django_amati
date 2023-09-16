from django.shortcuts import render,get_object_or_404
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

def course_detail(request,id):
    # try:
        course = Courses.objects.get(id=id)
        id_list = []
        course = Courses.objects.filter(status = True)
        for cr in course :
            id_list.append(cr.id)
        
        if id_list[0] == id:
            next_course = Courses.objects.get(id=id_list[1])
            previous_course =None

        elif id_list[-1] == id:
            next_course = None
            previous_course = Courses.objects.get(id=id_list[-2])

        else:
            next_course = Courses.objects.get(id=id_list[id_list.index(id)+1])
            previous_course = Courses.objects.get(id=id_list[id_list.index(id)-1])



        course.counted_views += 1
        course.save()
        context = {
            'course': course,
            'next_course': next_course,
            'previous_course': previous_course,
        }
        return render(request,"courses/course-details.html",context=context)
    # except:
    #     return render(request,'courses/404.html')
