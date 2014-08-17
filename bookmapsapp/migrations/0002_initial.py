# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Time'
        db.create_table(u'bookmapsapp_time', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'bookmapsapp', ['Time'])

        # Adding model 'Subject'
        db.create_table(u'bookmapsapp_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bookmapsapp', ['Subject'])

        # Adding model 'Author'
        db.create_table(u'bookmapsapp_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'bookmapsapp', ['Author'])

        # Adding model 'Place'
        db.create_table(u'bookmapsapp_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'bookmapsapp', ['Place'])

        # Adding model 'Book'
        db.create_table(u'bookmapsapp_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookmapsapp.Author'])),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookmapsapp.Place'], null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'bookmapsapp', ['Book'])

        # Adding M2M table for field time on 'Book'
        m2m_table_name = db.shorten_name(u'bookmapsapp_book_time')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'bookmapsapp.book'], null=False)),
            ('time', models.ForeignKey(orm[u'bookmapsapp.time'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'time_id'])

        # Adding M2M table for field subject on 'Book'
        m2m_table_name = db.shorten_name(u'bookmapsapp_book_subject')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'bookmapsapp.book'], null=False)),
            ('subject', models.ForeignKey(orm[u'bookmapsapp.subject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'subject_id'])


    def backwards(self, orm):
        # Deleting model 'Time'
        db.delete_table(u'bookmapsapp_time')

        # Deleting model 'Subject'
        db.delete_table(u'bookmapsapp_subject')

        # Deleting model 'Author'
        db.delete_table(u'bookmapsapp_author')

        # Deleting model 'Place'
        db.delete_table(u'bookmapsapp_place')

        # Deleting model 'Book'
        db.delete_table(u'bookmapsapp_book')

        # Removing M2M table for field time on 'Book'
        db.delete_table(db.shorten_name(u'bookmapsapp_book_time'))

        # Removing M2M table for field subject on 'Book'
        db.delete_table(db.shorten_name(u'bookmapsapp_book_subject'))


    models = {
        u'bookmapsapp.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'bookmapsapp.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookmapsapp.Author']"}),
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