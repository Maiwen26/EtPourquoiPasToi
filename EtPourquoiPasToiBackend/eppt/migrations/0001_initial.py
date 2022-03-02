# Generated by Django 4.0.3 on 2022-03-02 13:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temoignage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titreTemoignage', models.CharField(help_text='Entrez le nom de votre témoignage', max_length=20, unique=True)),
                ('typeTemoignage', models.CharField(choices=[('V', 'video'), ('A', 'audio'), ('T', 'texte')], max_length=1)),
                ('datePublication', models.DateField(default=datetime.datetime(2022, 3, 2, 13, 32, 50, 371174, tzinfo=utc))),
                ('contenu', models.FileField(upload_to='')),
                ('region', models.CharField(choices=[('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'), ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand Est', 'Grand Est'), ('Hauts-de-France', 'Hauts-de-France'), ('Île-de-France', 'Île-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'), ('Pays de la Loire', 'Pays de la Loire'), ("Provence-Alpes-Côte d'Azur", "Provence-Alpes-Côte d'Azur")], max_length=30)),
                ('domaineEtude', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['datePublication', '-titreTemoignage'],
            },
        ),
    ]