# Generated by Django 4.2.1 on 2023-06-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_post_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cources',
            name='img1',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='cources',
            name='img2',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='cources',
            name='img3',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='cources',
            name='img4',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='cources',
            name='img5',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(upload_to=''),
        ),
    ]
