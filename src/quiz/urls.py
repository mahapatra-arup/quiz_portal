"""pytube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#proj
from quiz.views.views import *
from quiz.views.student_views import *
from quiz.views.instructor_views import *
from quiz.views.views import *


urlpatterns = [
    # //Student====================>
    path('',StudentIndexView.as_view(),name='admin_view'),
    path('registration',UserCreateView.as_view(),name='user_create_view'),

    # //Instructor====================>
    path('instructor/subject_topic_list',Subject_TopicListView.as_view(),name='subject_topic_list'),
    path('instructor/add_subject_topic',Subject_TopicCreateView.as_view(),name='subject_topic_add'),
   
    #Question
    path('instructor/add_question',QuestionCreateView.as_view(),name='question_add'),
    path('instructor/update_question/<question_slug>',QuestionUpdateView.as_view(),name='question_edit'),
    path('instructor/delete_question/<question_slug>',QuestionDeleteView.as_view(),name='question_delete'),
    path('instructor/question_list',QuestionListView.as_view(),name='question_list'),

    #Question Set
    path('instructor/add_question_set',Question_SetCreateView.as_view(),name='question_set_add'),
    path('instructor/update_question_set/<question_set_slug>',Question_SetUpdateView.as_view(),name='question_set_edit'),
    path('instructor/delete_question_set/<question_set_slug>',Question_SetDeleteView.as_view(),name='question_set_delete'),
    path('instructor/question_set_list',Question_SetListView.as_view(),name='question_set_list'),


    # Question and Queston Set Manage
    path('instructor/question_and_set',QuestionAndSetView.as_view(),name='question_and_set'),
    path('instructor/question_and_set_delete/<slug:pk>',QuestionAndSetDeleteView.as_view(),name='question_and_set_delete'),

    path('instructor/question_and_set_addview',QuestionAndSetAddView.as_view(),name='question_and_set_addview'),
    #AJAX Request
    path('instructor/question_and_set_create',question_and_set_create,name='question_and_set_create'),
    path('instructor/question_and_set_ordering',question_and_set_ordering,name='question_and_set_ordering'),

    # Question Paper
    path('instructor/question_paper/add',QuestionPaperCreateView.as_view(),name='question_paper_add'),
    path('instructor/question_paper',QuestionPaperListView.as_view(),name='question_paper_list'),

    # Exam
    path('instructor/exam/add',ExamCreateView.as_view(),name='exam_add'),
    path('instructor/exam',ExamListView.as_view(),name='exam_list'),
    
]
