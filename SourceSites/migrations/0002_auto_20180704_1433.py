# Generated by Django 2.0.7 on 2018-07-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SourceSites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcesite',
            name='website',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
