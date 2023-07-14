# Generated by Django 4.2.1 on 2023-07-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_cources_img1_alter_cources_img2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(upload_to='')),
                ('name_tital', models.CharField(max_length=100)),
                ('recidence', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
                ('list_profile_1', models.CharField(max_length=100)),
                ('list_profile_2', models.CharField(max_length=100)),
                ('list_profile_3', models.CharField(max_length=100)),
                ('list_profile_4', models.CharField(max_length=100)),
                ('welcoming', models.CharField(max_length=100)),
                ('welcom_name', models.CharField(max_length=100)),
                ('Years_Experience', models.CharField(max_length=100)),
                ('Completed_Projects', models.CharField(max_length=100)),
                ('Happy_Customers', models.CharField(max_length=100)),
                ('Awards', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Price_Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_price_1', models.CharField(max_length=100)),
                ('free_price_2', models.CharField(max_length=100)),
                ('free_price_3', models.CharField(max_length=100)),
                ('free_price_4', models.CharField(max_length=100)),
                ('medium_price_1', models.CharField(max_length=100)),
                ('medium_price_2', models.CharField(max_length=100)),
                ('medium_price_3', models.CharField(max_length=100)),
                ('medium_price_4', models.CharField(max_length=100)),
                ('medium_price_5', models.CharField(max_length=100)),
                ('high_price_1', models.CharField(max_length=100)),
                ('high_price_2', models.CharField(max_length=100)),
                ('high_price_3', models.CharField(max_length=100)),
                ('high_price_4', models.CharField(max_length=100)),
                ('high_price_5', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_tita', models.CharField(max_length=100)),
                ('name_text', models.TextField()),
                ('name_image', models.CharField(max_length=100)),
            ],
        ),
    ]
