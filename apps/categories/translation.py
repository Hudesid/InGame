from modeltranslation.translator import register, TranslationOptions
from .models import Category


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_languages = {'ru': ('name', 'description'), 'uz': ('name', 'description')}