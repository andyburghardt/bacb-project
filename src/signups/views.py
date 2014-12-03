from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
from .forms import SignUpForm
from .forms import StoryboardForm
from .forms import JobModelForm
from .forms import TaskAnalysisForm
from .forms import SkillsChecklistForm
from .forms import SelfAssessmentForm

def home(request):

	return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def thankyou(request):

	return render_to_response("thankyou.html", locals(), context_instance=RequestContext(request))

def aboutus(request):

	return render_to_response("aboutus.html", locals(), context_instance=RequestContext(request))

# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def supervisors(request):

	return render_to_response("supervisors.html", locals(), context_instance=RequestContext(request))

# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Supervisees').count() == 0, login_url='/login/')
def supervisees(request):

	return render_to_response("supervisees.html", locals(), context_instance=RequestContext(request))

# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def skills(request):

	form = SkillsChecklistForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'We will be in touch')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("skills.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def knowledgequiz(request):

	return render_to_response("knowledgequiz.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def samplecontracts(request):

	return render_to_response("samplecontracts.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def supervisionfeedback(request):

	return render_to_response("supervisionfeedback.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def storyboard(request):

	form = StoryboardForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'You have successfully submitted the storyboard')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("storyboard.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def jobmodel(request):

	form = JobModelForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'We will be in touch')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("jobmodel.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def taskanalysis(request):

	form = TaskAnalysisForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'You have successfully submitted a task analysis')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("taskanalysis.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def selfassessment(request):

	form = SelfAssessmentForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'We will be in touch')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("selfassessment.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def selfassessmentview(request):

	return render_to_response("selfassessmentview.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def superviseeassessmentresults(request):

	return render_to_response("superviseeassessmentresults.html", locals(), context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
def experiencesupervisionform(request):

	return render_to_response("experiencesupervisionform.html", locals(), context_instance=RequestContext(request))