"""
Context processors to make settings available in templates
"""
from django.conf import settings


def settings_context(request):
    """
    Make specific settings available in all templates
    """
    return {
        'settings': {
            'EMAILJS_PUBLIC_KEY': settings.EMAILJS_PUBLIC_KEY,
            'EMAILJS_SERVICE_ID': settings.EMAILJS_SERVICE_ID,
            'EMAILJS_TEMPLATE_ID': settings.EMAILJS_TEMPLATE_ID,
        }
    }
