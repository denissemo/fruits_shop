# Generated by Django 3.0.5 on 2020-05-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200502_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
