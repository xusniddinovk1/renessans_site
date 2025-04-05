from django import forms
from models import Fotogalereya, OquvBolim, IstirohatZona, Faoliyat


class FotogalereyaForm(forms.ModelForm):
    model = Fotogalereya
    fields = "__all__"


class IstirohatZonaForm(forms.ModelForm):
    model = IstirohatZona
    fields = "__all__"


class OquvBolimForm(forms.ModelForm):
    model = OquvBolim
    fields = "__all__"


class FaoliyatForm(forms.ModelForm):
    model = Faoliyat
    fields = "__all__"
