# Generated by Django 4.2.9 on 2024-03-08 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='event',
            new_name='payment_event',
        ),
    ]
