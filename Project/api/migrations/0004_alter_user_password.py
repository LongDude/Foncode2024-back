# Generated by Django 5.0.3 on 2024-03-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]