from django.db import models
from django.forms import ModelForm
from datetime import date
import datetime
from django import forms
from django.forms import Textarea
from django.utils.encoding import smart_unicode

# Create your models here.

def home(request):

    return render_to_response("index.html", locals(), context_instance=RequestContext(request))

class SignUp(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    # password = models.CharField(max_length=50)
    # active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.email)

class Supervisee(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    supervisor_id = models.ForeignKey(SignUp)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.email)

class Storyboard(models.Model):
    performance = models.CharField(max_length=480, null=True, blank=True)
    rational = models.TextField()
    modeling_say = models.TextField()
    modeling_do = models.TextField()
    practice = models.TextField()
    feedback = models.TextField()
    evaluation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.performance)

class SupervisionFeedback(models.Model):
    supervisee = models.CharField(max_length=480, null=True, blank=True)
    supervisor = models.CharField(max_length=480, null=True, blank=True)
    setting = models.CharField(max_length=480, null=True, blank=True)
    date = models.CharField(max_length=480, null=True, blank=True)
    rational = models.TextField()
    modeling_say = models.TextField()
    modeling_do = models.TextField()
    practice = models.TextField()
    feedback = models.TextField()
    evaluation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.supervisee)

class JobModel(models.Model):
    position = models.CharField(max_length=480, null=True, blank=True)
    supervisor = models.CharField(max_length=480, null=True, blank=True)
    job_mission = models.CharField(max_length=480, null=True, blank=True)
    job_responsibility_1 = models.TextField()
    skills1_a01 = models.BooleanField()
    skills1_a02 = models.BooleanField()
    skills1_a03 = models.BooleanField()
    skills1_a04 = models.BooleanField()
    skills1_a05 = models.BooleanField()
    skills1_a06 = models.BooleanField()
    skills1_a07 = models.BooleanField()
    skills1_a08 = models.BooleanField()
    skills1_a09 = models.BooleanField()
    skills1_a10 = models.BooleanField()
    skills1_a11 = models.BooleanField()
    skills1_a12 = models.BooleanField()
    skills1_a13 = models.BooleanField()
    skills1_a14 = models.BooleanField()
    skills1_b01 = models.BooleanField()
    skills1_b02 = models.BooleanField()
    skills1_b03 = models.BooleanField()
    skills1_b04 = models.BooleanField()
    skills1_b05 = models.BooleanField()
    skills1_b06 = models.BooleanField()
    skills1_b07 = models.BooleanField()
    skills1_b08 = models.BooleanField()
    skills1_b09 = models.BooleanField()
    skills1_b10 = models.BooleanField()
    skills1_b11 = models.BooleanField()
    skills1_c01 = models.BooleanField()
    skills1_c02 = models.BooleanField()
    skills1_c03 = models.BooleanField()
    skills1_d01 = models.BooleanField()
    skills1_d02 = models.BooleanField()
    skills1_d03 = models.BooleanField()
    skills1_d04 = models.BooleanField()
    skills1_d05 = models.BooleanField()
    skills1_d06 = models.BooleanField()
    skills1_d07 = models.BooleanField()
    skills1_d08 = models.BooleanField()
    skills1_d09 = models.BooleanField()
    skills1_d10 = models.BooleanField()
    skills1_d11 = models.BooleanField()
    skills1_d12 = models.BooleanField()
    skills1_d13 = models.BooleanField()
    skills1_d14 = models.BooleanField()
    skills1_d15 = models.BooleanField()
    skills1_d16 = models.BooleanField()
    skills1_d17 = models.BooleanField()
    skills1_d18 = models.BooleanField()
    skills1_d19 = models.BooleanField()
    skills1_d20 = models.BooleanField()
    skills1_d21 = models.BooleanField()
    skills1_e01 = models.BooleanField()
    skills1_e02 = models.BooleanField()
    skills1_e03 = models.BooleanField()
    skills1_e04 = models.BooleanField()
    skills1_e05 = models.BooleanField()
    skills1_e06 = models.BooleanField()
    skills1_e07 = models.BooleanField()
    skills1_e08 = models.BooleanField()
    skills1_e09 = models.BooleanField()
    skills1_e10 = models.BooleanField()
    skills1_e11 = models.BooleanField()
    skills1_e12 = models.BooleanField()
    skills1_e13 = models.BooleanField()
    skills1_f01 = models.BooleanField()
    skills1_f02 = models.BooleanField()
    skills1_f03 = models.BooleanField()
    skills1_f04 = models.BooleanField()
    skills1_f05 = models.BooleanField()
    skills1_f06 = models.BooleanField()
    skills1_f07 = models.BooleanField()
    skills1_f08 = models.BooleanField()
    skills1_g01 = models.BooleanField()
    skills1_g02 = models.BooleanField()
    skills1_g03 = models.BooleanField()
    skills1_g04 = models.BooleanField()
    skills1_g05 = models.BooleanField()
    skills1_g06 = models.BooleanField()
    skills1_g07 = models.BooleanField()
    skills1_g08 = models.BooleanField()
    skills1_h01 = models.BooleanField()
    skills1_h02 = models.BooleanField()
    skills1_h03 = models.BooleanField()
    skills1_h04 = models.BooleanField()
    skills1_h05 = models.BooleanField()
    skills1_i01 = models.BooleanField()
    skills1_i02 = models.BooleanField()
    skills1_i03 = models.BooleanField()
    skills1_i04 = models.BooleanField()
    skills1_i05 = models.BooleanField()
    skills1_i06 = models.BooleanField()
    skills1_i07 = models.BooleanField()
    skills1_j01 = models.BooleanField()
    skills1_j02 = models.BooleanField()
    skills1_j03 = models.BooleanField()
    skills1_j04 = models.BooleanField()
    skills1_j05 = models.BooleanField()
    skills1_j06 = models.BooleanField()
    skills1_j07 = models.BooleanField()
    skills1_j08 = models.BooleanField()
    skills1_j09 = models.BooleanField()
    skills1_j10 = models.BooleanField()
    skills1_j11 = models.BooleanField()
    skills1_j12 = models.BooleanField()
    skills1_j13 = models.BooleanField()
    skills1_j14 = models.BooleanField()
    skills1_j15 = models.BooleanField()
    skills1_k01 = models.BooleanField()
    skills1_k02 = models.BooleanField()
    skills1_k03 = models.BooleanField()
    skills1_k04 = models.BooleanField()
    skills1_k05 = models.BooleanField()
    skills1_k06 = models.BooleanField()
    skills1_k07 = models.BooleanField()
    skills1_k08 = models.BooleanField()
    skills1_k09 = models.BooleanField()
    skills1_k10 = models.BooleanField()
    job_responsibility_2 = models.TextField()
    skills2_a01 = models.BooleanField()
    skills2_a02 = models.BooleanField()
    skills2_a03 = models.BooleanField()
    skills2_a04 = models.BooleanField()
    skills2_a05 = models.BooleanField()
    skills2_a06 = models.BooleanField()
    skills2_a07 = models.BooleanField()
    skills2_a08 = models.BooleanField()
    skills2_a09 = models.BooleanField()
    skills2_a10 = models.BooleanField()
    skills2_a11 = models.BooleanField()
    skills2_a12 = models.BooleanField()
    skills2_a13 = models.BooleanField()
    skills2_a14 = models.BooleanField()
    skills2_b01 = models.BooleanField()
    skills2_b02 = models.BooleanField()
    skills2_b03 = models.BooleanField()
    skills2_b04 = models.BooleanField()
    skills2_b05 = models.BooleanField()
    skills2_b06 = models.BooleanField()
    skills2_b07 = models.BooleanField()
    skills2_b08 = models.BooleanField()
    skills2_b09 = models.BooleanField()
    skills2_b10 = models.BooleanField()
    skills2_b11 = models.BooleanField()
    skills2_c01 = models.BooleanField()
    skills2_c02 = models.BooleanField()
    skills2_c03 = models.BooleanField()
    skills2_d01 = models.BooleanField()
    skills2_d02 = models.BooleanField()
    skills2_d03 = models.BooleanField()
    skills2_d04 = models.BooleanField()
    skills2_d05 = models.BooleanField()
    skills2_d06 = models.BooleanField()
    skills2_d07 = models.BooleanField()
    skills2_d08 = models.BooleanField()
    skills2_d09 = models.BooleanField()
    skills2_d10 = models.BooleanField()
    skills2_d11 = models.BooleanField()
    skills2_d12 = models.BooleanField()
    skills2_d13 = models.BooleanField()
    skills2_d14 = models.BooleanField()
    skills2_d15 = models.BooleanField()
    skills2_d16 = models.BooleanField()
    skills2_d17 = models.BooleanField()
    skills2_d18 = models.BooleanField()
    skills2_d19 = models.BooleanField()
    skills2_d20 = models.BooleanField()
    skills2_d21 = models.BooleanField()
    skills2_e01 = models.BooleanField()
    skills2_e02 = models.BooleanField()
    skills2_e03 = models.BooleanField()
    skills2_e04 = models.BooleanField()
    skills2_e05 = models.BooleanField()
    skills2_e06 = models.BooleanField()
    skills2_e07 = models.BooleanField()
    skills2_e08 = models.BooleanField()
    skills2_e09 = models.BooleanField()
    skills2_e10 = models.BooleanField()
    skills2_e11 = models.BooleanField()
    skills2_e12 = models.BooleanField()
    skills2_e13 = models.BooleanField()
    skills2_f01 = models.BooleanField()
    skills2_f02 = models.BooleanField()
    skills2_f03 = models.BooleanField()
    skills2_f04 = models.BooleanField()
    skills2_f05 = models.BooleanField()
    skills2_f06 = models.BooleanField()
    skills2_f07 = models.BooleanField()
    skills2_f08 = models.BooleanField()
    skills2_g01 = models.BooleanField()
    skills2_g02 = models.BooleanField()
    skills2_g03 = models.BooleanField()
    skills2_g04 = models.BooleanField()
    skills2_g05 = models.BooleanField()
    skills2_g06 = models.BooleanField()
    skills2_g07 = models.BooleanField()
    skills2_g08 = models.BooleanField()
    skills2_h01 = models.BooleanField()
    skills2_h02 = models.BooleanField()
    skills2_h03 = models.BooleanField()
    skills2_h04 = models.BooleanField()
    skills2_h05 = models.BooleanField()
    skills2_i01 = models.BooleanField()
    skills2_i02 = models.BooleanField()
    skills2_i03 = models.BooleanField()
    skills2_i04 = models.BooleanField()
    skills2_i05 = models.BooleanField()
    skills2_i06 = models.BooleanField()
    skills2_i07 = models.BooleanField()
    skills2_j01 = models.BooleanField()
    skills2_j02 = models.BooleanField()
    skills2_j03 = models.BooleanField()
    skills2_j04 = models.BooleanField()
    skills2_j05 = models.BooleanField()
    skills2_j06 = models.BooleanField()
    skills2_j07 = models.BooleanField()
    skills2_j08 = models.BooleanField()
    skills2_j09 = models.BooleanField()
    skills2_j10 = models.BooleanField()
    skills2_j11 = models.BooleanField()
    skills2_j12 = models.BooleanField()
    skills2_j13 = models.BooleanField()
    skills2_j14 = models.BooleanField()
    skills2_j15 = models.BooleanField()
    skills2_k01 = models.BooleanField()
    skills2_k02 = models.BooleanField()
    skills2_k03 = models.BooleanField()
    skills2_k04 = models.BooleanField()
    skills2_k05 = models.BooleanField()
    skills2_k06 = models.BooleanField()
    skills2_k07 = models.BooleanField()
    skills2_k08 = models.BooleanField()
    skills2_k09 = models.BooleanField()
    skills2_k10 = models.BooleanField()
    job_responsibility_3 = models.TextField()
    skills3_a01 = models.BooleanField()
    skills3_a02 = models.BooleanField()
    skills3_a03 = models.BooleanField()
    skills3_a04 = models.BooleanField()
    skills3_a05 = models.BooleanField()
    skills3_a06 = models.BooleanField()
    skills3_a07 = models.BooleanField()
    skills3_a08 = models.BooleanField()
    skills3_a09 = models.BooleanField()
    skills3_a10 = models.BooleanField()
    skills3_a11 = models.BooleanField()
    skills3_a12 = models.BooleanField()
    skills3_a13 = models.BooleanField()
    skills3_a14 = models.BooleanField()
    skills3_b01 = models.BooleanField()
    skills3_b02 = models.BooleanField()
    skills3_b03 = models.BooleanField()
    skills3_b04 = models.BooleanField()
    skills3_b05 = models.BooleanField()
    skills3_b06 = models.BooleanField()
    skills3_b07 = models.BooleanField()
    skills3_b08 = models.BooleanField()
    skills3_b09 = models.BooleanField()
    skills3_b10 = models.BooleanField()
    skills3_b11 = models.BooleanField()
    skills3_c01 = models.BooleanField()
    skills3_c02 = models.BooleanField()
    skills3_c03 = models.BooleanField()
    skills3_d01 = models.BooleanField()
    skills3_d02 = models.BooleanField()
    skills3_d03 = models.BooleanField()
    skills3_d04 = models.BooleanField()
    skills3_d05 = models.BooleanField()
    skills3_d06 = models.BooleanField()
    skills3_d07 = models.BooleanField()
    skills3_d08 = models.BooleanField()
    skills3_d09 = models.BooleanField()
    skills3_d10 = models.BooleanField()
    skills3_d11 = models.BooleanField()
    skills3_d12 = models.BooleanField()
    skills3_d13 = models.BooleanField()
    skills3_d14 = models.BooleanField()
    skills3_d15 = models.BooleanField()
    skills3_d16 = models.BooleanField()
    skills3_d17 = models.BooleanField()
    skills3_d18 = models.BooleanField()
    skills3_d19 = models.BooleanField()
    skills3_d20 = models.BooleanField()
    skills3_d21 = models.BooleanField()
    skills3_e01 = models.BooleanField()
    skills3_e02 = models.BooleanField()
    skills3_e03 = models.BooleanField()
    skills3_e04 = models.BooleanField()
    skills3_e05 = models.BooleanField()
    skills3_e06 = models.BooleanField()
    skills3_e07 = models.BooleanField()
    skills3_e08 = models.BooleanField()
    skills3_e09 = models.BooleanField()
    skills3_e10 = models.BooleanField()
    skills3_e11 = models.BooleanField()
    skills3_e12 = models.BooleanField()
    skills3_e13 = models.BooleanField()
    skills3_f01 = models.BooleanField()
    skills3_f02 = models.BooleanField()
    skills3_f03 = models.BooleanField()
    skills3_f04 = models.BooleanField()
    skills3_f05 = models.BooleanField()
    skills3_f06 = models.BooleanField()
    skills3_f07 = models.BooleanField()
    skills3_f08 = models.BooleanField()
    skills3_g01 = models.BooleanField()
    skills3_g02 = models.BooleanField()
    skills3_g03 = models.BooleanField()
    skills3_g04 = models.BooleanField()
    skills3_g05 = models.BooleanField()
    skills3_g06 = models.BooleanField()
    skills3_g07 = models.BooleanField()
    skills3_g08 = models.BooleanField()
    skills3_h01 = models.BooleanField()
    skills3_h02 = models.BooleanField()
    skills3_h03 = models.BooleanField()
    skills3_h04 = models.BooleanField()
    skills3_h05 = models.BooleanField()
    skills3_i01 = models.BooleanField()
    skills3_i02 = models.BooleanField()
    skills3_i03 = models.BooleanField()
    skills3_i04 = models.BooleanField()
    skills3_i05 = models.BooleanField()
    skills3_i06 = models.BooleanField()
    skills3_i07 = models.BooleanField()
    skills3_j01 = models.BooleanField()
    skills3_j02 = models.BooleanField()
    skills3_j03 = models.BooleanField()
    skills3_j04 = models.BooleanField()
    skills3_j05 = models.BooleanField()
    skills3_j06 = models.BooleanField()
    skills3_j07 = models.BooleanField()
    skills3_j08 = models.BooleanField()
    skills3_j09 = models.BooleanField()
    skills3_j10 = models.BooleanField()
    skills3_j11 = models.BooleanField()
    skills3_j12 = models.BooleanField()
    skills3_j13 = models.BooleanField()
    skills3_j14 = models.BooleanField()
    skills3_j15 = models.BooleanField()
    skills3_k01 = models.BooleanField()
    skills3_k02 = models.BooleanField()
    skills3_k03 = models.BooleanField()
    skills3_k04 = models.BooleanField()
    skills3_k05 = models.BooleanField()
    skills3_k06 = models.BooleanField()
    skills3_k07 = models.BooleanField()
    skills3_k08 = models.BooleanField()
    skills3_k09 = models.BooleanField()
    skills3_k10 = models.BooleanField()
    job_responsibility_4 = models.TextField()
    skills4_a01 = models.BooleanField()
    skills4_a02 = models.BooleanField()
    skills4_a03 = models.BooleanField()
    skills4_a04 = models.BooleanField()
    skills4_a05 = models.BooleanField()
    skills4_a06 = models.BooleanField()
    skills4_a07 = models.BooleanField()
    skills4_a08 = models.BooleanField()
    skills4_a09 = models.BooleanField()
    skills4_a10 = models.BooleanField()
    skills4_a11 = models.BooleanField()
    skills4_a12 = models.BooleanField()
    skills4_a13 = models.BooleanField()
    skills4_a14 = models.BooleanField()
    skills4_b01 = models.BooleanField()
    skills4_b02 = models.BooleanField()
    skills4_b03 = models.BooleanField()
    skills4_b04 = models.BooleanField()
    skills4_b05 = models.BooleanField()
    skills4_b06 = models.BooleanField()
    skills4_b07 = models.BooleanField()
    skills4_b08 = models.BooleanField()
    skills4_b09 = models.BooleanField()
    skills4_b10 = models.BooleanField()
    skills4_b11 = models.BooleanField()
    skills4_c01 = models.BooleanField()
    skills4_c02 = models.BooleanField()
    skills4_c03 = models.BooleanField()
    skills4_d01 = models.BooleanField()
    skills4_d02 = models.BooleanField()
    skills4_d03 = models.BooleanField()
    skills4_d04 = models.BooleanField()
    skills4_d05 = models.BooleanField()
    skills4_d06 = models.BooleanField()
    skills4_d07 = models.BooleanField()
    skills4_d08 = models.BooleanField()
    skills4_d09 = models.BooleanField()
    skills4_d10 = models.BooleanField()
    skills4_d11 = models.BooleanField()
    skills4_d12 = models.BooleanField()
    skills4_d13 = models.BooleanField()
    skills4_d14 = models.BooleanField()
    skills4_d15 = models.BooleanField()
    skills4_d16 = models.BooleanField()
    skills4_d17 = models.BooleanField()
    skills4_d18 = models.BooleanField()
    skills4_d19 = models.BooleanField()
    skills4_d20 = models.BooleanField()
    skills4_d21 = models.BooleanField()
    skills4_e01 = models.BooleanField()
    skills4_e02 = models.BooleanField()
    skills4_e03 = models.BooleanField()
    skills4_e04 = models.BooleanField()
    skills4_e05 = models.BooleanField()
    skills4_e06 = models.BooleanField()
    skills4_e07 = models.BooleanField()
    skills4_e08 = models.BooleanField()
    skills4_e09 = models.BooleanField()
    skills4_e10 = models.BooleanField()
    skills4_e11 = models.BooleanField()
    skills4_e12 = models.BooleanField()
    skills4_e13 = models.BooleanField()
    skills4_f01 = models.BooleanField()
    skills4_f02 = models.BooleanField()
    skills4_f03 = models.BooleanField()
    skills4_f04 = models.BooleanField()
    skills4_f05 = models.BooleanField()
    skills4_f06 = models.BooleanField()
    skills4_f07 = models.BooleanField()
    skills4_f08 = models.BooleanField()
    skills4_g01 = models.BooleanField()
    skills4_g02 = models.BooleanField()
    skills4_g03 = models.BooleanField()
    skills4_g04 = models.BooleanField()
    skills4_g05 = models.BooleanField()
    skills4_g06 = models.BooleanField()
    skills4_g07 = models.BooleanField()
    skills4_g08 = models.BooleanField()
    skills4_h01 = models.BooleanField()
    skills4_h02 = models.BooleanField()
    skills4_h03 = models.BooleanField()
    skills4_h04 = models.BooleanField()
    skills4_h05 = models.BooleanField()
    skills4_i01 = models.BooleanField()
    skills4_i02 = models.BooleanField()
    skills4_i03 = models.BooleanField()
    skills4_i04 = models.BooleanField()
    skills4_i05 = models.BooleanField()
    skills4_i06 = models.BooleanField()
    skills4_i07 = models.BooleanField()
    skills4_j01 = models.BooleanField()
    skills4_j02 = models.BooleanField()
    skills4_j03 = models.BooleanField()
    skills4_j04 = models.BooleanField()
    skills4_j05 = models.BooleanField()
    skills4_j06 = models.BooleanField()
    skills4_j07 = models.BooleanField()
    skills4_j08 = models.BooleanField()
    skills4_j09 = models.BooleanField()
    skills4_j10 = models.BooleanField()
    skills4_j11 = models.BooleanField()
    skills4_j12 = models.BooleanField()
    skills4_j13 = models.BooleanField()
    skills4_j14 = models.BooleanField()
    skills4_j15 = models.BooleanField()
    skills4_k01 = models.BooleanField()
    skills4_k02 = models.BooleanField()
    skills4_k03 = models.BooleanField()
    skills4_k04 = models.BooleanField()
    skills4_k05 = models.BooleanField()
    skills4_k06 = models.BooleanField()
    skills4_k07 = models.BooleanField()
    skills4_k08 = models.BooleanField()
    skills4_k09 = models.BooleanField()
    skills4_k10 = models.BooleanField()
    job_responsibility_5 = models.TextField()
    skills5_a01 = models.BooleanField()
    skills5_a02 = models.BooleanField()
    skills5_a03 = models.BooleanField()
    skills5_a04 = models.BooleanField()
    skills5_a05 = models.BooleanField()
    skills5_a06 = models.BooleanField()
    skills5_a07 = models.BooleanField()
    skills5_a08 = models.BooleanField()
    skills5_a09 = models.BooleanField()
    skills5_a10 = models.BooleanField()
    skills5_a11 = models.BooleanField()
    skills5_a12 = models.BooleanField()
    skills5_a13 = models.BooleanField()
    skills5_a14 = models.BooleanField()
    skills5_b01 = models.BooleanField()
    skills5_b02 = models.BooleanField()
    skills5_b03 = models.BooleanField()
    skills5_b04 = models.BooleanField()
    skills5_b05 = models.BooleanField()
    skills5_b06 = models.BooleanField()
    skills5_b07 = models.BooleanField()
    skills5_b08 = models.BooleanField()
    skills5_b09 = models.BooleanField()
    skills5_b10 = models.BooleanField()
    skills5_b11 = models.BooleanField()
    skills5_c01 = models.BooleanField()
    skills5_c02 = models.BooleanField()
    skills5_c03 = models.BooleanField()
    skills5_d01 = models.BooleanField()
    skills5_d02 = models.BooleanField()
    skills5_d03 = models.BooleanField()
    skills5_d04 = models.BooleanField()
    skills5_d05 = models.BooleanField()
    skills5_d06 = models.BooleanField()
    skills5_d07 = models.BooleanField()
    skills5_d08 = models.BooleanField()
    skills5_d09 = models.BooleanField()
    skills5_d10 = models.BooleanField()
    skills5_d11 = models.BooleanField()
    skills5_d12 = models.BooleanField()
    skills5_d13 = models.BooleanField()
    skills5_d14 = models.BooleanField()
    skills5_d15 = models.BooleanField()
    skills5_d16 = models.BooleanField()
    skills5_d17 = models.BooleanField()
    skills5_d18 = models.BooleanField()
    skills5_d19 = models.BooleanField()
    skills5_d20 = models.BooleanField()
    skills5_d21 = models.BooleanField()
    skills5_e01 = models.BooleanField()
    skills5_e02 = models.BooleanField()
    skills5_e03 = models.BooleanField()
    skills5_e04 = models.BooleanField()
    skills5_e05 = models.BooleanField()
    skills5_e06 = models.BooleanField()
    skills5_e07 = models.BooleanField()
    skills5_e08 = models.BooleanField()
    skills5_e09 = models.BooleanField()
    skills5_e10 = models.BooleanField()
    skills5_e11 = models.BooleanField()
    skills5_e12 = models.BooleanField()
    skills5_e13 = models.BooleanField()
    skills5_f01 = models.BooleanField()
    skills5_f02 = models.BooleanField()
    skills5_f03 = models.BooleanField()
    skills5_f04 = models.BooleanField()
    skills5_f05 = models.BooleanField()
    skills5_f06 = models.BooleanField()
    skills5_f07 = models.BooleanField()
    skills5_f08 = models.BooleanField()
    skills5_g01 = models.BooleanField()
    skills5_g02 = models.BooleanField()
    skills5_g03 = models.BooleanField()
    skills5_g04 = models.BooleanField()
    skills5_g05 = models.BooleanField()
    skills5_g06 = models.BooleanField()
    skills5_g07 = models.BooleanField()
    skills5_g08 = models.BooleanField()
    skills5_h01 = models.BooleanField()
    skills5_h02 = models.BooleanField()
    skills5_h03 = models.BooleanField()
    skills5_h04 = models.BooleanField()
    skills5_h05 = models.BooleanField()
    skills5_i01 = models.BooleanField()
    skills5_i02 = models.BooleanField()
    skills5_i03 = models.BooleanField()
    skills5_i04 = models.BooleanField()
    skills5_i05 = models.BooleanField()
    skills5_i06 = models.BooleanField()
    skills5_i07 = models.BooleanField()
    skills5_j01 = models.BooleanField()
    skills5_j02 = models.BooleanField()
    skills5_j03 = models.BooleanField()
    skills5_j04 = models.BooleanField()
    skills5_j05 = models.BooleanField()
    skills5_j06 = models.BooleanField()
    skills5_j07 = models.BooleanField()
    skills5_j08 = models.BooleanField()
    skills5_j09 = models.BooleanField()
    skills5_j10 = models.BooleanField()
    skills5_j11 = models.BooleanField()
    skills5_j12 = models.BooleanField()
    skills5_j13 = models.BooleanField()
    skills5_j14 = models.BooleanField()
    skills5_j15 = models.BooleanField()
    skills5_k01 = models.BooleanField()
    skills5_k02 = models.BooleanField()
    skills5_k03 = models.BooleanField()
    skills5_k04 = models.BooleanField()
    skills5_k05 = models.BooleanField()
    skills5_k06 = models.BooleanField()
    skills5_k07 = models.BooleanField()
    skills5_k08 = models.BooleanField()
    skills5_k09 = models.BooleanField()
    skills5_k10 = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

class TaskAnalysis(models.Model):
    performance = models.CharField(max_length=480, null=True, blank=True)
    triggering_event = models.CharField(max_length=480, null=True, blank=True)
    ending_event = models.CharField(max_length=480, null=True, blank=True)
    materials1 = models.CharField(max_length=480, null=True, blank=True)
    location1 = models.CharField(max_length=480, null=True, blank=True)
    materials2 = models.CharField(max_length=480, null=True, blank=True)
    location2 = models.CharField(max_length=480, null=True, blank=True)
    materials3 = models.CharField(max_length=480, null=True, blank=True)
    location3 = models.CharField(max_length=480, null=True, blank=True)
    materials4 = models.CharField(max_length=480, null=True, blank=True)
    location4 = models.CharField(max_length=480, null=True, blank=True)
    task_steps = models.TextField()
    permanant_products = models.CharField(max_length=480, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

class SkillsChecklist(models.Model):
    supervisor_id = models.ForeignKey(Supervisee)
    a01 = models.BooleanField()
    a02 = models.BooleanField()
    a03 = models.BooleanField()
    a04 = models.BooleanField()
    a05 = models.BooleanField()
    a06 = models.BooleanField()
    a07 = models.BooleanField()
    a08 = models.BooleanField()
    a09 = models.BooleanField()
    a10 = models.BooleanField()
    a11 = models.BooleanField()
    a12 = models.BooleanField()
    a13 = models.BooleanField()
    a14 = models.BooleanField()
    b01 = models.BooleanField()
    b02 = models.BooleanField()
    b03 = models.BooleanField()
    b04 = models.BooleanField()
    b05 = models.BooleanField()
    b06 = models.BooleanField()
    b07 = models.BooleanField()
    b08 = models.BooleanField()
    b09 = models.BooleanField()
    b10 = models.BooleanField()
    b11 = models.BooleanField()
    c01 = models.BooleanField()
    c02 = models.BooleanField()
    c03 = models.BooleanField()
    d01 = models.BooleanField()
    d02 = models.BooleanField()
    d03 = models.BooleanField()
    d04 = models.BooleanField()
    d05 = models.BooleanField()
    d06 = models.BooleanField()
    d07 = models.BooleanField()
    d08 = models.BooleanField()
    d09 = models.BooleanField()
    d10 = models.BooleanField()
    d11 = models.BooleanField()
    d12 = models.BooleanField()
    d13 = models.BooleanField()
    d14 = models.BooleanField()
    d15 = models.BooleanField()
    d16 = models.BooleanField()
    d17 = models.BooleanField()
    d18 = models.BooleanField()
    d19 = models.BooleanField()
    d20 = models.BooleanField()
    d21 = models.BooleanField()
    e01 = models.BooleanField()
    e02 = models.BooleanField()
    e03 = models.BooleanField()
    e04 = models.BooleanField()
    e05 = models.BooleanField()
    e06 = models.BooleanField()
    e07 = models.BooleanField()
    e08 = models.BooleanField()
    e09 = models.BooleanField()
    e10 = models.BooleanField()
    e11 = models.BooleanField()
    e12 = models.BooleanField()
    e13 = models.BooleanField()
    f01 = models.BooleanField()
    f02 = models.BooleanField()
    f03 = models.BooleanField()
    f04 = models.BooleanField()
    f05 = models.BooleanField()
    f06 = models.BooleanField()
    f07 = models.BooleanField()
    f08 = models.BooleanField()
    g01 = models.BooleanField()
    g02 = models.BooleanField()
    g03 = models.BooleanField()
    g04 = models.BooleanField()
    g05 = models.BooleanField()
    g06 = models.BooleanField()
    g07 = models.BooleanField()
    g08 = models.BooleanField()
    h01 = models.BooleanField()
    h02 = models.BooleanField()
    h03 = models.BooleanField()
    h04 = models.BooleanField()
    h05 = models.BooleanField()
    i01 = models.BooleanField()
    i02 = models.BooleanField()
    i03 = models.BooleanField()
    i04 = models.BooleanField()
    i05 = models.BooleanField()
    i06 = models.BooleanField()
    i07 = models.BooleanField()
    j01 = models.BooleanField()
    j02 = models.BooleanField()
    j03 = models.BooleanField()
    j04 = models.BooleanField()
    j05 = models.BooleanField()
    j06 = models.BooleanField()
    j07 = models.BooleanField()
    j08 = models.BooleanField()
    j09 = models.BooleanField()
    j10 = models.BooleanField()
    j11 = models.BooleanField()
    j12 = models.BooleanField()
    j13 = models.BooleanField()
    j14 = models.BooleanField()
    j15 = models.BooleanField()
    k01 = models.BooleanField()
    k02 = models.BooleanField()
    k03 = models.BooleanField()
    k04 = models.BooleanField()
    k05 = models.BooleanField()
    k06 = models.BooleanField()
    k07 = models.BooleanField()
    k08 = models.BooleanField()
    k09 = models.BooleanField()
    k10 = models.BooleanField()
    fk01 = models.BooleanField()
    fk02 = models.BooleanField()
    fk03 = models.BooleanField()
    fk04 = models.BooleanField()
    fk05 = models.BooleanField()
    fk06 = models.BooleanField()
    fk07 = models.BooleanField()
    fk08 = models.BooleanField()
    fk09 = models.BooleanField()
    fk10 = models.BooleanField()
    fk11 = models.BooleanField()
    fk12 = models.BooleanField()
    fk13 = models.BooleanField()
    fk14 = models.BooleanField()
    fk15 = models.BooleanField()
    fk16 = models.BooleanField()
    fk17 = models.BooleanField()
    fk18 = models.BooleanField()
    fk19 = models.BooleanField()
    fk20 = models.BooleanField()
    fk21 = models.BooleanField()
    fk22 = models.BooleanField()
    fk23 = models.BooleanField()
    fk24 = models.BooleanField()
    fk25 = models.BooleanField()
    fk26 = models.BooleanField()
    fk27 = models.BooleanField()
    fk28 = models.BooleanField()
    fk29 = models.BooleanField()
    fk30 = models.BooleanField()
    fk31 = models.BooleanField()
    fk32 = models.BooleanField()
    fk33 = models.BooleanField()
    fk34 = models.BooleanField()
    fk35 = models.BooleanField()
    fk36 = models.BooleanField()
    fk37 = models.BooleanField()
    fk38 = models.BooleanField()
    fk39 = models.BooleanField()
    fk40 = models.BooleanField()
    fk41 = models.BooleanField()
    fk42 = models.BooleanField()
    fk43 = models.BooleanField()
    fk44 = models.BooleanField()
    fk45 = models.BooleanField()
    fk46 = models.BooleanField()
    fk47 = models.BooleanField()
    fk48 = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

class SelfAssessment(models.Model):
    Allergies = models.BooleanField('Allergies:')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.Allergies)

