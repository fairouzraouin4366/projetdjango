# Generated by Django 4.2.1 on 2023-05-20 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0009_projetrealise_date_realisation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='fichier_cv',
            new_name='cvprs',
        ),
        migrations.RenameField(
            model_name='personnel',
            old_name='fichier_photo',
            new_name='photoprs',
        ),
    ]