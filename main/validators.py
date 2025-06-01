from django.core.exceptions import ValidationError

def validate_url(url):
 
    if not url.startswith("http") or not (url.endswith(".css") or url.endswith(".js")):
        raise ValidationError(
            "L'URL doit commencer par 'http' et se terminer par '.css' ou '.js'."
        )