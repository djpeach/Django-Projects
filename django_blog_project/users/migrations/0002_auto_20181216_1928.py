# Generated by Django 2.1.4 on 2018-12-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile-pics/default.png', upload_to='profile-pics'),
        ),
    ]
