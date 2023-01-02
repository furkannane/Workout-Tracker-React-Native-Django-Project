# Generated by Django 4.0 on 2022-12-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_exercise_image_exercise_image_l_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('calorie', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('taste', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('carb', models.IntegerField()),
                ('image_s', models.TextField(default='')),
                ('image_l', models.TextField(default='')),
            ],
        ),
    ]