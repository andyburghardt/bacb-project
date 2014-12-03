from django.contrib import admin

# Register your models here.
from .models import SignUp
from .models import Storyboard
from .models import TaskAnalysis
from .models import JobModel
from .models import SkillsChecklist

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp
        
admin.site.register(SignUp, SignUpAdmin)


class StoryboardAdmin(admin.ModelAdmin):
    class Meta:
        model = Storyboard

admin.site.register(Storyboard, StoryboardAdmin)

class TaskAnalysisAdmin(admin.ModelAdmin):
    class Meta:
        model = TaskAnalysis

admin.site.register(TaskAnalysis, TaskAnalysisAdmin)

class JobModelAdmin(admin.ModelAdmin):
    class Meta:
        model = JobModel

admin.site.register(JobModel, JobModelAdmin)

class SkillsChecklistAdmin(admin.ModelAdmin):
    class Meta:
        model = SkillsChecklist

admin.site.register(SkillsChecklist, SkillsChecklistAdmin)

