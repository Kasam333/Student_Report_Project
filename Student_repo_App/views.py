from django.shortcuts import render,HttpResponse
from Student_repo_App.models import *
from django.core.paginator import Paginator
from django.db.models import Q,Sum,Avg
from .seed import generate_report_card

# Create your views here.

def get_students(request):
    queryset = Student.objects.all()
    search = request.GET.get('search')
    if search:
        queryset = queryset.filter(
            Q(student_name__icontains = search) | 
            Q(department__department__icontains = search) | 
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search))

    paginator = Paginator(queryset, 25)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    
    print(page_obj)
    return render(request, "report/student.html", {'queryset': page_obj, 'search':search})

def see_marks(request, student_id):
    # generate_report_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    student = Student.objects.get(student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    total_avg = queryset.aggregate(total_avg = Avg('marks'))

    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i = 1
    for rank in ranks:
        if student_id == rank.student_id.student_id:
            current_rank = i
            break
        i += 1
    return render(request, 'report/see_marks.html', {'queryset': queryset, 'student': student, 'total_marks':total_marks, 'total_avg':total_avg, 'current_rank':current_rank})