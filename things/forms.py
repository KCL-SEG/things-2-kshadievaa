"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your forms here.

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        exclude = ['created_at']

    description = forms.CharField(
        widget=forms.Textarea,
        max_length=120,
        required=False
    )

    quantity = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    