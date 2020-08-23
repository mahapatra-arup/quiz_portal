from django import template
from quiz.models import ExamRequestStatus

#call register library
register = template.Library()

@register.filter
def exam_request_value(exam):
    """ This Filter Use for Set Request Value  """
    request_str="Request"
    data=ExamRequestStatus.objects.filter(exam=exam).first()

    if data:    
        if data.request and not data.approved :
            request_str="Cancel Request"
        elif data.approved:
            request_str="Approve"
        
    return request_str