from django import forms
from models import Gallery, Education, RestArea, Activity


class GalleryForm(forms.ModelForm):
    model = Gallery
    fields = "__all__"


class RestAreaForm(forms.ModelForm):
    model = RestArea
    fields = "__all__"


class EducationForm(forms.ModelForm):
    model = Education
    fields = "__all__"


class ActivityForm(forms.ModelForm):
    model = Activity
    fields = "__all__"
