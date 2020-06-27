from django import forms
from datetime import datetime, timedelta 
from django.utils.safestring import mark_safe
from core.widgets import BootstrapDateTimePickerInput
#model
from quiz.models import Subject_Topic,Subject,Question,Question_Set,QuestionPaper,Exam
#var
from quiz.models import QUESTION_TYPE_CHOICE


class Subject_TopicForm(forms.ModelForm):
    subject=forms.ModelChoiceField(queryset=Subject.objects.filter(is_active=True),
                                      empty_label="--Select--",
                                      widget=forms.Select(attrs=
                                                          {
                                                            #   "class": "form-control selectpicker",
                                                            #   "type": "text",
                                                            #   "name": "article-category",
                                                            #   "id": "articleCategory",
                                                            #   "data-live-search": "true"
                                                          }
                                      )
                                    )
    class Meta:
        model=Subject_Topic
        fields=('subject','name')
   
    def save(self,user=None):
      commit=True
      sub_topic = super().save(commit=False)
      sub_topic.create_by=user
      if commit:
          sub_topic.save()
      return sub_topic


class QuestionForm(forms.ModelForm):

  subject_topic=forms.ModelChoiceField(queryset=Subject_Topic.objects.filter(is_active=True),
                                    empty_label="--Select--",
                                    widget=forms.Select(attrs={}
                                    )
                                  )

  type=forms.ChoiceField(choices=QUESTION_TYPE_CHOICE,
      widget=forms.Select(attrs={}
       ))
     
  
  summary=forms.CharField(label="Summary/Question Title", help_text=mark_safe('Enter Summary/Question Title <i class="w3-text-red">EX: Python is a __ ?</i>'))
  points = forms.FloatField(widget=forms.NumberInput(attrs={ "type": "number",}))
                                                           
                                                           
  class Meta:
      model=Question
      fields=('summary','type','description','points','subject_topic','question_img','is_active')
  
  def save(self,user=None):
    commit=True
    ques = super().save(commit=False)
    ques.create_by=user
    if commit:
        ques.save()
    return ques


class Question_SetForm(forms.ModelForm):

    class Meta:
        model=Question_Set
        fields=('name','order_by','is_active')
   
    def save(self,user=None):
      commit=True
      qset = super().save(commit=False)
      qset.create_by=user
      if commit:
          qset.save()
      return qset


class QuestionPaperForm(forms.ModelForm):
  # time_duration = forms.DurationField(
  #       widget=forms.with))                                      
  
  class Meta:
      model=QuestionPaper
      fields=('paper_code','question_set','total_marks','time_duration','subject_topic','clas','is_active')
  
  def save(self,user=None):
    commit=True
    ques = super().save(commit=False)
    ques.create_by=user
    if commit:
        ques.save()
    return ques


class ExamForm(forms.ModelForm):
  start_date_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )   
          
  end_date_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'], 
        widget=BootstrapDateTimePickerInput()
    )
                                                                
  class Meta:
      model=Exam
      fields=('name','questionpaper','start_date_time','end_date_time','pass_per','is_active','is_trial','instructions')
  
  def __init__(self, *args, **kwargs):
    user_request = kwargs.pop('request')#must be put before __init__()
    super().__init__(*args, **kwargs)
    self.fields['questionpaper'].queryset = QuestionPaper.objects.filter(is_active=True,create_by=user_request.user)
    
  def save(self,user=None):
    commit=True
    exm = super().save(commit=False)
    exm.create_by=user
    if commit:
        exm.save()
    return exm
