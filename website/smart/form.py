from django import forms
from .models import input, Data
import Queue


from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class inputform(forms.ModelForm):
    start_date=forms.DateField(widget=DateInput())

class Meta:
    model = Data
    fields = ('tanggal')
    widgets = {
        'start_date': forms.DateInput(attrs={'class':'datepicker'}),
    }

class GraphForm(forms.Form):
    my_form = forms.CharField(label = 'my_form',max_length=100)
    start_date = forms.DateField(required=True)

