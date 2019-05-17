# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-31 06:32
from __future__ import unicode_literals

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objects', '0005_auto_20150403_2339'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xp_earned', models.SmallIntegerField(blank=0, default=0)),
                ('gm_notes', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('rating', models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'Value required to get this clue')),
                ('desc', models.TextField(blank=True, help_text=b'Description of the clue given to the player', verbose_name=b'Description')),
                ('red_herring', models.BooleanField(default=False, help_text=b'Whether this revelation is totally fake')),
                ('allow_investigation', models.BooleanField(default=False, help_text=b'Can be gained through investigation rolls')),
                ('allow_exploration', models.BooleanField(default=False, help_text=b'Can be gained through exploration rolls')),
                ('allow_trauma', models.BooleanField(default=False, help_text=b'Can be gained through combat rolls')),
                ('investigation_tags', models.TextField(blank=True, help_text=b'List keywords separated by semicolons for investigation', verbose_name=b'Keywords for investigation')),
            ],
        ),
        migrations.CreateModel(
            name='ClueDiscovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, help_text=b"Message for the player's records about how they discovered this.")),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('discovery_method', models.CharField(help_text=b'How this was discovered - exploration, trauma, etc', max_length=255)),
                ('roll', models.PositiveSmallIntegerField(blank=0, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ClueForRevelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_for_revelation', models.BooleanField(default=True, help_text=b'Whether this must be discovered for the revelation to finish')),
                ('tier', models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'How high in the hierarchy of discoveries this clue is, lower number discovered first')),
                ('clue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='character.Clue')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('gamedate', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('gm_notes', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='episodes', to='character.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ongoing', models.BooleanField(default=True, help_text=b'Whether this investigation is finished or not')),
                ('active', models.BooleanField(default=False, help_text=b'Whether this is the investigation for the week. Only one allowed')),
                ('automate_result', models.BooleanField(default=True, help_text=b"Whether to generate a result during weekly maintenance. Set false if GM'd")),
                ('results', models.TextField(blank=True, default=b"You didn't find anything.", help_text=b'The text to send the player, either set by GM or generated automatically by script if automate_result is set.')),
                ('actions', models.TextField(blank=True, help_text=b'The writeup the player submits of their actions, used for GMing.')),
                ('topic', models.CharField(blank=True, help_text=b'Keyword to try to search for clues against', max_length=255)),
                ('stat_used', models.CharField(blank=True, default=b'perception', help_text=b'The stat the player chose to use', max_length=80)),
                ('skill_used', models.CharField(blank=True, default=b'investigation', help_text=b'The skill the player chose to use', max_length=80)),
                ('silver', models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'Additional silver added by the player')),
                ('economic', models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'Additional economic resources added by the player')),
                ('military', models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'Additional military resources added by the player')),
                ('social', models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'Additional social resources added by the player')),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('secret', models.BooleanField(default=False)),
                ('gm_notes', models.TextField(blank=True, null=True)),
                ('importance', models.PositiveSmallIntegerField(blank=0, default=0)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='milestones', to='character.Chapter')),
                ('episode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='milestones', to='character.Episode')),
            ],
        ),
        migrations.CreateModel(
            name='Mystery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True, help_text=b'Description of the mystery given to the player when fully revealed', verbose_name=b'Description')),
                ('category', models.CharField(blank=True, help_text=b'Type of mystery this is - ability-related, metaplot, etc', max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Mysteries',
            },
        ),
        migrations.CreateModel(
            name='MysteryDiscovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, help_text=b"Message for the player's records about how they discovered this.")),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xp_earned', models.PositiveSmallIntegerField(blank=0, default=0)),
                ('karma_earned', models.PositiveSmallIntegerField(blank=0, default=0)),
                ('gm_notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=200, verbose_name=b'Name or description of the picture (optional)')),
                ('alt_text', models.CharField(blank=True, max_length=200, verbose_name=b"Optional 'alt' text when mousing over your image")),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'image')),
                ('owner', models.ForeignKey(blank=True, help_text=b'a Character owner of this image, if any.', null=True, on_delete=django.db.models.deletion.CASCADE, to='objects.ObjectDB', verbose_name=b'owner')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('karma', models.PositiveSmallIntegerField(blank=0, default=0)),
                ('gm_notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Revelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('desc', models.TextField(blank=True, help_text=b'Description of the revelation given to the player', verbose_name=b'Description')),
                ('required_clue_value', models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'The total value of clues to trigger this')),
                ('red_herring', models.BooleanField(default=False, help_text=b'Whether this revelation is totally fake')),
            ],
        ),
        migrations.CreateModel(
            name='RevelationDiscovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, help_text=b"Message for the player's records about how they discovered this.")),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('discovery_method', models.CharField(help_text=b'How this was discovered - exploration, trauma, etc', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RevelationForMystery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_for_mystery', models.BooleanField(default=True, help_text=b'Whether this must be discovered for the mystery to finish')),
                ('tier', models.PositiveSmallIntegerField(blank=0, default=0, help_text=b'How high in the hierarchy of discoveries this revelation is, lower number discovered first')),
                ('mystery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revelations_used', to='character.Mystery')),
                ('revelation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='character.Revelation')),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('lock_storage', models.TextField(blank=True, help_text=b'defined in setup_utils', verbose_name=b'locks')),
            ],
        ),
        migrations.CreateModel(
            name='RosterEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gm_notes', models.TextField(blank=True)),
                ('inactive', models.BooleanField(default=False)),
                ('frozen', models.BooleanField(default=False)),
                ('sheet_style', models.TextField(blank=True)),
                ('lock_storage', models.TextField(blank=True, help_text=b'defined in setup_utils', verbose_name=b'locks')),
                ('character', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roster', to='objects.ObjectDB')),
                ('current_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characters', to='character.PlayerAccount')),
                ('player', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roster', to=settings.AUTH_USER_MODEL)),
                ('previous_accounts', models.ManyToManyField(blank=True, through='character.AccountHistory', to='character.PlayerAccount')),
                ('profile_picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='character.Photo')),
                ('roster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entries', to='character.Roster')),
            ],
            options={
                'verbose_name_plural': 'Roster Entries',
            },
        ),
        migrations.CreateModel(
            name='RPScene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name=b'title of the scene')),
                ('synopsis', models.TextField(verbose_name=b'Description of the scene written by player')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('log', models.TextField(verbose_name=b'Text log of the scene')),
                ('lock_storage', models.TextField(blank=True, help_text=b'defined in setup_utils', verbose_name=b'locks')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='character.RosterEntry')),
                ('milestone', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log', to='character.Milestone')),
            ],
            options={
                'verbose_name_plural': 'RP Scenes',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('season', models.PositiveSmallIntegerField(blank=0, default=0)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('current_chapter', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_chapter_story', to='character.Chapter')),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
        ),
        migrations.CreateModel(
            name='StoryEmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emits', to='character.Chapter')),
                ('episode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emits', to='character.Episode')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='revelationdiscovery',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revelations', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='revelationdiscovery',
            name='investigation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revelations', to='character.Investigation'),
        ),
        migrations.AddField(
            model_name='revelationdiscovery',
            name='milestone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revelation', to='character.Milestone'),
        ),
        migrations.AddField(
            model_name='revelationdiscovery',
            name='revealed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revelations_spoiled', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='revelationdiscovery',
            name='revelation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discoveries', to='character.Revelation'),
        ),
        migrations.AddField(
            model_name='revelation',
            name='characters',
            field=models.ManyToManyField(blank=True, through='character.RevelationDiscovery', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='revelation',
            name='mysteries',
            field=models.ManyToManyField(through='character.RevelationForMystery', to='character.Mystery'),
        ),
        migrations.AddField(
            model_name='participant',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='participant',
            name='milestone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.Milestone'),
        ),
        migrations.AddField(
            model_name='mysterydiscovery',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mysteries', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='mysterydiscovery',
            name='investigation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mysteries', to='character.Investigation'),
        ),
        migrations.AddField(
            model_name='mysterydiscovery',
            name='milestone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mystery', to='character.Milestone'),
        ),
        migrations.AddField(
            model_name='mysterydiscovery',
            name='mystery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discoveries', to='character.Mystery'),
        ),
        migrations.AddField(
            model_name='mystery',
            name='characters',
            field=models.ManyToManyField(blank=True, through='character.MysteryDiscovery', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='milestones', to='character.Photo'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='participants',
            field=models.ManyToManyField(blank=True, through='character.Participant', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='protagonist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milestones', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='investigation',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investigations', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='investigation',
            name='clue_target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character.Clue'),
        ),
        migrations.AddField(
            model_name='comment',
            name='milestone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='character.Milestone'),
        ),
        migrations.AddField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_upon', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='clueforrevelation',
            name='revelation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clues_used', to='character.Revelation'),
        ),
        migrations.AddField(
            model_name='cluediscovery',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clues', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='cluediscovery',
            name='clue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discoveries', to='character.Clue'),
        ),
        migrations.AddField(
            model_name='cluediscovery',
            name='investigation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clues', to='character.Investigation'),
        ),
        migrations.AddField(
            model_name='cluediscovery',
            name='milestone',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clue', to='character.Milestone'),
        ),
        migrations.AddField(
            model_name='cluediscovery',
            name='revealed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clues_spoiled', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='clue',
            name='characters',
            field=models.ManyToManyField(blank=True, through='character.ClueDiscovery', to='character.RosterEntry'),
        ),
        migrations.AddField(
            model_name='clue',
            name='revelations',
            field=models.ManyToManyField(through='character.ClueForRevelation', to='character.Revelation'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_chapters', to='character.Story'),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.PlayerAccount'),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.RosterEntry'),
        ),
    ]