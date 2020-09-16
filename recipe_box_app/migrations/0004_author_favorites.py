# Generated by Django 3.1 on 2020-09-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_box_app', '0003_author_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to='recipe_box_app.Recipe'),
        ),
    ]