# Generated by Django 4.2.1 on 2023-05-23 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0022_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imgblog',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]