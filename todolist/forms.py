from django import forms
from django.contrib.auth.models import User
from .models import TodoList
import datetime

class TodoForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'autofocus': 'True'}))
    description = forms.CharField(required=True, widget=forms.Textarea())
    expire = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'], widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S'),initial=datetime.date.today())
    class Meta:
        model = TodoList
        fields = {
            'name',
            'description',
            'expire',
        }
    # def check_creation(self):
    #     created = self.cleaned_data.get('created')
    #     #Check date is not in past.
    #     if created < datetime.date.today():
    #         raise ValidationError(_('Invalid date - date in past'))
    #     return created
