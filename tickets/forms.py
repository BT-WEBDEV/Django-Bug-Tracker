from django import forms
from .models import Ticket

### COMMENT FORM ###
class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

### NEW TICKET FORM ###


class TicketForm(forms.ModelForm): 
    
    class Meta: 
        model = Ticket
        fields = (
            'title',
            'reporter', 
            'priorities', 
            'categories', 
            'summary',
            'url',
            'image',
            'platform',
            'operating_system',
            'browser',
            'steps_to_reproduce',
            'expected_result',
            'actual_result',
            'assigned_to'
            )