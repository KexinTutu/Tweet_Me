# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-04-25 14:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0003_tweet_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Tweet'),
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tweet',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_users', through='tweets.TweetLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
