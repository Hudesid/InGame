from modeltranslation.translator import register, TranslationOptions
from .models import Attribute


@register(Attribute)
class AttributeTranslationOptions(TranslationOptions):
    fields = ('type',)
    required_languages = {'ru': ('type',), 'uz': ('type',)}