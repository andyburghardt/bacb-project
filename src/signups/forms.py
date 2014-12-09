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


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		widgets = {
			'password': forms.PasswordInput(),
		}
		fields = "__all__" 

class StoryboardForm(forms.ModelForm):
	class Meta:
		model = Storyboard
		fields = "__all__" 

class JobModelForm(forms.ModelForm):
	class Meta:
		model = JobModel
		fields = "__all__" 

class TaskAnalysisForm(forms.ModelForm):
	class Meta:
		model = TaskAnalysis
		fields = "__all__" 

class SkillsChecklistForm(forms.ModelForm):
	class Meta:
		model = SkillsChecklist 
		fields = "__all__" 

class SuperviseeForm(forms.ModelForm):
	class Meta:
		model = Supervisee
		fields = "__all__" 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class SelfAssessmentForm(forms.ModelForm):
    class Meta:
        model = SelfAssessment

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        # form.fields['myuser'].queryset = User.objects.filter(groups__name='Supervisees')

class ExperienceSupervisionForm(forms.ModelForm):
    class Meta:
        model = ExperienceSupervision

class SupervisionFeedbackForm(forms.ModelForm):
    class Meta:
        model = SupervisionFeedback