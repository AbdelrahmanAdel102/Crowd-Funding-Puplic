# Generated by Django 4.0.1 on 2022-02-19 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_delete_projectimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
