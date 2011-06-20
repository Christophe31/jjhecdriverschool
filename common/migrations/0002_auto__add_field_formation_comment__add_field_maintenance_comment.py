# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Formation.comment'
        db.add_column('common_formation', 'comment', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Maintenance.comment'
        db.add_column('common_maintenance', 'comment', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Formation.comment'
        db.delete_column('common_formation', 'comment')

        # Deleting field 'Maintenance.comment'
        db.delete_column('common_maintenance', 'comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'common.codemark': {
            'Meta': {'ordering': "('date',)", 'object_name': 'CodeMark'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'common.event': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Event'},
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        'common.exam': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Exam', '_ormbases': ['common.Event']},
            'agence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Place']"}),
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['common.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'license': ('django.db.models.fields.IntegerField', [], {}),
            'places': ('django.db.models.fields.IntegerField', [], {}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
        },
        'common.formation': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Formation', '_ormbases': ['common.Event']},
            'agence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Place']", 'null': 'True'}),
            'aptitude': ('django.db.models.fields.IntegerField', [], {}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['common.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Package']", 'null': 'True'}),
            'trainer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Transaction']"}),
            'vehicule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Vehicule']", 'null': 'True'})
        },
        'common.formula': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Formula'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        'common.maintenance': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Maintenance', '_ormbases': ['common.Event']},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['common.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'vehicule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Vehicule']"})
        },
        'common.package': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Package'},
            'formula': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Formula']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'common.place': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Place'},
            'agence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Place']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'road': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'common.transaction': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Transaction'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'transactions_buyed'", 'to': "orm['auth.User']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'formula': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Formula']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'seller': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'transactions_selled'", 'to': "orm['auth.User']"})
        },
        'common.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_code_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Place']", 'null': 'True'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'common.vehicule': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Vehicule'},
            'agence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.Place']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matriculation': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['common']
