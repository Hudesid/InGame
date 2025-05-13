from modeltranslation.translator import register, TranslationOptions
from .models import Banner


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_languages = {'ru': ('name', 'description'), 'uz': ('name', 'description')}