# Generated by Django 3.0.7 on 2020-07-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default='this is desc', max_length=1000),
            preserve_default=False,
        ),
    ]
