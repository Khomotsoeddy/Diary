from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('article',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['article'].widget.attrs.update({'class' : 'textarea', 'placeholder': 'What\'s on your mind'})