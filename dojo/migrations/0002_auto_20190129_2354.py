# Generated by Django 2.1.5 on 2019-01-29 14:54

from django.db import migrations, models
import dojo.models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[dojo.models.min_length_3_validator]),
        ),
    ]
