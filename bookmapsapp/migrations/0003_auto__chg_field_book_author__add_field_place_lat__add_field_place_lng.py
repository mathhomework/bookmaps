# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Book.author'
        db.alter_column(u'bookmapsapp_book', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookmapsapp.Author'], null=True))
        # Adding field 'Place.lat'
        db.add_column(u'bookmapsapp_place', 'lat',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Place.lng'
        db.add_column(u'bookmapsapp_place', 'lng',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Book.author'
        db.alter_column(u'bookmapsapp_book', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['bookmapsapp.Author']))
        # Deleting field 'Place.lat'
        db.delete_column(u'bookmapsapp_place', 'lat')

        # Deleting field 'Place.lng'
        db.delete_column(u'bookmapsapp_place', 'lng')


    models = {
        u'bookmapsapp.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'bookmapsapp.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookmapsapp.Author']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookmapsapp.Place']", 'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'books'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['bookmapsapp.Subject']"}),
            'time': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'books'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['bookmapsapp.Time']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'bookmapsapp.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'bookmapsapp.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bookmapsapp.time': {
            'Meta': {'object_name': 'Time'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['bookmapsapp']