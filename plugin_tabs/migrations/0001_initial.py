# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TabsList'
        db.create_table('cmsplugin_tabslist', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('plantilla', self.gf('django.db.models.fields.CharField')(default='plugin_tabs/tabs.html', max_length=255)),
        ))
        db.send_create_signal('plugin_tabs', ['TabsList'])

        # Adding model 'Tab'
        db.create_table('plugin_tabs_tab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plugin', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tabs', to=orm['plugin_tabs.TabsList'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contenido', self.gf('django.db.models.fields.TextField')(null=True)),
            ('orden', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
        ))
        db.send_create_signal('plugin_tabs', ['Tab'])


    def backwards(self, orm):
        # Deleting model 'TabsList'
        db.delete_table('cmsplugin_tabslist')

        # Deleting model 'Tab'
        db.delete_table('plugin_tabs_tab')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'plugin_tabs.tab': {
            'Meta': {'ordering': "['orden']", 'object_name': 'Tab'},
            'contenido': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'plugin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tabs'", 'to': "orm['plugin_tabs.TabsList']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'plugin_tabs.tabslist': {
            'Meta': {'object_name': 'TabsList', 'db_table': "'cmsplugin_tabslist'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'plantilla': ('django.db.models.fields.CharField', [], {'default': "'plugin_tabs/tabs.html'", 'max_length': '255'})
        }
    }

    complete_apps = ['plugin_tabs']