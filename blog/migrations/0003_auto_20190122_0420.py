# Generated by Django 2.1.5 on 2019-01-21 19:20

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190122_0155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='경도/위도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
    ]
