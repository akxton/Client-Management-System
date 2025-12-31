from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'client_id',
            'name',
            'company_name',
            'project_name',
            'project_deadline',
            'pay_amount',
            'email',
            'phone',
            'address',
        ]
        widgets = {
            'project_deadline': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
