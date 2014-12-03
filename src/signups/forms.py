from django import forms

from .models import SignUp
from .models import Storyboard
from .models import JobModel
from .models import TaskAnalysis
from .models import SkillsChecklist
from .models import Supervisee
from .models import SelfAssessment


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

class SelfAssessmentForm(forms.ModelForm):
	class Meta:
		model = SelfAssessment
		YESNO_CHOICES = ((0, 'No'), (1, 'Yes'))
		Allergies = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect, coerce=int
                )

#	class Meta:
#		model = SelfAssessment
#		fields = "__all__"

