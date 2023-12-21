from django import template

register = template.Library()

@register.filter(name='is_numeric')
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False