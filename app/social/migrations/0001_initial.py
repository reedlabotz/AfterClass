# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table('social_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('course_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('professor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('social', ['Course'])

        # Adding model 'UserProfile'
        db.create_table('social_userprofile', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('person_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('learning_style', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('interest', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('monday_availability', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('tuesday_availability', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('wednesday_availability', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('thursday_availability', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('friday_availability', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('saturday_availability', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('sunday_availability', self.gf('django.db.models.fields.CharField')(max_length=48)),
        ))
        db.send_create_signal('social', ['UserProfile'])

        # Adding model 'UserCourse'
        db.create_table('social_usercourse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.UserProfile'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.Course'])),
            ('general_experience', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('general_level', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('topic_experience', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('topic_level', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('years_experience', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('goals', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('social', ['UserCourse'])

        # Adding unique constraint on 'UserCourse', fields ['user', 'course']
        db.create_unique('social_usercourse', ['user_id', 'course_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserCourse', fields ['user', 'course']
        db.delete_unique('social_usercourse', ['user_id', 'course_id'])

        # Deleting model 'Course'
        db.delete_table('social_course')

        # Deleting model 'UserProfile'
        db.delete_table('social_userprofile')

        # Deleting model 'UserCourse'
        db.delete_table('social_usercourse')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'social.course': {
            'Meta': {'ordering': "['service', 'name']", 'object_name': 'Course'},
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'social.usercourse': {
            'Meta': {'unique_together': "(('user', 'course'),)", 'object_name': 'UserCourse'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social.Course']"}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'general_experience': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'general_level': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'goals': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'topic_experience': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'topic_level': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social.UserProfile']"}),
            'years_experience': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'social.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['social.Course']", 'through': "orm['social.UserCourse']", 'symmetrical': 'False'}),
            'friday_availability': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'interest': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'learning_style': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'monday_availability': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'person_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'saturday_availability': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'sunday_availability': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'thursday_availability': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'tuesday_availability': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'wednesday_availability': ('django.db.models.fields.CharField', [], {'max_length': '48'})
        }
    }

    complete_apps = ['social']