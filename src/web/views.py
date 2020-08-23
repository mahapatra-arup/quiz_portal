from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
from quiz.models import Exam, Student_Details, ExamRequestStatus
from django.db.models import Q
from datetime import datetime


def exam_lists_data():
    exam_list = Exam.objects.filter(
        Q(start_date_time__gte=datetime.now()), is_active=True).distinct()
    return {'exam_list': exam_list}


class HomeView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "description": 'Home',
            "title": 'Home',
            "keywords": 'Home',
            "author": 'pytube , Arup Mahapatra',
            "page_title": 'Home',
            "breadcrumb": '<i class="fa fa-home"></i> ',
        })
        context.update(exam_lists_data())
        return context


class AboutUsView(TemplateView):
    template_name = "web/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "description": 'About Us',
            "title": 'About Us',
            "keywords": 'About Us',
            "author": '',
            "page_title": 'About Us',
            "breadcrumb": '<i class="fa fa-home"></i> / About Us',
        })
        return context


class ExamRequestUpdateView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "description": 'Student Exam Request',
            "title": 'Student Exam Request',
            "keywords": 'Student Exam Request',
            "author": '',
            "page_title": 'Student Exam Request',
            "breadcrumb": '<i class="fa fa-home"></i> /Student Exam Request',
        })
        return context

    def post(self, request, *args, **kwargs):
        exam = Exam.objects.filter(
            slug=self.request.POST.get("exam_slug")).first()
        examRequestStatus = ExamRequestStatus.objects.filter(
            exam=exam, user=self.request.user).first()

        btnSubmitValue = self.request.POST.get("btnSubmit")
        if btnSubmitValue.lower() == "request":
            if examRequestStatus:
                print("----------------Update processs-----------------")
                examRequestStatus.request = True
                examRequestStatus.approved = False
                examRequestStatus.cancelled = False
                examRequestStatus.save()
            else:
                print("-----------------Insert process-------------------")
                examRequestStatus = ExamRequestStatus()

                examRequestStatus.exam = exam
                examRequestStatus.user = self.request.user
                examRequestStatus.request = True
                examRequestStatus.approved = False
                examRequestStatus.cancelled = False
                examRequestStatus.save()
            messages.add_message(self.request, messages.INFO, 'Request Send Successfull',
                                 extra_tags='Exam Request', fail_silently=True)
        elif btnSubmitValue.lower() == "cancel request":
            examRequestStatus.request = False
            examRequestStatus.approved = False
            examRequestStatus.cancelled = True
            examRequestStatus.save()
            messages.add_message(self.request, messages.WARNING, 'Request Cancel Successfull',
                                 extra_tags='Exam Request', fail_silently=True)

        # go to previous page
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

# Exam Process=======================================>


class ExamQuizView(TemplateView):
    template_name = "web/exam_quiz_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "description": 'Home',
            "title": 'Home',
            "keywords": 'Home',
            "author": 'pytube , Arup Mahapatra',
            "page_title": 'Home',
            "breadcrumb": '<i class="fa fa-home"></i> ',
        })
        context.update(exam_lists_data())
        return context
