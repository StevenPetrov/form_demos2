from django import forms
from django.core.exceptions import ValidationError

from form_demos2.web.models import Todo, Person
from form_demos2.web.validators import validate_text, ValueInRangeValidator, validate_max_todos


class TodoForm(forms.Form):
    text = forms.CharField(validators=(validate_text,))
    is_done = forms.BooleanField(required=False)
    priority = forms.IntegerField(validators=(ValueInRangeValidator(1, 15),))


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        return super().clean()

    def clean_text(self):
        return self.cleaned_data['text'].lower()

    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']
        validate_max_todos(assignee)
        return assignee

class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'