# Generated by Django 4.2.10 on 2024-02-25 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_todo_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]