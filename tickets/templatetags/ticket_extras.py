from django import template
from tickets.models import Category, Priority

register = template.Library()

# Sidebar Category List
@register.inclusion_tag('category_list.html')
def get_category_list():
    categories = Category.objects.filter()
    return {'categories': categories}


# Sidebar Priority List
@register.inclusion_tag('priority_list.html')
def get_priority_list():
    priorities = Priority.objects.filter()
    return {'priorities': priorities}