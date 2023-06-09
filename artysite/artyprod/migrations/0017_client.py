# Generated by Django 4.2.1 on 2023-05-23 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artyprod', '0016_demandeprojet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=255)),
                ('adresse', models.CharField(default='', max_length=255)),
                ('telephone', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=255)),
                ('Img', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
