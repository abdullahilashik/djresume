# Generated by Django 4.0.3 on 2022-03-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djresume', '0003_userprofile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]