# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.bio'
        db.add_column('social_userprofile', 'bio',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserProfile.bio'
        db.delete_column('social_userprofile', 'bio')


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
        'social.circleaction': {
            'Meta': {'object_name': 'CircleAction'},
            'circle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social.Circle']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['social.Course']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partner_request_owner'", 'to': "orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partner_request_user'", 'to': "orm['auth.User']"})
        },
        'social.partnersuggest': {
            'Meta': {'object_name': 'PartnerSuggest'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['social.Course']"}),
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
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
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