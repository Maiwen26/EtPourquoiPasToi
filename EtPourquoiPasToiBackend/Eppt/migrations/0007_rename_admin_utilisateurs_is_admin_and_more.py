# Generated by Django 4.0.3 on 2022-04-24 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eppt', '0006_utilisateurs_admin_utilisateurs_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateurs',
            old_name='admin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='utilisateurs',
            old_name='staff',
            new_name='is_staff',
        ),
    ]
