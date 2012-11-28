# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Circle'
        db.create_table('social_circle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.Course'])),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('social', ['Circle'])

        # Adding model 'CircleSuggestion'
        db.create_table('social_circlesuggestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.Course'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('social', ['CircleSuggestion'])

        # Adding M2M table for field users on 'CircleSuggestion'
        db.create_table('social_circlesuggestion_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('circlesuggestion', models.ForeignKey(orm['social.circlesuggestion'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('social_circlesuggestion_users', ['circlesuggestion_id', 'user_id'])

        # Adding M2M table for field confirmed on 'CircleSuggestion'
        db.create_table('social_circlesuggestion_confirmed', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('circlesuggestion', models.ForeignKey(orm['social.circlesuggestion'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('social_circlesuggestion_confirmed', ['circlesuggestion_id', 'user_id'])

        # Adding model 'CircleRequest'
        db.create_table('social_circlerequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('circle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.Circle'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requester', to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('social', ['CircleRequest'])

        # Adding M2M table for field confirmed on 'CircleRequest'
        db.create_table('social_circlerequest_confirmed', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('circlerequest', models.ForeignKey(orm['social.circlerequest'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('social_circlerequest_confirmed', ['circlerequest_id', 'user_id'])

        # Adding model 'CircleUser'
        db.create_table('social_circleuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('circle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.Circle'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('joined', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('social', ['CircleUser'])


    def backwards(self, orm):
        # Deleting model 'Circle'
        db.delete_table('social_circle')

        # Deleting model 'CircleSuggestion'
        db.delete_table('social_circlesuggestion')

        # Removing M2M table for field users on 'CircleSuggestion'
        db.delete_table('social_circlesuggestion_users')

        # Removing M2M table for field confirmed on 'CircleSuggestion'
        db.delete_table('social_circlesuggestion_confirmed')

        # Deleting model 'CircleRequest'
        db.delete_table('social_circlerequest')

        # Removing M2M table for field confirmed on 'CircleRequest'
        db.delete_table('social_circlerequest_confirmed')

        # Deleting model 'CircleUser'
        db.delete_table('social_circleuser')


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
        'social.circle': {
            'Meta': {'object_name': 'Circle'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'requests': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'request'", 'symmetrical': 'False', 'through': "orm['social.CircleRequest']", 'to': "orm['auth.User']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['social.CircleUser']", 'symmetrical': 'False'})
        },
        'social.circlerequest': {
            'Meta': {'object_name': 'CircleRequest'},
            'circle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social.Circle']"}),
            'confirmed': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requester'", 'to': "orm['auth.User']"})
        },
        'social.circlesuggestion': {
            'Meta': {'object_name': 'CircleSuggestion'},
            'confirmed': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'confirmer'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social.Course']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
        },
        'social.circleuser': {
            'Meta': {'object_name': 'CircleUser'},
            'circle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social.Circle']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joined': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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