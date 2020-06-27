from django.shortcuts import render
from django.views.generic import FormView
#Messgee show
from django.contrib import messages

# from quiz.forms.student_forms import StdRegisterForm
from quizportal.send_emails import send_user_mail

# Create your views here.

# class StdRegisterCreateView(FormView):
#     template_name = "dashboard/student/register.html"
#     form_class = StdRegisterForm
    

#     def get(self, request, *args, **kwargs):
#         form  = self.form_class()
#         context = {'form': form,
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             #save
#             u_name, pwd, user_email, key=form.save()
#             new_user = authenticate(username=u_name, password=pwd)
#             login(request, new_user)

#             messages.add_message(request, messages.INFO ,'Message Send Successfull',extra_tags='Register', fail_silently=True)

#             if user_email and key:
#                 success, msg = send_user_mail(user_email, key)
#                 context = {'activation_msg': msg}
#                 render(request, self.template_name, {'form': form})
#             return index(request)
#         else:
#             return render(request, self.template_name, {'form': form})

            
#             #new instance
#             # form = StdRegisterForm()
#             # return render(request, self.template_name, {'form': form})

#         return render(request, self.template_name, {'form': form})

