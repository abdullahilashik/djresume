from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactProfile
        fields = '__all__'

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-field js-field-name',
                'placeholder': 'Your Name'
            }
        ), required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-field js-field-name',
                'placeholder': 'Your\'r email'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-field js-field-name',
                'placeholder': 'Type your message here'
            }
        )
    )
