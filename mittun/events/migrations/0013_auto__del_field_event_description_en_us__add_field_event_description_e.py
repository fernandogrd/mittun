# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.description_en'
        db.delete_column('events_event', 'description_en')

        # Adding field 'Event.description_en'
        db.add_column('events_event', 'description_en', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True), keep_default=False)

        # Changing field 'Event.description_pt_br'
        db.alter_column('events_event', 'description_pt_br', self.gf('django.db.models.fields.TextField')(default='', max_length=200))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Event.description_en'
        raise RuntimeError("Cannot reverse this migration. 'Event.description_en' and its values cannot be restored.")

        # Deleting field 'Event.description_en'
        db.delete_column('events_event', 'description_en')

        # Changing field 'Event.description_pt_br'
        db.alter_column('events_event', 'description_pt_br', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'description_en': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description_pt_br': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'events.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['events']
