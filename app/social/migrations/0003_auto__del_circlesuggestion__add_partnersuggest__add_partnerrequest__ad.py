# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CircleSuggestion'
        db.delete_table('social_circlesuggestion')

        # Removing M2M table for field confirmed on 'CircleSuggestion'
        db.delete_table('social_circlesuggestion_confirmed')

        # Removing M2M table for field users on 'CircleSuggestion'
        db.delete_table('social_circlesuggestion_users')

        # Adding model 'PartnerSuggest'
        db.create_table('social_partnersuggest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='partner_suggest_owner', to=orm['auth.User'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='partner_suggest_user', to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('social', ['PartnerSuggest'])

        # Adding model 'PartnerRequest'
        db.create_table('social_partnerrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='partner_request_owner', to=orm['auth.User'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='partner_request_user', to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('social', ['PartnerRequest'])

        # Adding model 'CircleSuggest'
        db.create_table('social_circlesuggest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='circle_suggest_owner', to=orm['auth.User'])),
            ('circle', self.gf('django.db.models.fields.related.ForeignKey')(related_name='circle_suggest_circle', to=orm['social.Circle'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('social', ['CircleSuggest'])


        # Changing field 'UserCourse.user'
        db.alter_column('social_usercourse', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))
        # Deleting field 'CircleRequest.user'
        db.delete_column('social_circlerequest', 'user_id')

        # Adding field 'CircleRequest.owner'
        db.add_column('social_circlerequest', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='circle_request_owner', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'CircleRequest.deleted'
        db.add_column('social_circlerequest', 'deleted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'CircleSuggestion'
        db.create_table('social_circlesuggestion', (
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.Course'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('social', ['CircleSuggestion'])

        # Adding M2M table for field confirmed on 'CircleSuggestion'
        db.create_table('social_circlesuggestion_confirmed', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('circlesuggestion', models.ForeignKey(orm['social.circlesuggestion'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('social_circlesuggestion_confirmed', ['circlesuggestion_id', 'user_id'])

        # Adding M2M table for field users on 'CircleSuggestion'
        db.create_table('social_circlesuggestion_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('circlesuggestion', models.ForeignKey(orm['social.circlesuggestion'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('social_circlesuggestion_users', ['circlesuggestion_id', 'user_id'])

        # Deleting model 'PartnerSuggest'
        db.delete_table('social_partnersuggest')

        # Deleting model 'PartnerRequest'
        db.delete_table('social_partnerrequest')

        # Deleting model 'CircleSuggest'
        db.delete_table('social_circlesuggest')


        # Changing field 'UserCourse.user'
        db.alter_column('social_usercourse', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social.UserProfile']))
        # Adding field 'CircleRequest.user'
        db.add_column('social_circlerequest', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='requester', to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'CircleRequest.owner'
        db.delete_column('social_circlerequest', 'owner_id')

        # Deleting field 'CircleRequest.deleted'
        db.delete_column('social_circlerequest', 'deleted')


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
            'requests': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'circle_request'", 'symmetrical': 'False', 'through': "orm['social.CircleRequest']", 'to': "orm['auth.User']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['social.CircleUser']", 'symmetrical': 'False'})
        },
        'social.circlerequest': {
            'Meta': {'object_name': 'CircleRequest'},
            'circle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social.Circle']"}),
            'confirmed': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'circle_request_confirmer'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'circle_request_owner'", 'to': "orm['auth.User']"})
        },
        'social.circlesuggest': {
            'Meta': {'object_name': 'CircleSuggest'},
            'circle': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'circle_suggest_circle'", 'to': "orm['social.Circle']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'circle_suggest_owner'", 'to': "orm['auth.User']"})
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
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['social.UserCourse']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'social.partnerrequest': {
            'Meta': {'object_name': 'PartnerRequest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partner_request_owner'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partner_request_user'", 'to': "orm['auth.User']"})
        },
        'social.partnersuggest': {
            'Meta': {'object_name': 'PartnerSuggest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partner_suggest_owner'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partner_suggest_user'", 'to': "orm['auth.User']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'years_experience': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'social.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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