# Generated by Django 5.0.6 on 2024-09-18 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_student_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='students_new',
        ),
    ]
