# Generated by Django 4.2.2 on 2023-07-04 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_attendance_roll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='name',
            new_name='student',
        ),
    ]
