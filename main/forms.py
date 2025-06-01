from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import AdminTheme

class AdminThemeForm(ModelForm):
    class Meta:
        model = AdminTheme
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        css_url = cleaned_data.get("css_url")
        js_url = cleaned_data.get("js_url")

        # Au moins une URL (CSS ou JS) doit être fournie
        if not css_url and not js_url:
            raise ValidationError("Vous devez fournir au moins une URL CSS ou JS.")
        return cleaned_data