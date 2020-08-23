from django.shortcuts import render
from django.views.generic import TemplateView,CreateView

from quiz.forms.forms import UserRegisterForm
from django.http import JsonResponse
from django.contrib import messages
from quizportal.send_emails import send_user_mail

from datetime import datetime
from  quiz.forms import forms
from django.contrib.auth.views import LoginView,LogoutView

#//Settings
from quizportal.settings.development import LOGIN_URL,LOGIN_REDIRECT_URL,LOGOUT_REDIRECT_URL


class StudentIndexView(TemplateView):
    template_name = "dashboard/student/index.html"

class UserCreateView(CreateView):
    template_name ="dashboard/account/user_create.html"
    form_class = UserRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "description": 'Create User',
        "title": 'Create User',
        "keywords": 'Create User, Registration',
        "author": '',
        "page_title":'Create User',
        "breadcrumb": '<i class="fa fa-home"></i> / Registration',
        }) 
        return context

    def form_valid(self, form):
        usr = form.save()

        #email
        success, msg = send_user_mail(usr.email, usr.activation_key)
        messages.success(self.request, 'Successfully added your User')
        return JsonResponse({"error": False, "response": "Successfully added your User"})

    def form_invalid(self, form):
        return JsonResponse({"error": True, "response": form.errors})
    
class UserLoginView(LoginView):
    template_name=LOGIN_URL
    authentication_form= forms.UserAuthenticationForm
    extra_context={
            'title': 'Log in',
            'year': datetime.now().year,
        }  

class UserLogoutView(LogoutView):
    next_page=LOGOUT_REDIRECT_URL


