from django.contrib.auth.models import User
from django import forms

from .models import SignUp
from .models import Storyboard
from .models import JobModel
from .models import TaskAnalysis
from .models import SkillsChecklist
from .models import Supervisee
from .models import SelfAssessment
from .models import MyModel
from .models import ExperienceSupervision
from .models import SupervisionFeedback
from .models import MyDataSheets
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['created_by', 'user', 'current_supervisor', 'can_view']   # Will be taken from the request

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        widgets = {
            'password': forms.PasswordInput(),
        }

class StoryboardForm(forms.ModelForm):
    class Meta:
        model = Storyboard
        exclude = ['user']   # Will be taken from the request

class JobModelForm(forms.ModelForm):
    class Meta:
        model = JobModel
        exclude = ['user']   # Will be taken from the request

class TaskAnalysisForm(forms.ModelForm):
    class Meta:
        model = TaskAnalysis
        exclude = ['user']   # Will be taken from the request

class SkillsChecklistForm(forms.ModelForm):
    class Meta:
        model = SkillsChecklist 
        exclude = ['user']   # Will be taken from the request

class SuperviseeForm(forms.ModelForm):
    class Meta:
        model = Supervisee

SELECT1A = (
(u'A', u'Does not meet the expectations1'),
(u'B', u'Does not meet the expectations2'),
(u'C', u'Meets the expectations1'),
(u'D', u'Meets the expectations2'),
(u'E', u'Exceeds the expectations1'),
(u'F', u'Exceeds the expectations2'),
(u'G', u'Exceeds the expectations3'),
)

SELECT1B = (
(u'A', u'Does not meet the expectations'),
(u'B', u'Meets the expectations'),
(u'C', u'Exceeds the expectations1'),
(u'D', u'Exceeds the expectations2'),
)

SELECT2 = (
(u'A', u'Does not meet the expectations'),
(u'B', u'Meets the expectations'),
(u'C', u'Exceeds the expectations'),
)

SELECT3A = (
(u'A', u'Does not meet the expectations'),
(u'B', u'Meets the expectations'),
(u'C', u'Exceeds the expectations'),
)

SELECT3B = (
(u'A', u'Does not meet the expectations'),
(u'B', u'Meets the expectations'),
(u'C', u'Exceeds the expectations'),
)

SELECT3C = (
(u'A', u'Does not meet the expectations'),
(u'B', u'Meets the expectations'),
(u'C', u'Exceeds the expectations'),
)

SELECT4A = (
(u'A', u'Does not meet the expectations'),
(u'B', u'Meets the expectations'),
(u'C', u'Exceeds the expectations'),
)

SELECT4B = (
(u'A', u'Does not meet the expectations'),
(u'B', u'Meets the expectations'),
(u'C', u'Exceeds the expectations'),
)

SELECT5 = (
(u'A', u'Does not meet the expectations1'),
(u'B', u'Does not meet the expectations2'),
(u'C', u'Meets the expectations1'),
(u'D', u'Meets the expectations2'),
(u'E', u'Exceeds the expectations'),
)

SELECT6A = (
(u'A', u'Does not meet the expectations'),
(u'B', u'Meets the expectations'),
(u'C', u'Exceeds the expectations1'),
(u'D', u'Exceeds the expectations2'),
)

SELECT6B = (
(u'A', u'Does not meet the expectations '),
(u'B', u'Meets the expectations'),
(u'C', u'Exceeds the expectations'),
)

class SelfAssessmentForm(forms.ModelForm):
    sa_1a = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT1A)
    sa_1b = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT1B)
    sa_2 = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT2)
    sa_3a = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT3A)
    sa_3b = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT3B)
    sa_3c = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT3C)
    sa_4a = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT4A)
    sa_4b = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT4B)
    sa_5 = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT5)
    sa_6a = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT6A)
    sa_6b = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT6B)
    class Meta:
        model = SelfAssessment
        exclude = ['user']   # Will be taken from the request

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        # form.fields['myuser'].queryset = User.objects.filter(groups__name='Supervisees')

class ExperienceSupervisionForm(forms.ModelForm):
    class Meta:
        model = ExperienceSupervision
        exclude = ['user']   # Will be taken from the request

class SupervisionFeedbackForm(forms.ModelForm):
    class Meta:
        model = SupervisionFeedback
        exclude = ['user']   # Will be taken from the request

class MyDataSheetsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyDataSheetsForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True
        self.fields['description'].error_messages = {'required': 'Please fill out a file title'}
    class Meta:
        model = MyDataSheets
        fields = ('files', 'description')
        exclude = ['user']   # Will be taken from the request


