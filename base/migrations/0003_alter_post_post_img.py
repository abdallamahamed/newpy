# Generated by Django 4.2.1 on 2023-06-29 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_postcategory_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(upload_to='static/post'),
        ),
    ]
