# blog/templatetags/my_filters.py
from django import template

register = template.Library()

@register.filter
def truncate_chars(value, max_length):
    """
    Truncate text after max_length characters
    """
    if len(value) > max_length:
        return value[:max_length] + "..."
    return value
