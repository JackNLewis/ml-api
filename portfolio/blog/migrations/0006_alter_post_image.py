# Generated by Django 3.2.5 on 2021-08-08 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/media/images/milky-way.jpeg', upload_to='images/'),
        ),
    ]
