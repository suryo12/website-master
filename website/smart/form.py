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

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check date is in range librarian allowed to change (+4 weeks).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data