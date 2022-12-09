from django import forms
from .models import Uploader
class UserForm(forms.ModelForm):
  class Meta:
    model = Uploader
    fields = '__all__'