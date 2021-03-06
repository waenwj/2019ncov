# Generated by Django 2.2.10 on 2020-02-18 09:17

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.RandomCharField(blank=True, db_index=True, editable=False, include_alpha=False, length=12, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('crawlSource', models.CharField(max_length=255)),
                ('majorClassification', models.CharField(max_length=255)),
                ('metaInfoName', models.CharField(max_length=255)),
                ('webpageCode', models.CharField(max_length=32, unique=True)),
                ('webpageUrl', models.URLField(blank=True, default='', max_length=255)),
                ('releaseTime', models.DateTimeField(db_index=True)),
            ],
        ),
    ]
