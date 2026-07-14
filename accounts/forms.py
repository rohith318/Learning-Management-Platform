from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "username",
            "full_name",
            "email",
            "role",
            "is_active",
        ]

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "full_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),
            "role": forms.Select(
                attrs={"class": "form-select"}
            ),
            "is_active": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }