# Generated by Django 4.0.1 on 2022-02-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='total_target',
            field=models.FloatField(),
        ),
    ]
