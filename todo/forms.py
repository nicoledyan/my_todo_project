from django import forms
from django.utils.timezone import now

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed', 'complete_by', 'priority']
        widgets = {
            'complete_by': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'priority': forms.Select(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')]),
        }

    # Custom validation for 'complete_by' field
    def clean_complete_by(self):
        complete_by = self.cleaned_data.get('complete_by')
        if complete_by and complete_by < now():
            raise forms.ValidationError("Due date cannot be in the past.")
        return complete_by
