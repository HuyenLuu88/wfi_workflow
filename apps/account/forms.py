from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm
# from django.contrib.account.models import User
from django.core.exceptions import ValidationError

from apps.account.models import User, CompanyRole, Office, Country
from django.utils.translation import gettext_lazy as _
from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, ButtonHolder, Submit
from django_countries import countries
from django.contrib.auth.forms import PasswordChangeForm
from smart_selects.db_fields import ChainedForeignKey
# from django.forms import ModelForm
# from django_otp.models import Device

class RegisterForm(UserCreationForm):
    company_role = forms.ModelChoiceField(queryset=CompanyRole.objects, empty_label='Select Company Role',
                                          required=False)
    office = forms.ModelChoiceField(queryset=Office.objects, empty_label='Select Office', required=False)
    location = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Select Location", required=False)


    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['office'].queryset = Office.objects.none()



        # if 'company_role' in self.data:
        #     try:
        #         company_role_id = int(self.data.get('company_role'))
        #         self.fields['office'].queryset = Office.objects.filter(company_role_id=company_role_id).order_by('name')
        #
        #
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty Office queryset
        # elif self.instance.pk:
        #     self.fields['office'].queryset = self.instance.company_role.office_set.order_by('name')











class PersonalInfoForm(UserChangeForm):
    #username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50, error_messages={'required': 'This is a custom error message for #862'}) # Required
    last_name = forms.CharField(max_length=50) # Required
    #company_role = forms.ModelChoiceField(queryset=CompanyRole.objects, empty_label='fuck off')



    # All fields you re-define here will become required fields in the form

    # helper = FormHelper()
    # helper.layout = Layout(
    #     Field('first_name', css_class='form-control-lg'),
    #
    # )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'company_role', 'location', 'office']


class SecurityForm(PasswordChangeForm):

    helper = FormHelper()
    helper.layout = Layout(
        Field('new_password2', css_class='form-control-lg'),

    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


