from django.shortcuts import redirect, render
from rest_framework.viewsets import ModelViewSet
from .models import AdminTheme
from .serializers import AdminThemeSerializer
from django.views.decorators.csrf import csrf_exempt
import requests
from rest_framework.permissions import IsAdminUser




class AdminThemeViewSet(ModelViewSet):
    queryset = AdminTheme.objects.all()
    serializer_class = AdminThemeSerializer
    permission_classes=[IsAdminUser]


@csrf_exempt
def switch_theme(request):
    if request.method == "POST":
        theme_id = request.POST.get("theme_id")
        if theme_id:
            # Définir la mutation GraphQL
            mutation = """
            mutation {
                switchTheme(themeId: "%s") {
                    success
                    activeThemeCssUrl
                }
            }
            """ % theme_id

            # Appeler l'API GraphQL
            response = requests.post(
                url="http://127.0.0.1:8000/graphql/",
                json={"query": mutation},
                headers={"Content-Type": "application/json"},
            )

            # Vérifier la réponse
            if response.status_code == 200:
                data = response.json()
                if data.get("data", {}).get("switchTheme", {}).get("success"):
                    # Rediriger vers l'admin après succès
                    return redirect("/admin/")
                else:
                    return redirect("/admin/?error=theme_switch_failed")
            else:
                return redirect("/admin/?error=graphql_request_failed")

    # Rediriger en cas d'erreur
    return redirect("/admin/")