# Generated by Django 3.2.1 on 2021-05-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_post_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='book_img',
            field=models.ImageField(upload_to='book_images'),
        ),
    ]
