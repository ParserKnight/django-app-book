# Generated by Django 2.0.7 on 2018-07-08 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20180708_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informacion',
            options={'get_latest_by': 'fecha', 'verbose_name_plural': 'informacion'},
        ),
    ]