from modeltranslation.translator import register, TranslationOptions
from .models import DeliveryMethod


@register(DeliveryMethod)
class DeliveryMethodTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = {'ru': ('name',), 'uz': ('name',)}