from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Re Enter Password',widget=forms.PasswordInput)
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    def clean(self):
        print('validating passwords match...')
        total_cleaned_data=super().clean()
        fpwd=total_cleaned_data['password']
        spwd=total_cleaned_data['rpassword']
        if fpwd != spwd:
            raise forms.ValidationError('Both passwords must be matched')
