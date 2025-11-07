from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "message", "rating"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
            "rating": forms.Select(),
        }