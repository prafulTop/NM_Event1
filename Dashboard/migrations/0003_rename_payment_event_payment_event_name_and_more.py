# Generated by Django 4.2.9 on 2024-03-08 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_rename_event_payment_payment_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_event',
            new_name='event_name',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='Status',
            new_name='status',
        ),
    ]
