from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions
)

class SignUpForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

    