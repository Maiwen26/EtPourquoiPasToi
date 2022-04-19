# Generated by Django 4.0.4 on 2022-04-19 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateurs',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('utilisateurId', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('typeUtilisateur', models.CharField(choices=[('Lycéenne ou collégienne', 'Lycéenne ou collégienne'), ('Ingénieure ou étudiante ingénieure', 'Ingénieure ou étudiante ingénieure'), ('Autre utilisateur.e', 'Autre utilisateur.e')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Temoignages',
            fields=[
                ('temoignageId', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=150)),
                ('datePublication', models.DateField(auto_now_add=True)),
                ('domaineEtude', models.CharField(max_length=100)),
                ('typeTemoignage', models.CharField(choices=[('Texte', 'Texte'), ('Audio', 'Audio'), ('Vidéo', 'Vidéo')], max_length=50)),
                ('region', models.CharField(choices=[('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'), ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand Est', 'Grand Est'), ('Hauts-de-France', 'Hauts-de-France'), ('Île-de-France', 'Île-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'), ('Pays de la Loire', 'Pays de la Loire'), ("Provence-Alpes-Côte d'Azur", "Provence-Alpes-Côte d'Azur"), ('Guadeloupe', 'Guadeloupe'), ('Guyane', 'Guyane'), ('Martinique', 'Martinique'), ('La Réunion', 'La Réunion'), ('Mayotte', 'Mayotte')], max_length=50)),
                ('contenu', models.FileField(upload_to='medias/')),
                ('creatrice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Eppt.utilisateurs')),
            ],
        ),
    ]
