from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^logout/$', 'signups.views.logout', name='logout'),
    # url(r'^$', 'bacb_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    url(r'^supervisors/$', 'signups.views.supervisors', name='supervisors'),
    url(r'^supervisees/$', 'signups.views.supervisees', name='supervisees'),
    url(r'^skills/$', 'signups.views.skills', name='skills'),
    url(r'^knowledgequiz/$', 'signups.views.knowledgequiz', name='knowledgequiz'),
    url(r'^samplecontracts/$', 'signups.views.samplecontracts', name='samplecontracts'),
    url(r'^supervisionfeedback/$', 'signups.views.supervisionfeedback', name='supervisionfeedback'),
    url(r'^experiencesupervisionform/$', 'signups.views.experiencesupervisionform', name='experiencesupervisionform'),
    url(r'^storyboard/$', 'signups.views.storyboard', name='storyboard'),
    url(r'^taskanalysis/$', 'signups.views.taskanalysis', name='taskanalysis'),
    url(r'^selfassessment/$', 'signups.views.selfassessment', name='selfassessment'),
    url(r'^selfassessmentview/$', 'signups.views.selfassessmentview', name='selfassessmentview'),
    url(r'^superviseeassessmentresults/$', 'signups.views.superviseeassessmentresults', name='superviseeassessmentresults'),
    url(r'^jobmodel/$', 'signups.views.jobmodel', name='jobmodel'),
    url(r'^register/$', 'signups.views.register', name='register'),
    url(r'^resources/$', 'signups.views.resources', name='resources'),
    url(r'^mydatasheets/$', 'signups.views.mydatasheets', name='mydatasheets'),
    url(r'^developmentgoals/$', 'signups.views.developmentgoals', name='developmentgoals'),
    url(r'^validation/$', 'signups.views.validation', name='validation'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='logout'),
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)