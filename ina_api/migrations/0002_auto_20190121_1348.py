# Generated by Django 2.0.5 on 2019-01-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ina_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='function',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='organisation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo_path',
            field=models.CharField(max_length=200),
        ),
    ]