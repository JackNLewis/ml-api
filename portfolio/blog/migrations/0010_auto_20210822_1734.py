# Generated by Django 3.2.5 on 2021-08-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='catagory',
            field=models.CharField(choices=[('AI', 'Artificial Intelligence'), ('WB', 'Web Development')], default='WB', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]