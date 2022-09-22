from dataclasses import field
from django import forms
from django.core import validators
from .models import User

class FormName(forms.Form):
    name = forms.CharField()
    email= forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
