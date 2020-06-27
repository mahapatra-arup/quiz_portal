from quiz.models import Subject_Topic 


class F(FilterSet):
    class Meta:
        model = Subject_Topic
        fields = '__all__'