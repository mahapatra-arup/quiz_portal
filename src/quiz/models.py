from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils.text import slugify
from quizportal.tools.utils import generate_unique_slug
import uuid
from users.models import User


IDENTITY_CHOICE=(('Aadhaar Card','Aadhaar Card'),
('Voter Card','Voter Card'),
('Pan Card','Pan Card'),
('DOB Certificate','DOB Certificate'),
('Secondary Admite','Secondary Admite')
)
INSTRUCTOR_REQUEST_CHOICE = (
    ('APPROAVE', 'APPROAVE'),
    ('REJECT', 'REJECT'),
) 
GENDER_CHOICE=(
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHERS','OTHERS')
)
QUESTION_TYPE_CHOICE = (
        ("mcq", "Single Correct Choice"),
        # ("mcc", "Multiple Correct Choices"),
        # ("code", "Code"),
        # ("upload", "Assignment Upload"),
        # ("integer", "Answer in Integer"),
        # ("string", "Answer in String"),
        # ("float", "Answer in Float"),
        # ("arrange", "Arrange in Correct Order"),

    )


#===================================================================================
class Student_Details(models.Model):
    """ Store Student details"""
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$',
                                 message="Phone number must be entered in the define format")

    # Model 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_code=models.CharField(unique=True,max_length=50,default=uuid.uuid4)
    display_name = models.CharField(max_length=50)
    father_name=models.CharField(max_length=100)
    gender= models.CharField(choices=GENDER_CHOICE,max_length=50, default='Male')
    dob= models.DateTimeField()

    institute = models.CharField(max_length=128)
    slug = models.CharField(max_length=50, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
    
    phone = models.CharField(validators=[phone_regex], max_length=12)
    student_img= models.ImageField('Student Image',upload_to='student/images/%Y/%m/', blank=True, null=True,help_text='Maximum file size allowed is 200kb')
    
    department = models.CharField(max_length=50)
    address = models.CharField(max_length=200,)
    address1 = models.CharField(max_length=200, blank=True)
    
    identity_doc_name = models.CharField(max_length=100, choices=IDENTITY_CHOICE, default='Aadhaar Card')
    identity_doc_no = models.CharField(max_length=100)
    identity_doc = models.FileField(upload_to='student/documents/%Y/%m/', blank=True, null=True)
    
    about_your_self= models.TextField(max_length=500,blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['display_name']
        verbose_name = 'Student Details'
        verbose_name_plural = 'Student Details'

        db_table = "Student_Details"

    def get_student_img_url(self):
         if self.student_img and hasattr(self.student_img, 'url'):
          return self.student_img.url

    def get_identity_doc_url(self):
         if self.identity_doc and hasattr(self.identity_doc, 'url'):
          return self.identity_doc.url

    def __str__(self):
        return self.dispay_name

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.display_name) != self.slug:
                self.slug = generate_unique_slug(Student_Details, self.display_name)
        else:  # create
            self.slug = generate_unique_slug(Student_Details, self.display_name)
        super().save(*args, **kwargs)

class Student_Register(models.Model):
    """ store Student Register details"""
    student=models.ForeignKey(Student_Details, on_delete=models.CASCADE)
    clas=models.CharField("Class", max_length=20)
    roll_no=models.CharField(max_length=20, blank=True, null=True,help_text='Roll No Like a Class No/Registration No/others')
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table = "Student_Register"
        verbose_name = "Student Register"
        verbose_name_plural = "Student Register"

    def __str__(self):
        return self.name

#===================================================================================
class Instructor(models.Model):
    """ Instructor/Teachers details"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,help_text='create user because one user is a one staff')
    display_name= models.CharField(max_length=50)
    gender= models.CharField(choices=GENDER_CHOICE,max_length=50, default='Male')
    dob= models.DateTimeField()
    edu_qualification= models.CharField("Educational Qualification",max_length=50)
    designation= models.CharField("designation / Post",blank=True,max_length=50)
    institute = models.CharField(max_length=128)
    
    contact_no= models.CharField(max_length=13,blank=True)
    address=models.TextField(max_length=500,blank=True)
    address1=models.TextField(max_length=500,blank=True)

    instructor_img = models.ImageField('Instructor Photo',upload_to='instructor/images/%Y/%m/', blank=True, null=True,help_text='Maximum file size allowed is 100kb')

    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')

    identity_doc_name = models.CharField(max_length=100, choices=IDENTITY_CHOICE, default='Aadhaar Card')
    identity_doc_no = models.CharField(max_length=100)
    identity_doc = models.FileField(upload_to='instructor/documents/%Y/%m/', blank=True, null=True)
    
    about_your_self= models.TextField(max_length=500,blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    status=models.CharField(max_length=20,choices=INSTRUCTOR_REQUEST_CHOICE, blank=True, null=True)



    @property         
    def get_image_url(self):
         if self.instructor_img and hasattr(self.instructor_img, 'url'):
          return self.instructor_img.url

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.display_name) != self.slug:
                self.slug = generate_unique_slug(Instructor, self.display_name)
        else:  # create
            self.slug = generate_unique_slug(Instructor, self.display_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.display_name

    def get_instructor_img_url(self):
         if self.instructor_img and hasattr(self.instructor_img, 'url'):
          return self.instructor_img.url

    def get_identity_doc_url(self):
         if self.identity_doc and hasattr(self.identity_doc, 'url'):
          return self.identity_doc.url

    class Meta:
        db_table = "Instructor"
        # unique_together = ('name', 'code')

        verbose_name = 'Instructors'
        verbose_name_plural = 'Instructors'

#===================================================================================
class Clas(models.Model):
    """ Store Student Class  """
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField("Class Name", max_length=100)
    order_by = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "clas"
        
        verbose_name = 'Class'
        verbose_name_plural = 'Class'

class Subject(models.Model):
    """ Store Subject """
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField("Subject Name",unique=True, max_length=100)
    code=models.CharField("Subject Code", max_length=100)
    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Subject"
        # unique_together = ('name', 'code')
        verbose_name = 'Subject'
        verbose_name_plural = 'Subject'

class Subject_Topic(models.Model):
    """ Store Subject Topic Like Subject Chapter """

    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name=models.CharField("Subject Name",unique=True, max_length=100)
    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
    is_active=models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
            return self.name

    class Meta:
        db_table = "Subject_Topic"
        
        verbose_name = 'Subject Topic'
        verbose_name_plural = 'Subject Topic'

#===================================================================================
class Question(models.Model):
    """Store Questions for a quiz."""

    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # A one-line summary of the question. like What is Python ? 
    summary = models.CharField(max_length=256)

    # The type of question.
    type = models.CharField(max_length=24, choices=QUESTION_TYPE_CHOICE)

    # The question text, should be valid HTML.
    description = models.CharField(max_length=256,null=True,blank=True)

    # Number of points for the question.
    points = models.FloatField(default=1.0)

    # The language for question.
    subject_topic = models.ForeignKey(Subject_Topic,  on_delete=models.CASCADE)
    

    # Is this question active or not. If it is inactive it will not be used
    # when creating a QuestionPaper.
    is_active = models.BooleanField(default=True)

    question_img = models.FileField(upload_to='question/images/%Y/%m/', blank=True, null=True)
    
    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
   
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    # # Tags for the Question.
    # tags = TaggableManager(blank=True)
    def __str__(self):
        return str(self.summary )

    def get_questionimg_url(self):
         if self.question_img and hasattr(self.question_img, 'url'):
          return self.question_img.url

    class Meta:
        db_table = "Question"
        verbose_name = 'Question'
        verbose_name_plural = 'Question'

#===================================================================================
class Question_Option(models.Model):
    """ Store Option for Question for a quiz. """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=150, blank=True, null=True)
    img_option = models.FileField(upload_to='question/option_img/%Y/%m/', blank=True, null=True)
    answer = models.BooleanField(default=True)
    order_by=models.PositiveIntegerField(default=0)

    is_active=models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
   
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.question.summary+': ('+self.option_name+')'

    def get_img_option_url(self):
         if self.img_option and hasattr(self.img_option, 'url'):
          return self.img_option.url

    class Meta:
        db_table = "Question_Option"
        verbose_name = 'Question Option'
        verbose_name_plural = 'Question Option'

#===================================================================================
class Question_Set(models.Model):
    """ Store Question Set """
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="Question_Set_User")
    name = models.CharField(max_length=150,help_text='Enter meaningfull Question-Set Name like "2020-Bengali-Set-I"')
    
    #Question Add
    question = models.ManyToManyField(Question,through='Question_Set_Question')

    order_by = models.PositiveIntegerField(default=0)
    is_active=models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
   
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "Question_Set"
        verbose_name = 'Question Set'
        verbose_name_plural = 'Question Set'

class Question_Set_Question(models.Model):
    """ Add Questions on Question set """
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    question_set=models.ForeignKey(Question_Set,on_delete=models.CASCADE)
    order_by=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question.summary+': ('+self.question_set.name+')'

    class Meta:
        db_table = "Question_Set_Question"
        verbose_name = 'Question & Question-Set Manage'
        verbose_name_plural = 'Question & Question-Set Manage'

#===================================================================================
class QuestionPaper(models.Model):
    """Store multiple   Question Set   """
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paper_code=models.CharField(max_length=256,unique=True)
    
    question_set = models.ManyToManyField(Question_Set)

    # Total marks for the question paper.
    total_marks = models.FloatField(default=0.0)
    time_duration = models.DurationField(default='00:00:00')

    # The language for question.
    subject_topic = models.ForeignKey(Subject_Topic,  on_delete=models.CASCADE)
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
   
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    def __str__(self):
        return self.paper_code+'). '+ self.subject_topic.name

    class Meta:
        db_table = "QuestionPaper"
        verbose_name = 'QuestionPaper'
        verbose_name_plural = 'QuestionPaper'

#===================================================================================
class Exam(models.Model):
    """ Ready to ExamPaper For quiz """
    name=models.CharField(max_length=256)

    questionpaper=models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)

    start_date_time=models.DateTimeField()
    end_date_time=models.DateTimeField()

    #Percentage of passmarks
    pass_per=models.FloatField("Percentage of Pass Marks",default=0.0)

    is_active = models.BooleanField(default=True)
    is_trial = models.BooleanField(default=False)
    instructions = models.TextField('Instructions for Students',
                                    default=None, blank=True, null=True)

    featured_image=models.ImageField(upload_to='exam/images/%Y/%m/', blank=True, null=True)                                
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    # view_answerpaper = models.BooleanField('Allow student to view their answer\
    #                                         paper', default=False)

    # allow_skip = models.BooleanField("Allow students to skip questions",default=True)

    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
   
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(self.name)

    def get_featured_image_url(self):
         if self.featured_image and hasattr(self.featured_image, 'url'):
          return self.featured_image.url

    class Meta:
        db_table = "Exam"
        verbose_name = 'Exam'
        verbose_name_plural = 'Exam'           

    
    def get_featured_image_url(self):
         if self.featured_image and hasattr(self.featured_image, 'url'):
          return self.featured_image.url
          
#===================================================================================
class ExamRequestStatus(models.Model):
    """Student Send The Request For Exam"""
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    
    #After Approve Student For exam , Then Admin Set The Question-Set
    question_set = models.ForeignKey(Question_Set,on_delete=models.CASCADE,null=True,blank=True)

    request=models.BooleanField(default=False)
    approved=models.BooleanField(default=False)

    # Only Rejected track
    cancelled=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = "ExamRequestStatus"
        verbose_name = 'Student Exam Request'
        verbose_name_plural = 'Student Exam Request'

#===================================================================================


    

