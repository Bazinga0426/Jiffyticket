# Generated by Django 2.2.7 on 2019-11-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='counts',
            new_name='adult_counts',
        ),
        migrations.AddField(
            model_name='order',
            name='child_counts',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='student_counts',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
