from django.views.generic import TemplateView,CreateView,UpdateView,ListView,DeleteView

from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.contrib import messages

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_list_or_404 , get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
#project
from quiz.models import Question, QuestionPaper, Question_Set, Question_Set_Question, Subject_Topic,Exam
from quiz.forms.instructor_forms import QuestionForm, QuestionPaperForm, Question_SetForm, Subject_TopicForm,ExamForm
import json

#Subject Topic==================================
class Subject_TopicCreateView(CreateView):
    model = Subject_Topic
    template_name = 'dashboard\instructor\subject_topic\subject_topic_add.html'
    form_class = Subject_TopicForm
    success_url = "subject_topic_add"#

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "description": 'Create Subject Topic',
        "title": 'Create Subject Topic',
        "keywords": 'Create Subject Topic',
        "author": '',
        "page_title":'Subject Topic',
        "breadcrumb": '<i class="fa fa-home"></i> / Subject Topic',
        }) 
        return context

    def form_valid(self, form):
        sub_topic = form.save(self.request.user)
        messages.add_message(self.request, messages.INFO ,'Save Successfull',extra_tags='Subject Topic', fail_silently=True)
        return HttpResponseRedirect(reverse_lazy(self.success_url,args=[]))

    def form_invalid(self, form):
        return JsonResponse({"error": True, "response": form.errors})

class Subject_TopicListView(ListView):
    template_name = "dashboard/instructor/subject_topic/subject_topic_list.html"
    context_object_name = "obj_subject_topic"

    # All user data view
    def get_queryset(self):
        return Subject_Topic.objects.filter()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'Subject Topic View',
            "title": 'Subject Topic View',
            "keywords": 'Subject Topic View',
            "author": '',
            "page_title":'Subject Topic',
            "breadcrumb": '<i class="fa fa-home"></i> / Subject Topic',
            }) 
        return context

#Question ==================================
class QuestionCreateView(CreateView):
    model = Question
    template_name = 'dashboard\instructor\question\question_add.html'
    form_class = QuestionForm
    success_url = "question_add"#

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "description": 'Question',
        "title": 'Create Question',
        "keywords": 'Create Question',
        "author": '',
        "page_title":'Question',
        "breadcrumb": '<i class="fa fa-home"></i> / Question',
        }) 
        return context

    def form_valid(self, form):
        ques = form.save(self.request.user)
        messages.add_message(self.request, messages.INFO ,'Save Successfull',extra_tags='Question', fail_silently=True)
        return HttpResponseRedirect(reverse_lazy(self.success_url,args=[]))

    def form_invalid(self, form):
        return JsonResponse({"error": True, "response": form.errors})

class QuestionUpdateView(UpdateView):
    template_name = "dashboard\instructor\question\question_add.html"
    model = Question
    slug_url_kwarg = "question_slug"
    form_class = QuestionForm
    success_url = "question_list"#

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "description": 'Question',
        "title": 'Edit Question',
        "keywords": 'Edit Question',
        "author": '',
        "page_title":'Question',
        "breadcrumb": '<i class="fa fa-home"></i> / Question',
        }) 
        return context

    def form_valid(self, form):
        ques = form.save(self.request.user)
        messages.add_message(self.request, messages.INFO ,'Update Successfull',extra_tags='Question', fail_silently=True)
        return HttpResponseRedirect(reverse_lazy(self.success_url,args=[]))

    def form_invalid(self, form):
        return JsonResponse({'error': True, 'response': form.errors})

class QuestionDeleteView(DeleteView):
    
    model = Question
    slug_url_kwarg = "question_slug"
    success_url = reverse_lazy("question_list")
    success_message = "Deleted Successfully"
    template_name ="dashboard/confirm_delete_view.html"
    

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(self.success_url)
        else:
            return super().post(request, *args, **kwargs)

    # def get_object(self):
    #     return get_object_or_404(Question, slug=self.kwargs['question_slug'])

    # def post(self, request, *args, **kwargs):
    #     ques = self.get_object()
    #     ques.delete()
    #     messages.success(request, 'User successfully deleted!')
    #     return HttpResponseRedirect(reverse_lazy(success_url))

class QuestionListView(ListView):
    template_name = "dashboard/instructor/question/question_list.html"
    context_object_name = "obj_question"

    #only Login user data view
    def get_queryset(self):
        return Question.objects.filter(create_by=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'Question List View',
            "title": 'Question View',
            "keywords": 'Question View',
            "author": '',
            "page_title":'Question',
            "breadcrumb": '<i class="fa fa-home"></i> / Question',
            }) 
        return context


#Question Set===============================
class Question_SetCreateView(CreateView):
    model = Question_Set
    template_name = 'dashboard\instructor\question_set\question_set_add.html'
    form_class = Question_SetForm
    success_url = "question_set_add"#

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "description": 'Question Set',
        "title": 'Create Question Set',
        "keywords": 'Create Question Set',
        "author": '',
        "page_title":'Question Set',
        "breadcrumb": '<i class="fa fa-home"></i> / Question Set',
        }) 
        return context

    def form_valid(self, form):
        ques = form.save(self.request.user)
        messages.add_message(self.request, messages.INFO ,'Save Successfull',extra_tags='Question Set', fail_silently=True)
        return HttpResponseRedirect(reverse_lazy(self.success_url,args=[]))

    def form_invalid(self, form):
        return JsonResponse({"error": True, "response": form.errors})

class Question_SetUpdateView(UpdateView):
    template_name = "dashboard\instructor\question_set\question_set_add.html"
    model = Question_Set
    slug_url_kwarg = "question_set_slug"
    form_class = Question_SetForm
    success_url = "question_set_list"#

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "description": 'Question Set',
        "title": 'Edit Question Set',
        "keywords": 'Edit Question Set',
        "author": '',
        "page_title":'Question Set',
        "breadcrumb": '<i class="fa fa-home"></i> / Question Set',
        }) 
        return context

    def form_valid(self, form):
        ques = form.save(self.request.user)
        messages.add_message(self.request, messages.INFO ,'Update Successfull',extra_tags='Question Set', fail_silently=True)
        return HttpResponseRedirect(reverse_lazy(self.success_url,args=[]))

    def form_invalid(self, form):
        return JsonResponse({'error': True, 'response': form.errors})

class Question_SetDeleteView(DeleteView):
    
    model = Question
    slug_url_kwarg = "question_set_slug"
    success_url = reverse_lazy("question_set_list")
    success_message = "Deleted Successfully"
    template_name ="dashboard/confirm_delete_view.html"
    

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:# for cancel button
            return HttpResponseRedirect(self.success_url)
        else:
            return super().post(request, *args, **kwargs)

class Question_SetListView(ListView):
    template_name = "dashboard/instructor/question_set/question_set_list.html"
    context_object_name = "obj_question_set"

    # Only log in user
    def get_queryset(self):
        return Question_Set.objects.filter(create_by=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'Question Set List View',
            "title": 'Question Set View',
            "keywords": 'Question Set View',
            "author": '',
            "page_title":'Question Set',
            "breadcrumb": '<i class="fa fa-home"></i> / Question Set',
            }) 
        return context


#Question and Question Set=====================
class QuestionAndSetView(ListView):
    template_name = "dashboard/instructor/question_and_set/question_and_set.html"
    context_object_name = "obj_question_and_set"

    # Only log in user
    def get_queryset(self):
        self.query_ques_set_slug = self.request.GET.get('ques_set')#'ques_set' -- This Is the SELECT Id
        
        ques_set_ques=None
        if self.query_ques_set_slug:
            ques_set_ques= Question_Set_Question.objects.filter(create_by=self.request.user,question_set__slug=self.query_ques_set_slug).order_by('order_by')
        return ques_set_ques

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        question_sets=Question_Set.objects.filter(create_by=self.request.user, is_active=True)
       
       
        context.update({'question_sets':question_sets,'question_set_slug':self.query_ques_set_slug})

         #Default
        context.update({
            "description": 'Question and QuestionSet ',
            "title": 'Question and QuestionSet ',
            "keywords": 'Question and QuestionSet ',
            "author": '',
            "page_title":'Question and QuestionSet ',
            "breadcrumb": '<i class="fa fa-home"></i> / Question and QuestionSet',
            }) 
        return context

class QuestionAndSetDeleteView(DeleteView):
    
    model = Question_Set_Question
    success_url = reverse_lazy("question_and_set")
    success_message = "Deleted Successfully"
    template_name ="dashboard/confirm_delete_view.html"

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:# for cancel button
            return HttpResponseRedirect(self.success_url)
        else:
            return super().post(request, *args, **kwargs)

@csrf_exempt
def question_and_set_ordering(request):

    if (request.user.is_authenticated==True):
        if request.method == 'POST':    
            #Get Data 
            q_s_q_data=request.POST.get("question_data_ary")
            #load json
            json_quesandset=json.loads(q_s_q_data)
            
            try:
                i=1
                for ques in json_quesandset:
                    # print(ques['id'])
                    q_s_q=Question_Set_Question.objects.get(id=ques['id'])
                    q_s_q.order_by = i
                    q_s_q.save()
                    i+=1

                return HttpResponse("Save SuccessFull")
            except Exception as e:
                print(e)
                return HttpResponse(e)
        else:
            return HttpResponse("Invalid Data Input !! Please Select Valid Data")

    else:
        return HttpResponse("You are not logged in. Please log in and try again")

#Question and Question Set / Add===============
class QuestionAndSetAddView(ListView):
    template_name = "dashboard/instructor/question_and_set/question_and_set_add.html"
    context_object_name = "obj_question_and_set"

    # Only log in user
    def get_queryset(self):
        self.query_ques_set_slug = self.request.GET.get('ques_set')#'ques_set' -- This Is the SELECT Id
        return Question_Set_Question.objects.filter(create_by=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

         #another Context  Data
        questions=None
        if self.query_ques_set_slug :
            questions=Question.objects.filter(~Q(question_set__slug=self.query_ques_set_slug),create_by=self.request.user, is_active=True)#~Q : use for not in
            # print(questions.query)

        #All
        question_sets=Question_Set.objects.filter(create_by=self.request.user, is_active=True)
        context.update({'questions':questions,'question_sets':question_sets,'question_set_slug':self.query_ques_set_slug})
        
        #Default
        context.update({
            "description": 'Question and Set Manage',
            "title": 'Question and Set Manage',
            "keywords": 'Question and Set Manage',
            "author": '',
            "page_title":'Question and Set Manage',
            "breadcrumb": '<i class="fa fa-home"></i> / Question and Set Manage',
            }) 
        return context

@csrf_exempt
def question_and_set_create(request):
    # print(request.body)
    if (request.user.is_authenticated==True):
        if request.method == 'POST':    

            #Get Data 
            questions_data=request.POST.get("question_data_ary")
            ques_set_slug=request.POST.get("ques_set_slug")

            if questions_data and ques_set_slug:
                #load json
                json_questions=json.loads(questions_data)
                json_set_slug=json.loads(ques_set_slug)
                
                try:
                    # print(json_set_slug)
                    question_set=Question_Set.objects.get(slug=json_set_slug)

                    for ques in json_questions:
                        # print(ques['id'])
                        question=Question.objects.get(id=ques['id'])
                        
                        q_s_q = Question_Set_Question()
                        q_s_q.create_by = request.user
                        q_s_q.question = question
                        q_s_q.question_set =question_set
                        q_s_q.save()

                    return HttpResponse("Save SuccessFull")
                except Exception as e:
                    print(e)
                    return HttpResponse(e)
            else:
                return HttpResponse("Invalid Data Input !! Please Select Valid Data")

    else:
        return HttpResponse("You are not logged in. Please log in and try again")

#Question Paper=====================
class QuestionPaperCreateView(CreateView):
    model = QuestionPaper
    template_name = 'dashboard\instructor\question_paper\question_paper_add.html'
    form_class = QuestionPaperForm
    success_url = "question_paper_add"#

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "description": 'Question Paper',
        "title": 'Create Question Paper',
        "keywords": 'Create Question Paper',
        "author": '',
        "page_title":'Question Paper',
        "breadcrumb": '<i class="fa fa-home"></i> / Question Paper',
        }) 
        return context

    def form_valid(self, form):
        # Save the new instance.
        ques = form.save(self.request.user)
        # Now, save the many-to-many data for the form.
        form.save_m2m()
        messages.add_message(self.request, messages.INFO ,'Save Successfull',extra_tags='Question Paper', fail_silently=True)
        return HttpResponseRedirect(reverse_lazy(self.success_url,args=[]))

    def form_invalid(self, form):
        return JsonResponse({"error": True, "response": form.errors})

class QuestionPaperListView(ListView):
    template_name = "dashboard/instructor/question_paper/question_paper_list.html"
    context_object_name = "obj_question_paper"

    #only Login user data view
    def get_queryset(self):
        return QuestionPaper.objects.filter(create_by=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'Question Paper List View',
            "title": 'Question Paper View',
            "keywords": 'Question Paper View',
            "author": '',
            "page_title":'Question Paper',
            "breadcrumb": '<i class="fa fa-home"></i> / Question Paper',
            }) 
        return context

#Exam=====================
class ExamCreateView(CreateView):
    model = Exam
    template_name = 'dashboard\instructor\exam\exam_add.html'
    form_class = ExamForm
    success_url = "exam_add"#
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'request' : self.request
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "description": 'Exam',
        "title": 'Exam',
        "keywords": 'Exam',
        "author": '',
        "page_title":'Exam',
        "breadcrumb": '<i class="fa fa-home"></i> / Exam',
        }) 
        return context

    def form_valid(self, form):
        # Save the new instance.
        frm=  form
        ques = frm.save(self.request.user)
       
        messages.add_message(self.request, messages.INFO ,'Save Successfull ',extra_tags='Question Paper', fail_silently=True)
        return HttpResponseRedirect(reverse_lazy(self.success_url,args=[]))

    def form_invalid(self, form):
        return JsonResponse({"error": True, "response": form.errors})

class ExamListView(ListView):
    template_name = "dashboard/instructor/exam/exam_list.html"
    context_object_name = "obj_exam"

    #only Login user data view
    def get_queryset(self):
        return Exam.objects.filter(create_by=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'Exam List View',
            "title": 'Exam View',
            "keywords": 'Exam View',
            "author": '',
            "page_title":'Exam',
            "breadcrumb": '<i class="fa fa-home"></i> / Exam',
            }) 
        return context
