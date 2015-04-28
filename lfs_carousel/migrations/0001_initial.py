# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lfs.core.fields.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_id', models.PositiveIntegerField(null=True, verbose_name='Content id', blank=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title', blank=True)),
                ('image', lfs.core.fields.thumbs.ImageWithThumbsField(upload_to=b'images', null=True, verbose_name='Image', sizes=((60, 60), (90, 90), (100, 100), (200, 200), (300, 300), (400, 400), (530, 345), (1024, 768)), blank=True)),
                ('link', models.URLField(default=b'', null=True, verbose_name='URL', blank=True)),
                ('text', models.TextField(default=b'', verbose_name='Text', blank=True)),
                ('position', models.PositiveSmallIntegerField(default=999, verbose_name='Position')),
                ('content_type', models.ForeignKey(related_name='carousel_item', verbose_name='Content type', blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
