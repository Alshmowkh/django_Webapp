# Generated by Django 5.1.2 on 2024-11-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_temp', '0004_alter_student_student_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_img',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
