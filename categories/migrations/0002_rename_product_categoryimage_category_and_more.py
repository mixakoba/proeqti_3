# Generated by Django 5.1.6 on 2025-02-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryimage',
            old_name='product',
            new_name='category',
        ),
        migrations.AddField(
            model_name='categoryimage',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
