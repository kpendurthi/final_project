# Generated by Django 3.0.5 on 2020-04-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image_url',
            field=models.TextField(default='https://www.mydrdental.com/wp-content/uploads/2017/12/Prinicpal_Financial_Group.jpg'),
        ),
    ]
