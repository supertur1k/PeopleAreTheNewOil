# Generated by Django 4.0.4 on 2022-05-03 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='id',
            new_name='worker_id',
        ),
    ]