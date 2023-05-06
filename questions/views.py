from django.shortcuts import render,redirect


from .models import Question_Bank,Answer
from home.models import Course,Question




def student_details(request):
    if request.method=='POST':
        username = request.POST.get('student_username')
        student_answers = Answer.objects.filter(username=username)
        content = {
            'student_answers':student_answers,
            'student_username':username,
        }
    return render(request,'student_detail.html',content)


def feedback(request):
    if request.method=='POST':
        data = request.POST;
        username = request.POST.get('student_username')
        student_answers = Answer.objects.filter(username=username)
        for question in student_answers:
            question.remark = data[question.question_statement]
            question.save()
    return redirect('profile')