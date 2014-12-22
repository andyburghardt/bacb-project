from django.shortcuts import redirect, render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView

# Create your views here.
from .forms import SignUpForm
from .forms import StoryboardForm
from .forms import JobModelForm
from .forms import TaskAnalysisForm
from .forms import SkillsChecklistForm
from .forms import SelfAssessmentForm
from .forms import UserForm
from .forms import UserProfileForm
from .forms import MyForm
from .forms import ExperienceSupervisionForm
from .forms import SupervisionFeedbackForm
from .forms import MyDataSheetsForm
from .forms import DevelopmentGoalsForm
from .forms import ValidationForm
from .forms import Validation2Form

from .models import SelfAssessment
from .models import MyDataSheets
from .models import SuperviseeValidation

def home(request):

	return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def resources(request):

	return render_to_response("supresources.html", locals(), context_instance=RequestContext(request))

def thankyou(request):

	return render_to_response("thankyou.html", locals(), context_instance=RequestContext(request))

def aboutus(request):

	return render_to_response("aboutus.html", locals(), context_instance=RequestContext(request))


# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def supervisors(request):

	form = MyForm()
	return render_to_response("supervisors.html", locals(), context_instance=RequestContext(request))


# @user_passes_test(lambda u: u.groups.filter(name='Supervisees').count() == 0, login_url='/login/')
@login_required
def supervisees(request):

	return render_to_response("supervisees.html", locals(), context_instance=RequestContext(request))


# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def skills(request):

	form = SkillsChecklistForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.user = request.user  # The logged-in user
		save_it.save()
		messages.success(request, 'You have successfully submitted a skills checklist')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("skills.html", locals(), context_instance=RequestContext(request))


# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def knowledgequiz(request):

	return render_to_response("knowledgequiz.html", locals(), context_instance=RequestContext(request))


# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def samplecontracts(request):

	return render_to_response("samplecontracts.html", locals(), context_instance=RequestContext(request))


# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def supervisionfeedback(request):

	form = SupervisionFeedbackForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.user = request.user  # The logged-in user
		save_it.save()
		messages.success(request, 'You have successfully submitted supervision feedback')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("supervisionfeedback.html", locals(), context_instance=RequestContext(request))

# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def storyboard(request):

	form = StoryboardForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.user = request.user  # The logged-in user
		save_it.save()
		messages.success(request, 'You have successfully submitted the storyboard')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("storyboard.html", locals(), context_instance=RequestContext(request))

# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def jobmodel(request):

	form = JobModelForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.user = request.user  # The logged-in user
		save_it.save()
		messages.success(request, 'You have successfully submitted a job model')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("jobmodel.html", locals(), context_instance=RequestContext(request))

# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def taskanalysis(request):

	form = TaskAnalysisForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.user = request.user  # The logged-in user
		save_it.save()
		messages.success(request, 'You have successfully submitted a task analysis')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("taskanalysis.html", locals(), context_instance=RequestContext(request))

# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def selfassessment(request):

	form = SelfAssessmentForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.user = request.user  # The logged-in user
		save_it.save()
		messages.success(request, 'You have successfully submitted a self assessment')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("selfassessment.html", locals(), context_instance=RequestContext(request))

# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def selfassessmentview(request):

	return render_to_response("selfassessmentview.html", locals(), context_instance=RequestContext(request))

# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def superviseeassessmentresults(request):

	return render_to_response("superviseeassessmentresults.html", locals(), context_instance=RequestContext(request))

# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def experiencesupervisionform(request):

	form = ExperienceSupervisionForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.user = request.user  # The logged-in user
		save_it.save()
		messages.success(request, 'You have successfully submitted an experience supervision form')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("experiencesupervisionform.html", locals(), context_instance=RequestContext(request))

@login_required
def register(request):
    # Like before, get the request's context.
    form = UserProfileForm(request.POST or None)
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.created_by = request.user # The logged-in user
            profile.current_supervisor = request.user # The logged-in user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

@login_required
def mydatasheets(request):
	query_results = MyDataSheets.objects.all()
	if request.POST:
		form = MyDataSheetsForm(request.POST, request.FILES)
		if form.is_valid():
			save_it = form.save(commit=False)
			save_it.user = request.user  # The logged-in user
			save_it.save()
			messages.success(request, 'You have successfully submitted a data sheet')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		form = MyDataSheetsForm()

	return render_to_response("mydatasheets.html", locals(), context_instance=RequestContext(request))

# @user_passes_test(lambda u: u.groups.filter(name='Supervisors').count() == 0, login_url='/login/')
@login_required
def developmentgoals(request):

	form = DevelopmentGoalsForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.user = request.user  # The logged-in user
		save_it.save()
		messages.success(request, 'You have successfully submitted performance development goals')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("goals.html", locals(), context_instance=RequestContext(request))

@login_required
def validation(request):
	query_results = SuperviseeValidation.objects.all()
	if request.POST:
		form = ValidationForm(request.POST, request.FILES)
		if form.is_valid():
			save_it = form.save(commit=False)
			save_it.user = request.user  # The logged-in user
			save_it.save()
			messages.success(request, 'You have successfully submitted a supervisee validation')
			return HttpResponseRedirect('/thank-you/')
	else:
		form = ValidationForm()

	return render_to_response("validation.html", locals(), context_instance=RequestContext(request))

@login_required
def validation(request):
	form = Validation2Form(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.user = request.user  # The logged-in user
		save_it.save()
		messages.success(request, 'You have successfully submitted a supervisee validation')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("validation.html", locals(), context_instance=RequestContext(request))