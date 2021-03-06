# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import markupfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentNickname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=40, unique=True)),
                ('rating', models.SmallIntegerField(default=0)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Component')),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoveComponentSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.PositiveSmallIntegerField(default=0)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Component')),
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Move')),
            ],
        ),
        migrations.CreateModel(
            name='MoveNickname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=40, unique=True)),
                ('rating', models.SmallIntegerField(default=0)),
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Move')),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tips', markupfield.fields.MarkupField(rendered_field=True)),
                ('tips_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown'), ('ReST', 'ReST')], default='markdown', max_length=30)),
                ('_tips_rendered', models.TextField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='VideoAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_type', models.CharField(choices=[('1', 'URL'), ('2', 'Youtube')], default='1', max_length=1)),
                ('URL', models.URLField()),
                ('video_id', models.CharField(max_length=20)),
                ('use_start', models.BooleanField(default=False)),
                ('start_time', models.PositiveSmallIntegerField(default=0)),
                ('use_end', models.BooleanField(default=False)),
                ('end_time', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentDemonstrationVideo',
            fields=[
                ('videoasset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='footbagmoves.VideoAsset')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Component')),
            ],
            bases=('footbagmoves.videoasset',),
        ),
        migrations.CreateModel(
            name='ComponentTips',
            fields=[
                ('tips_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='footbagmoves.Tips')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Component')),
            ],
            bases=('footbagmoves.tips',),
        ),
        migrations.CreateModel(
            name='ComponentTutorialVideo',
            fields=[
                ('videoasset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='footbagmoves.VideoAsset')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Component')),
            ],
            bases=('footbagmoves.videoasset',),
        ),
        migrations.CreateModel(
            name='MoveDemonstrationVideo',
            fields=[
                ('videoasset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='footbagmoves.VideoAsset')),
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Move')),
            ],
            bases=('footbagmoves.videoasset',),
        ),
        migrations.CreateModel(
            name='MoveTips',
            fields=[
                ('tips_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='footbagmoves.Tips')),
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Move')),
            ],
            bases=('footbagmoves.tips',),
        ),
        migrations.CreateModel(
            name='MoveTutorialVideo',
            fields=[
                ('videoasset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='footbagmoves.VideoAsset')),
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footbagmoves.Move')),
            ],
            bases=('footbagmoves.videoasset',),
        ),
    ]
