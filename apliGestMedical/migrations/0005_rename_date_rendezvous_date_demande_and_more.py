# Generated by Django 5.0.3 on 2024-03-06 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apliGestMedical', '0004_rendezvous_documentjustificatif'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rendezvous',
            old_name='date',
            new_name='date_demande',
        ),
        migrations.RenameField(
            model_name='rendezvous',
            old_name='marital_status',
            new_name='situation_Matrimoniale',
        ),
        migrations.RenameField(
            model_name='rendezvous',
            old_name='type_consultation',
            new_name='type_personne',
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='adresse',
            field=models.CharField(max_length=100),
        ),
    ]
