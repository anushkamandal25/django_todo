# Generated by Django 4.0.3 on 2022-08-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='email', max_length=254),
        ),
    ]
