# Generated by Django 3.1.3 on 2021-06-27 09:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0004_auto_20210425_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={},
        ),
        migrations.AlterIndexTogether(
            name='tweet',
            index_together={('user', 'created_at')},
        ),
    ]
