# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CarouselItem'
        db.create_table('lfs_carousel_carouselitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='carousel_item', null=True, to=orm['contenttypes.ContentType'])),
            ('content_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('image', self.gf('lfs.core.fields.thumbs.ImageWithThumbsField')(blank=True, max_length=100, null=True, sizes=((60, 60), (100, 100), (200, 200), (300, 300), (400, 400)))),
            ('link', self.gf('django.db.models.fields.URLField')(default='', max_length=200, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=999)),
        ))
        db.send_create_signal('lfs_carousel', ['CarouselItem'])


    def backwards(self, orm):
        
        # Deleting model 'CarouselItem'
        db.delete_table('lfs_carousel_carouselitem')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lfs_carousel.carouselitem': {
            'Meta': {'ordering': "('position',)", 'object_name': 'CarouselItem'},
            'content_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'carousel_item'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('lfs.core.fields.thumbs.ImageWithThumbsField', [], {'blank': 'True', 'max_length': '100', 'null': 'True', 'sizes': '((60, 60), (100, 100), (200, 200), (300, 300), (400, 400))'}),
            'link': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '999'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['lfs_carousel']
