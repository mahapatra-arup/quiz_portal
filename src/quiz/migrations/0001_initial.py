# Generated by Django 2.2.6 on 2020-05-10 08:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Class Name')),
                ('order_by', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=100, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Class',
                'db_table': 'clas',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('mcq', 'Single Correct Choice')], max_length=24)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('points', models.FloatField(default=1.0)),
                ('is_active', models.BooleanField(default=True)),
                ('question_img', models.FileField(blank=True, null=True, upload_to='question/images/%Y/%m/')),
                ('slug', models.SlugField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=100, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Question',
                'db_table': 'Question',
            },
        ),
        migrations.CreateModel(
            name='Question_Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Set Name like "2020-Set-I"', max_length=150)),
                ('order_by', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=100, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Question_Set_User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Question Set',
                'verbose_name_plural': 'Question Set',
                'db_table': 'Question_Set',
            },
        ),
        migrations.CreateModel(
            name='Student_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
                ('display_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], default='Male', max_length=50)),
                ('dob', models.DateTimeField()),
                ('institute', models.CharField(max_length=128)),
                ('slug', models.CharField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=50, unique=True)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the define format', regex='^\\+?1?\\d{9,12}$')])),
                ('student_img', models.ImageField(blank=True, help_text='Maximum file size allowed is 200kb', null=True, upload_to='student/images/%Y/%m/', verbose_name='Student Image')),
                ('department', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('address1', models.CharField(blank=True, max_length=200)),
                ('identity_doc_name', models.CharField(choices=[('Aadhaar Card', 'Aadhaar Card'), ('Voter Card', 'Voter Card'), ('Pan Card', 'Pan Card'), ('DOB Certificate', 'DOB Certificate'), ('Secondary Admite', 'Secondary Admite')], default='Aadhaar Card', max_length=100)),
                ('identity_doc_no', models.CharField(max_length=100)),
                ('identity_doc', models.FileField(blank=True, null=True, upload_to='student/documents/%Y/%m/')),
                ('about_your_self', models.TextField(blank=True, max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student Details',
                'verbose_name_plural': 'Student Details',
                'db_table': 'Student_Details',
                'ordering': ['display_name'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Subject Name')),
                ('code', models.CharField(max_length=100, verbose_name='Subject Code')),
                ('slug', models.SlugField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=100, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subject',
                'db_table': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='Subject_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Subject Name')),
                ('slug', models.SlugField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Subject')),
            ],
            options={
                'verbose_name': 'Subject Topic',
                'verbose_name_plural': 'Subject Topic',
                'db_table': 'Subject_Topic',
            },
        ),
        migrations.CreateModel(
            name='Student_Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clas', models.CharField(max_length=20, verbose_name='Class')),
                ('roll_no', models.CharField(blank=True, help_text='Roll No Like a Class No/Registration No/others', max_length=20, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Student_Details')),
            ],
            options={
                'verbose_name': 'Student Register',
                'verbose_name_plural': 'Student Register',
                'db_table': 'Student_Register',
            },
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_code', models.CharField(max_length=256, unique=True)),
                ('total_marks', models.FloatField(default=0.0)),
                ('time_duration', models.DurationField(default='00:00:00')),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=100, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Clas')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question_set', models.ManyToManyField(to='quiz.Question_Set')),
                ('subject_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Subject_Topic')),
            ],
            options={
                'verbose_name': 'QuestionPaper',
                'verbose_name_plural': 'QuestionPaper',
                'db_table': 'QuestionPaper',
            },
        ),
        migrations.CreateModel(
            name='Question_Set_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_by', models.PositiveIntegerField(default=0)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
                ('question_set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question_Set')),
            ],
            options={
                'verbose_name': 'Question_Set_Question',
                'verbose_name_plural': 'Question_Set_Question',
                'db_table': 'Question_Set_Question',
            },
        ),
        migrations.AddField(
            model_name='question_set',
            name='question',
            field=models.ManyToManyField(through='quiz.Question_Set_Question', to='quiz.Question'),
        ),
        migrations.CreateModel(
            name='Question_Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(blank=True, max_length=150, null=True)),
                ('img_option', models.FileField(blank=True, null=True, upload_to='option_img')),
                ('answer', models.BooleanField(default=True)),
                ('order_by', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=100, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
            options={
                'verbose_name': 'Question Option',
                'verbose_name_plural': 'Question Option',
                'db_table': 'Question_Option',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='subject_topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Subject_Topic'),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], default='Male', max_length=50)),
                ('dob', models.DateTimeField()),
                ('edu_qualification', models.CharField(max_length=50, verbose_name='Educational Qualification')),
                ('designation', models.CharField(blank=True, max_length=50, verbose_name='designation / Post')),
                ('institute', models.CharField(max_length=128)),
                ('contact_no', models.CharField(blank=True, max_length=13)),
                ('address', models.TextField(blank=True, max_length=500)),
                ('address1', models.TextField(blank=True, max_length=500)),
                ('instructor_img', models.ImageField(blank=True, help_text='Maximum file size allowed is 100kb', null=True, upload_to='instructor/images/%Y/%m/', verbose_name='Instructor Photo')),
                ('slug', models.SlugField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=100, unique=True)),
                ('identity_doc_name', models.CharField(choices=[('Aadhaar Card', 'Aadhaar Card'), ('Voter Card', 'Voter Card'), ('Pan Card', 'Pan Card'), ('DOB Certificate', 'DOB Certificate'), ('Secondary Admite', 'Secondary Admite')], default='Aadhaar Card', max_length=100)),
                ('identity_doc_no', models.CharField(max_length=100)),
                ('identity_doc', models.FileField(blank=True, null=True, upload_to='instructor/documents/%Y/%m/')),
                ('about_your_self', models.TextField(blank=True, max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('APPROAVE', 'APPROAVE'), ('REJECT', 'REJECT')], max_length=20, null=True)),
                ('user', models.OneToOneField(help_text='create user because one user is a one staff', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Instructors',
                'verbose_name_plural': 'Instructors',
                'db_table': 'Instructor',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('pass_per', models.FloatField(default=0.0, verbose_name='Percentage of Pass Marks')),
                ('is_active', models.BooleanField(default=True)),
                ('is_trial', models.BooleanField(default=False)),
                ('instructions', models.TextField(blank=True, default=None, null=True, verbose_name='Instructions for Students')),
                ('slug', models.SlugField(default=uuid.uuid4, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=100, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('questionpaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.QuestionPaper')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exam',
                'db_table': 'Exam',
            },
        ),
    ]
