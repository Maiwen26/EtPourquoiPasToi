# Generated by Django 4.0.3 on 2022-04-23 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eppt', '0003_alter_temoignages_creatrice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temoignages',
            old_name='creatrice',
            new_name='utilisateurId',
        ),
    ]
