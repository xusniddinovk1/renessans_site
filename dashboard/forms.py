from django import forms
from lager_app.models import Gallery, Education, RestArea, Activity


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(event)"})
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(even)"})
        }


class RestAreaForm(forms.ModelForm):
    class Meta:
        model = RestArea
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(even)"})
        }


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(even)"})
        }