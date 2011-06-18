# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Place'
        db.create_table('common_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('road', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('agence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Place'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('common', ['Place'])

        # Adding model 'UserProfile'
        db.create_table('common_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('last_code_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('adress', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('postal_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Place'], null=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('common', ['UserProfile'])

        # Adding model 'Formula'
        db.create_table('common_formula', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('common', ['Formula'])

        # Adding model 'Transaction'
        db.create_table('common_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'transactions_buyed', to=orm['auth.User'])),
            ('seller', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'transactions_selled', to=orm['auth.User'])),
            ('formula', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Formula'])),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('common', ['Transaction'])

        # Adding model 'Package'
        db.create_table('common_package', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('formula', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Formula'])),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('common', ['Package'])

        # Adding model 'Vehicule'
        db.create_table('common_vehicule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('matriculation', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('agence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Place'])),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('common', ['Vehicule'])

        # Adding model 'Event'
        db.create_table('common_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('common', ['Event'])

        # Adding model 'Maintenance'
        db.create_table('common_maintenance', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['common.Event'], unique=True, primary_key=True)),
            ('vehicule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Vehicule'])),
        ))
        db.send_create_signal('common', ['Maintenance'])

        # Adding model 'CodeMark'
        db.create_table('common_codemark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mark', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('common', ['CodeMark'])

        # Adding model 'Formation'
        db.create_table('common_formation', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['common.Event'], unique=True, primary_key=True)),
            ('agence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Place'], null=True)),
            ('vehicule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Vehicule'], null=True)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Package'], null=True)),
            ('aptitude', self.gf('django.db.models.fields.IntegerField')()),
            ('trainer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Transaction'])),
        ))
        db.send_create_signal('common', ['Formation'])

        # Adding model 'Exam'
        db.create_table('common_exam', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['common.Event'], unique=True, primary_key=True)),
            ('agence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Place'])),
            ('places', self.gf('django.db.models.fields.IntegerField')()),
            ('license', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('common', ['Exam'])

        # Adding M2M table for field subscribers on 'Exam'
        db.create_table('common_exam_subscribers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exam', models.ForeignKey(orm['common.exam'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('common_exam_subscribers', ['exam_id', 'user_id'])


    def backwards(self, orm):
        
        # Deleting model 'Place'
        db.delete_table('common_place')

        # Deleting model 'UserProfile'
        db.delete_table('common_userprofile')

        # Deleting model 'Formula'
        db.delete_table('common_formula')

        # Deleting model 'Transaction'
        db.delete_table('common_transaction')

        # Deleting model 'Package'
        db.delete_table('common_package')

        # Deleting model 'Vehicule'
        db.delete_table('common_vehicule')

        # Deleting model 'Event'
        db.delete_table('common_event')

        # Deleting model 'Maintenance'
        db.delete_table('common_maintenance')

        # Deleting model 'CodeMark'
        db.delete_table('common_codemark')

        # Deleting model 'Formation'
        db.delete_table('common_formation')

        # Deleting model 'Exam'
        db.delete_table('common_exam')

        # Removing M2M table for field subscribers on 'Exam'
        db.delete_table('common_exam_subscribers')


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
