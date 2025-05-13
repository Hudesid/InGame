from modeltranslation.translator import register, TranslationOptions
from .models import Desktop


@register(Desktop)
class DesktopTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_languages = {'ru': ('name', 'description'), 'uz': ('name', 'description')}