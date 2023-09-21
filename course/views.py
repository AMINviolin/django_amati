from django.shortcuts import render,redirect
from .models import Courses,Comment,Reply
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import CommentForm,ReplyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    if request.method == 'GET':
        # try:
            course = Courses.objects.get(id=id)
            comments = Comment.objects.filter(which_course = id,status = True)
            reply = Reply.objects.filter(status = True)
            id_list = []
            courses = Courses.objects.filter(status = True)
            for cr in courses:
                id_list.append(cr.id)

            id_list.reverse()
            
            if id_list[0] == id :
                next_course = Courses.objects.get(id = id_list[1])
                previous_course = None  

            elif id_list[-1] == id :
                next_course = None
                previous_course = Courses.objects.get(id = id_list[-2])  

            else:
                next_course = Courses.objects.get(id=id_list[id_list.index(id)+1])
                previous_course = Courses.objects.get(id=id_list[id_list.index(id)-1])   


            course.counted_views += 1
            course.save()
            context = {
                'course': course,
                'next_course': next_course,
                'previous_course': previous_course,
                'comments': comments,
                'reply' :reply,
            }
            return render(request,"courses/course-details.html",context=context)
        # except:
        #     return render(request,'courses/404.html')
    elif request.method == 'POST':
        form  = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited')
            return redirect(request.path_info)
    else:
        messages.add_message(request,messages.ERROR,'your comment is invalid')
        return redirect(request.path_info)
    
@login_required
def delete_comment(request,id):
    comment = Comment.objects.get(id=id)
    cid = comment.which_course.id
    comment.delete()
    return redirect(f'/course/course_detail/{cid}')

@login_required
def edit(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        context ={
            'comment': comment
        }
        return render(request, 'courses/edit.html',context)
    
    elif request.method == 'POST':
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
            cid = comment.which_course.id
            return redirect(f'/course/course_detail/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'invalid inputs')
            return redirect(request.path_info)
        

@login_required
def reply(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        form = ReplyForm()
        context ={
            'comment': comment,
            'form': form,
        }
        return render(request, 'courses/reply.html',context)
    
    elif request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            cid = comment.which_course.id
            return redirect(f'/course/course_detail/{cid}')
        else:
            messages.add_message(request,messages.ERROR,'your reply is invalid')
            return redirect(request.path_info)