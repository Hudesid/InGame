from modeltranslation.translator import register, TranslationOptions
from .models import Comment


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('comment', 'description')
    required_languages = {'ru': ('comment', 'description'), 'uz': ('comment', 'description')}