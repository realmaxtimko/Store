from django import template
from django.forms.boundfield import BoundField

register = template.Library()

@register.filter
def add_class(field, css_class):
    # Перевіряємо, чи це поле форми
    if isinstance(field, BoundField):
        return field.as_widget(attrs={"class": css_class})
    # Повертаємо поле без змін, якщо це не BoundField
    return field  

@register.filter
def add_placeholder(field, placeholder):
    # Перевіряємо, чи це поле форми
    if isinstance(field, BoundField):
        return field.as_widget(attrs={"placeholder": placeholder})
    # Повертаємо поле без змін, якщо це не BoundField
    return field
