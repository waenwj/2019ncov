# Generated by Django 2.2.10 on 2020-02-11 10:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Epidemic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('add_suspect', models.IntegerField(default=0)),
                ('cumulative_suspect', models.IntegerField(default=0)),
                ('new_diagnosis', models.IntegerField(default=0)),
                ('cumulative_diagnosis', models.IntegerField(default=0)),
                ('added_death', models.IntegerField(default=0)),
                ('cumulative_death', models.IntegerField(default=0)),
                ('published_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
    ]
