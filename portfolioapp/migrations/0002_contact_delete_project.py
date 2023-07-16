# Generated by Django 4.2.3 on 2023-07-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='project',
        ),
    ]
