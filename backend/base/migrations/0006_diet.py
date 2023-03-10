# Generated by Django 4.0 on 2022-12-21 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0005_workout_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image_s', models.TextField(default='')),
                ('image_l', models.TextField(default='')),
                ('foods', models.ManyToManyField(to='base.Exercise')),
                ('user', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
