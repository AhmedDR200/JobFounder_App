# Generated by Django 3.2 on 2023-07-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wazifa', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
