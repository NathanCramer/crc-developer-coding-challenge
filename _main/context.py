import os
from django.conf import settings
import secrets


def global_context(request):
    return {
        'open_ai_api_key': secrets.OPEN_AI_API_KEY if settings.STAGE == "dev" else os.environ["OPEN_AI_API_KEY"] ,  # Use environment variable in prod
    }
