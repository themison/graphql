# Generated by Django 2.1.2 on 2018-10-17 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20181015_1606'),
    ]

    operations = [
        migrations.RenameField(model_name='pizza', old_name='secretKey', new_name='secret_key')
    ]