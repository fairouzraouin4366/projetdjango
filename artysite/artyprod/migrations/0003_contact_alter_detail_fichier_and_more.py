# Generated by Django 4.2.1 on 2023-05-16 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0002_projetrealise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='detail',
            name='fichier',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='fichier_cv',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='fichier_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='projetrealise',
            name='photoPrj',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]