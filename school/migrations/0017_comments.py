# Generated by Django 5.0.6 on 2024-09-20 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_alter_attendance_classid_alter_attendance_studentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False)),
                ('comment_text', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
    ]
