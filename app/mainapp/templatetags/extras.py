from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def split(val, separator=" "):
    return (v for v in val.split(separator) if v)


@register.filter
@stringfilter
def custom_upper(value):
    return value.upper()
