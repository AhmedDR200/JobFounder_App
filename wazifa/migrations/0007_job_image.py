# Generated by Django 3.2 on 2023-08-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wazifa', '0006_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
