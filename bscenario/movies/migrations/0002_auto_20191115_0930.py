# Generated by Django 2.2.7 on 2019-11-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='desp',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
