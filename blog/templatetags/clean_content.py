import bleach 
from django import template 

register = template.Library()

ALLOWED_TAGS = ['b', 'i', 'u', 'strong', 'em', 'p', 'br', 'ul', 'ol', 'li', 'a'] 
ALLOWED_ATTRIBUTES = {'a': ['href', 'title']} 

@register.filter(name='clean_html') 
def clean_html(value): 
    return bleach.clean(value, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, strip=True)