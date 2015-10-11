# -*- coding: utf-8 -*-
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

from lfs.catalog.settings import THUMBNAIL_SIZES
from lfs.core.fields.thumbs import ImageWithThumbsField


class CarouselItem(models.Model):
    """An carousel item with a title, image with several sizes and url.

    Attributes:
        - content
          The content object it belongs to.
        - title
          The title of the image.
        - image
          The image file.
        - link
          The link that can be used 'under' image
        - position
          The position of the image within the content object it belongs to.
    """
    content_type = models.ForeignKey(ContentType, verbose_name=_(u"Content type"), related_name="carousel_item", blank=True, null=True)
    content_id = models.PositiveIntegerField(_(u"Content id"), blank=True, null=True)
    content = GenericForeignKey(ct_field="content_type", fk_field="content_id")

    title = models.CharField(_(u"Title"), blank=True, max_length=100)
    image = ImageWithThumbsField(_(u"Image"), upload_to="images", blank=True, null=True, sizes=THUMBNAIL_SIZES)
    link = models.URLField(_(u"URL"), null=True, blank=True, default='')
    text = models.TextField(_('Text'), null=False, blank=True, default='')
    position = models.PositiveSmallIntegerField(_(u"Position"), default=999)

    class Meta:
        ordering = ("position", )
        app_label = 'lfs_carousel'

    def __unicode__(self):
        return self.title