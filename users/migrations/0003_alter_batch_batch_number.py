# Generated by Django 4.2.4 on 2023-08-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_user_alter_user_batch_alter_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_number',
            field=models.IntegerField(blank=True, max_length=7, null=True, unique=True),
        ),
    ]