from modeltranslation.translator import register, TranslationOptions
from .models import Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_languages = {'ru': ('name', 'description'), 'uz': ('name', 'description')}