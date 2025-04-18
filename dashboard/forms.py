from django import forms
from lager_app.models import Gallery, Education, RestArea, Activity


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control",
                                            "onchange": "loadFile(even)"})
        }
