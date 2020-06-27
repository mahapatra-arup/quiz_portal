from django.contrib import admin
from .models import  Student_Details,Student_Register,Instructor,Clas,Subject,Subject_Topic,Question,Question_Option,Question_Set,QuestionPaper,Exam,Question_Set_Question


@admin.register(Student_Details,Student_Register,Instructor,Clas,Subject,Subject_Topic,Question,Question_Option,Question_Set,Question_Set_Question,QuestionPaper,Exam,)
class DefaultAdmin(admin.ModelAdmin):
    pass
# Register your models here.
