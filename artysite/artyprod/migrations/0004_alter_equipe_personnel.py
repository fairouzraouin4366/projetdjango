# Generated by Django 4.2.1 on 2023-05-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0003_contact_alter_detail_fichier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='personnel',
            field=models.ManyToManyField(related_name='equipes', to='artyprod.personnel'),
        ),
    ]