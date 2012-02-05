# -*- coding: utf-8 -*-

# django imports
from django.template import Library

from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe

from lfs_carousel import carousel

register = Library()


@register.simple_tag(takes_context=True)
def carousel_management(context, obj):
    request = context.get('request', None)  # we rely on request context processor

    ct = ContentType.objects.get_for_model(obj)

    result = carousel.manage_items(request, ct.pk, obj.pk, as_string=True)
    return mark_safe(result)


@register.inclusion_tag('lfs_carousel/carousel.html', takes_context=True)
def carousel_show(context, obj):
    ct = ContentType.objects.get_for_model(obj)

    items = carousel.get_item_cls().objects.filter(content_type=ct,
                                                   content_id=obj.pk)
    return {'items': items, 'obj': obj, 'ct': ct}