# Generated by Django 4.0.3 on 2022-04-25 14:06

import WebIStudy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebIStudy', '0007_alter_forum_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=WebIStudy.models.filepath),
        ),
    ]
