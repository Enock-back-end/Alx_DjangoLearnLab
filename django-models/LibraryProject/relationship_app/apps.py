from django.apps import AppConfig
from django.db import models
from django.contrib.auth.models import User

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
def ready(self):
    import relationship_app.signals
