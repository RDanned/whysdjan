# Generated by Django 4.1.3 on 2022-11-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
