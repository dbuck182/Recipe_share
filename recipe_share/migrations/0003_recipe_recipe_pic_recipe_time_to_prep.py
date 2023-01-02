# Generated by Django 4.1.4 on 2022-12-27 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_share', '0002_rename_post_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_pic',
            field=models.ImageField(default='default_food.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_to_prep',
            field=models.TextField(default='10 minutes', max_length=100),
            preserve_default=False,
        ),
    ]