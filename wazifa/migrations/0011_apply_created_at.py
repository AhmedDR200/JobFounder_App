# Generated by Django 3.2 on 2023-08-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wazifa', '0010_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
