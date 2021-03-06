# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import django_revision.revision_field
import edc_base.model.fields.hostname_modification_field
import edc_base.model.fields.userfield
import edc_base.model.fields.uuid_auto_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model.fields.uuid_auto_field.UUIDAutoField(editable=False, help_text='System field. UUID primary key.', primary_key=True, serialize=False)),
                ('notification_plan_name', models.CharField(max_length=200)),
                ('notification_datetime', models.DateTimeField()),
                ('subject', models.CharField(max_length=200)),
                ('recipient_list', models.TextField(null=True)),
                ('cc_list', models.TextField(null=True)),
                ('body', models.TextField(null=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('sent', 'Sent'), ('cancelled', 'Cancelled')], default='new', max_length=15)),
                ('sent', models.BooleanField(default=False)),
                ('sent_datetime', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ('notification_datetime',),
            },
        ),
        migrations.CreateModel(
            name='NotificationPlan',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='One-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model.fields.uuid_auto_field.UUIDAutoField(editable=False, help_text='System field. UUID primary key.', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('friendly_name', models.CharField(max_length=50)),
                ('subject_format', models.TextField()),
                ('body_format', models.TextField()),
                ('recipient_list', models.TextField()),
                ('cc_list', models.TextField()),
            ],
        ),
    ]
