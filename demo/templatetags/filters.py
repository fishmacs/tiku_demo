from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.filter
def repair_html(str):
    return mark_safe(str.replace('\\n', ''))
