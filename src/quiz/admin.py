from django.contrib import admin
from .models import  *


@admin.register(Student_Details,Student_Register,Instructor,Clas,Subject,Subject_Topic,Question,Question_Option,Question_Set,Question_Set_Question,QuestionPaper,Exam,ExamRequestStatus)
class DefaultAdmin(admin.ModelAdmin):
    pass
# Register your models here.
