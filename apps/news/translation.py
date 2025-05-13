from modeltranslation.translator import register, TranslationOptions
from .models import New


@register(New)
class NewTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = {'ru': ('title', 'description'), 'uz': ('title', 'description')}