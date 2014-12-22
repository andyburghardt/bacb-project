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
from .models import DevelopmentGoals
from .models import SuperviseeValidation
from .models import SuperviseeValidation2

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

class DevelopmentGoalsForm(forms.ModelForm):
    class Meta:
        model = DevelopmentGoals
        exclude = ['user']   # Will be taken from the request

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

PERFORMANCE0 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)

PERFORMANCE1 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE2 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE3 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE4 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE5 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE6 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE7 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE8 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE9 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE10 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)

PERFORMANCE11 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE12 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE13 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE14 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE15 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)
PERFORMANCE16 = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
(u'NA', u'NA'),
)


EVAL = (
(u'S', u'S'),
(u'NI', u'NI'),
(u'U', u'U'),
)

class ExperienceSupervisionForm(forms.ModelForm):
    arrives_on_time = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE0)
    maintains_professional = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE1)
    clients_consumers = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE2)
    other_service_providers = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE3)
    coworkers = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE4)
    maintains_appropriate_attire = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE5)
    initiates_professional_improvement = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE6)
    accepts_supervisory_feedback = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE7)
    seeks_supervision = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE8)
    timely_submission_reports = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE9)
    communicates_effectively = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE10)
    written = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE11)
    oral = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE12)
    demonstrates_sensitivity = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE13)
    personal_limitations = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE14)
    professional_limitations = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE15)
    behavior_analytic_skills = forms.ChoiceField(widget=forms.RadioSelect, choices=PERFORMANCE16)
    overall_evaluation = forms.ChoiceField(widget=forms.RadioSelect, choices=EVAL)
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

class ValidationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ValidationForm, self).__init__(*args, **kwargs)
    class Meta:
        model = SuperviseeValidation
        fields = ('Supervisees', 'files1', 'files2', 'files3', 'files4')
        exclude = ['user']   # Will be taken from the request

VALIDATED = (
(u'YES', u'YES'),
(u'NO', u'NO'),
)

class Validation2Form(forms.ModelForm):
    validated1 = forms.ChoiceField(widget=forms.RadioSelect, choices=VALIDATED)
    validated2 = forms.ChoiceField(widget=forms.RadioSelect, choices=VALIDATED)
    validated3 = forms.ChoiceField(widget=forms.RadioSelect, choices=VALIDATED)
    validated4 = forms.ChoiceField(widget=forms.RadioSelect, choices=VALIDATED)
    class Meta:
        model = SuperviseeValidation2
        fields = ('Supervisees', 'actions1', 'deadline1', 'validated1', 'actions2', 'deadline2', 'validated2', 'actions3', 'deadline3', 'validated3', 'actions4', 'deadline4', 'validated4')
        exclude = ['user']   # Will be taken from the request
