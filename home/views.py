from django.shortcuts import render,redirect
from .models import Topic,Question
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Course, Topic, Question
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


def index(request):
    return render(request, "index.html")

def courses(request):
    if request.method == "POST":
        course_id = request.POST.get("course_id")
        return redirect(reverse("course_detail"), kwargs={"course_id": course_id})
    else:
        courses = Course.objects.all()
        content = {
            'courses':courses,
        }
        return render(request,"courses.html",content)

@login_required
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    questions = Question.objects.filter(course_id=course_id)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        new_course = Course.objects.create(name=name, description=description)
        return redirect(reverse("course_detail", kwargs={"course_id": new_course.id}))

    content = {
        'course': course,
        'questions': questions,
        'new_course_form': True,
    }
    return render(request, "course_detail.html", content)

def learning(request):
    topics = Topic.objects.all()
    content = {
        'topics': topics,
    }
    return render(request, "learning.html", content)

def learning_detail(request):
    topic_id = request.POST.get("topic_id")
    topic = Topic.objects.filter(id=topic_id)[0]
    content = {
        'name': topic.name,
        'description':topic.description,
    }
    return render(request, "learning_detail.html", content)

def news(request):
    return render(request,"news.html")

def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        # do something with the uploaded file (e.g. save it to the database)
        return render(request, "file_upload_success.html")
    return render(request, "file_upload.html")