# Generated by Django 3.0.5 on 2020-04-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]
