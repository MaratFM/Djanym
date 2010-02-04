"""
Forms and validation code for user registration.

"""


from registration.custom_user import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from models import Company
# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = { 'class': 'required' }


class RegistrationForm(forms.Form):
    """
   
    """
    first_name = forms.CharField(label=_('first name'), max_length=30)
    last_name = forms.CharField(label=_('last name'), max_length=30)
        
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                            label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password (again)"))
    
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']
    
    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data



class AccountEditForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'position', 'phone','fax']


class EmployerForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password (again)"))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'position', 'phone','fax']

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']
    
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data

class EmployerEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'position', 'phone','fax']
        

class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'full_name', 
                  'postal_adr', 'legal_adr', 'url', 'email', 'phone', 'fax', 
                  'ogrn', 'inn', 'kpp', 'okpo', 'okato', 'okogu', 'okfs', 'okopf', 
                  'bank_no', 'bank_no2', 'bank_name', 'bank_adr', 'bank_bik', 
                  'contact1', 'contact2', 'contact3']
 
 
 

