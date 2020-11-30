from django.forms import ModelForm
from .models import TaskList

class CreateTask(ModelForm):
    class Meta:
        model=TaskList
        fields=['task','done']
