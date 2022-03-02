from django import forms
from django.forms import ModelForm
from .models import Meetup


class MeetupForm(ModelForm):

    class Meta:
        model = Meetup
        fields = ['title', 'date', 'time', 'featured_image', 'description', 'dog_sizes', 'location', 'city', 'country']
        widgets = {
            'title': forms.TextInput(),
            'date': forms.SelectDateWidget(),
            'time': forms.TimeInput(),
            'description': forms.Textarea(),
            'dog_sizes': forms.CheckboxSelectMultiple(),
            'location': forms.TextInput(),
            'city': forms.TextInput(),
        }

        def __init__(self, *args, **kwargs):
            super(MeetupForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'form-control'})