from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from company.models import Company
from job.models import JobDescription


class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False

    class Meta:
        model = Company
        fields = ['description']
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }


class JDForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False

    class Meta:
        model = JobDescription
        fields = ['description', 'requirements', 'benefits']
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
