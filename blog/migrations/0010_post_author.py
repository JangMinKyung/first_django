# Generated by Django 2.1.5 on 2019-01-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190126_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
    ]
