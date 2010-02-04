#coding=utf-8
from django.http import Http404, HttpResponse
from django.views.generic.list_detail import object_detail, object_list
from django.core import serializers 
from libs.shortcuts import render_to
from models import Company
from registration.custom_user import User
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django import forms
from django.db.models import Q, Sum
import re 
from django.conf import settings
from django.shortcuts import redirect
from forms import AccountEditForm, CompanyEditForm, EmployerForm, EmployerEditForm
from backend import EmployerBackend    
backend = EmployerBackend()
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site



@render_to('account/profile_edit.html')
def profile_edit(request):
    if request.method == "POST":
        form = AccountEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            account = form.save()
            return redirect('account_index')
    else:
        form = AccountEditForm(instance=request.user)
        
    return {'form': form
            }

@render_to('account/company_edit.html')
def company_edit(request):
    if request.method == "POST":
        form = CompanyEditForm(request.POST, request.FILES, instance=request.user.company)
        if form.is_valid():
            company = form.save()
            request.user.company = company
            request.user.save()
            return redirect('company_index')
    else:
        form = CompanyEditForm(instance=request.user.company)
        
    return {'form': form
            }    
    
def employer_detail(request, object_id):
    '''
    Выводит подробную информацию о компании-заказчике
    '''
    return object_detail(request,
                         queryset=User.objects.all(),
                         object_id=object_id,
                         )        
EMAIL_SPLIT_RE = re.compile('\n\-{3,}\n')
    
@render_to('account/employer_edit.html')
def employer_add(request):
        
    if request.method == "POST":
        form = EmployerForm(request.POST)
        if form.is_valid():

            employer = backend.register(request, **form.cleaned_data)
            employer.first_name = form.cleaned_data['first_name'] 
            employer.last_name = form.cleaned_data['last_name']
            employer.position = form.cleaned_data['position']
            employer.phone = form.cleaned_data['phone']
            employer.fax = form.cleaned_data['fax']            
            
            employer.company = request.user.company
            employer.admin = False
            employer.save()

            if Site._meta.installed:
                site = Site.objects.get_current()
            else:
                site = RequestSite(request)
            context_dict = {'user': employer,
                            'password': form.cleaned_data['password1'],
                            'site': site }
            
            email = render_to_string('account/employer_email.txt', context_dict)
            subject, message = EMAIL_SPLIT_RE.split(email, 1)
        
            employer.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)            
            return redirect('company_index')
    else:
        form = EmployerForm()
        
    return {'form': form
            }       

@render_to('account/employer_edit.html')
def employer_edit(request, object_id):

    instance = get_object_or_404(User, id=object_id)
        
    if request.method == "POST":
        form = EmployerEditForm(request.POST, instance=instance)
        if form.is_valid():
            employer = form.save()
            employer.save()
            return redirect('company_index')
    else:
        form = EmployerEditForm(instance=instance)
        
    return {'form': form
            }       

      