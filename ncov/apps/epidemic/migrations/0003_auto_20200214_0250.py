# Generated by Django 2.2.10 on 2020-02-14 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("epidemic", "0002_auto_20200211_2109")]

    operations = [
        migrations.AlterModelOptions(
            name="epidemic",
            options={
                "ordering": ["-published_at", "-cumulative_diagnosis", "-new_diagnosis"]
            },
        )
    ]
