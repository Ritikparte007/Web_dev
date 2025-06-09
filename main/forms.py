from django import forms
from .models import ContactMessage, QuoteRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+91 XXXXX XXXXX',
                'required': True
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control'
            }, choices=[
                ('Website Development', 'Website Development'),
                ('Game Development', 'Game Development'),
                ('Mobile App', 'Mobile App'),
                ('Django Project', 'Django Project'),
                ('Other', 'Other')
            ]),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe your project requirements, budget, and timeline...',
                'required': True
            })
        }

class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'phone', 'company', 'project_type', 
                 'budget_range', 'description', 'deadline', 'features_needed']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+91 XXXXX XXXXX'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name (Optional)'
            }),
            'project_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'budget_range': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your project requirements in detail...'
            }),
            'deadline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'When do you need it? (e.g., 1 week, 1 month)'
            }),
            'features_needed': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'List specific features you need (optional)...'
            })
        }
