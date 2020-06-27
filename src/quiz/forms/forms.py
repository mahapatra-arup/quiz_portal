from django import forms
from datetime import datetime, timedelta 


try:
    from string import letters
except ImportError:
    from string import ascii_letters as letters
from string import punctuation, digits

#user
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

#project
from quizportal.send_emails import generate_activation_key

USER_TYPE_CHOICE=(
    ('STUDENT','STUDENT'),
    ('INSTRUCTOR','INSTRUCTOR'),
)
UNAME_CHARS = letters + "._" + digits
PWD_CHARS = letters + punctuation + digits

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50,help_text='Letters, digits,\period and underscores only.', 
    widget=forms.TextInput(attrs={'class':'','placeholder': "Username",}))

    email = forms.EmailField(
    widget=forms.EmailInput(attrs={'class':'','placeholder': "Email"}))

    password = forms.CharField( max_length=30,
    widget=forms.PasswordInput(attrs={'placeholder': "Password"}))

    confirm_password = forms.CharField(max_length=30, 
            widget=forms.PasswordInput(attrs={'placeholder': "Confirm Password"}))

    user_type=forms.ChoiceField(label='I Am a',choices=USER_TYPE_CHOICE,
    widget=forms.RadioSelect(attrs={'class':''}))

    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'password')

        

    def clean_username(self):
        u_name = self.cleaned_data["username"]
        if u_name.strip(UNAME_CHARS):
            msg = "Only letters, digits, period and underscore characters are"\
                  " allowed in username"
            raise forms.ValidationError(msg)
        try:
            User.objects.get(username__exact=u_name)
            raise forms.ValidationError("Username already exists.")
        except User.DoesNotExist:
            return u_name

    def clean_password(self):
        pwd = self.cleaned_data['password']
        if pwd.strip(PWD_CHARS):
            raise forms.ValidationError("Only letters, digits and punctuation\
                                        are allowed in password")
        return pwd

    def clean_confirm_password(self):
        c_pwd = self.cleaned_data['confirm_password']
        pwd = self.data['password']
        if c_pwd != pwd:
            raise forms.ValidationError("Passwords do not match")

        return c_pwd

    def clean_email(self):
        user_email = self.cleaned_data['email']
        if User.objects.filter(email=user_email).exists():
            raise forms.ValidationError("This email already taken")
        return user_email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required = True

        # for field in iter(self.fields):
        #     if max(enumerate(iter(self.fields)))[0] != field:
        #         self.fields[field].widget.attrs.update({
        #             'class': '',
        #             "placeholder": "Please enter your " + field.capitalize()
        #         })

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]

        #
        user_type=self.cleaned_data["user_type"]
        if user_type=='INSTRUCTOR':
            user.is_student=False
            user.is_instructor=True
        else:
            user.is_student=True
            user.is_instructor=False

         # Activations
        user.activation_key = generate_activation_key(user.username)
        user.key_expiry_time = datetime.now() + timedelta(minutes=20)

        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
