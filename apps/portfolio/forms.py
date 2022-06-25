from django import forms
from apps.portfolio.models import Account


class DateInput(forms.DateInput):
    input_type = 'date'



class PortfolioForm(forms.ModelForm):
    #first_name = forms.CharField(max_length=50, error_messages={'required': 'This is a custom error message for #862'}) # Required
    #test = forms.CharField(max_length=50) # Required
    #portfolio = forms.CharField(widget=forms.Textarea)



    class Meta:
        widgets = {'deadline': DateInput()}
        model = Account
        fields = ['name', 'comments', 'priority', 'deadline']



# class IsinForm(forms.ModelForm):
#     isin = forms.CharField(widget=forms.Textarea)
#
#     class Meta:
#         model = ISIN
#         fields = ['isin']



class IdentifierForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)

