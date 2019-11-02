from django import forms
from django.utils import timezone
from .models import Student, DEGREE_TYPE, GENDER
    
class stu_search_form(forms.Form):
    uin = forms.CharField(label = 'UIN', max_length = 255, widget = forms.TextInput(attrs = {'class': 'w3-input'}))
    last_name = forms.CharField(label = 'Last Name', max_length = 255, widget = forms.TextInput(attrs = {'class': 'w3-input'}))
    first_name = forms.CharField(label = 'First Name', max_length = 255, widget = forms.TextInput(attrs = {'class': 'w3-input'}))
    gender = forms.ChoiceField(widget = forms.Select(attrs = {'class': 'w3-select'}), choices = GENDER)
    degree = forms.ChoiceField(widget = forms.Select(attrs = {'class': 'w3-select'}), choices = DEGREE_TYPE)
    
class create_stu_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['uin', 'first_name', 'middle_name', 'last_name', 'email', 'gender']
        widgets = {
            'uin': forms.TextInput(attrs = {'class': 'w3-input'}),
            'first_name': forms.TextInput(attrs = {'class': 'w3-input w3-light-gray'}),
            'middle_name': forms.TextInput(attrs = {'class': 'w3-input'}),
            'last_name': forms.TextInput(attrs = {'class': 'w3-input w3-light-gray'}),
            'email': forms.EmailInput(attrs = {'class': 'w3-input'}),
            'gender': forms.Select(attrs = {'class': 'w3-select w3-light-gray'}),
        }

def create_doc_form(model_in):
    '''Generate Model Form for docs dynamically'''
    class Meta:
        model = model_in        # model input
        fields = ['doc_type', 'doc', 'notes', 'appr_cs_date', 'appr_ogs_date']
        widgets = {
            'doc_type': forms.Select(attrs={'class': 'w3-select'}),
            'notes': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
            'appr_cs_date': forms.SelectDateWidget\
                (attrs={'class': 'w3-select'},\
                    years = [y for y in range(timezone.now().year - 7, timezone.now().year + 8)]),
            'appr_ogs_date': forms.SelectDateWidget\
                (attrs={'class': 'w3-select'},\
                    years = [y for y in range(timezone.now().year - 7, timezone.now().year + 8)])
        }

    attrs = {'Meta':Meta}

    _model_form_class = type("DynamicModelForm", (forms.ModelForm,), attrs)     
        # Parameters: object name, tuple(input father)，dict of meta
    
    return _model_form_class    # return a class