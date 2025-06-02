🧩 Gestionnaire de Thèmes pour l'Admin Django

Une application pratique pour personnaliser facilement l'apparence de l'interface d'administration Django.
🌟 Fonctionnalités principales

    Changer le thème visuel de l'admin Django en un clic

    Gérer les thèmes via une interface GraphQL moderne

    Traitement automatique des fichiers SCSS (compiler le fichier scss et faire un output css (CSS avancé)

    Vérification de la contrast des couleurs

    Exécution des tâches lourdes en arrière-plan

🛠 Installation
1. Télécharger le projet
bash

git clone https://github.com/bassemoueslati/django-DS-FINAL.git
cd Django_DS-main

2. Installer les dépendances


pipenv install -r requirements.txt

⚙ Configuration
Dans settings.py

Ajouter ces lignes :
python

INSTALLED_APPS = [
    ...
    "graphene_django",  # Pour GraphQL
    "django_celery_beat",  # Pour les tâches planifiées
    "main",  # Notre application principale
]

GRAPHENE = {
    "SCHEMA": "main.schema.schema",  # Configuration GraphQL
}

Lancer Celery

Dans deux terminaux séparés :
bash

# Terminal 1 - Worker
celery -A main worker --pool=threads --loglevel=INFO

# Terminal 2 - Planificateur
celery -A main beat --loglevel=INFO

🖥 Utilisation
Interface GraphQL

Accédez à : http://127.0.0.1:8000/graphql/
Lister les thèmes disponibles
graphql

query {
    allAdminThemes {
        id
        name
        cssUrl
        isActive
    }
}

Changer de thème
graphql

mutation {
    switchTheme(themeId: 3) {
        success
        activeThemeCssUrl
        suggestions
    }
}

🔧 Tâches utiles
Compiler les fichiers SCSS

Depuis le shell Django :
bash

python manage.py shell

Puis :
python

from main.tasks import compile_scss
from main.tasks import compile_scss

# Test ultra-simplifié
try:
    result = compile_scss.apply(args=[
        'static/admin/css.scss', 
        'staticfiles/admin/test.css'
    ]).get()
    print("Résultat:", result)
except Exception as e:
    print("Échec:", str(e))
    print("Vérifiez :")
    print("- Que le worker Celery tourne")
    print("- Que Redis est démarré")
    print("- Que le fichier css.scss existe")



Vérifier l'accessibilité
python

from main.tasks import analyze_theme_accessibility
analyze_theme_accessibility.delay(theme_id=3)

💡 Personnalisation

Modifiez le fichier admin/base_site.html pour inclure :
html

{{ active_theme.css_url }}

🚀 Lancement

Démarrer le serveur :
bash

python manage.py runserver

