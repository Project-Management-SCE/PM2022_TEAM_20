# Generated by Django 4.0.3 on 2022-05-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebIStudy', '0004_reports'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='report',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
