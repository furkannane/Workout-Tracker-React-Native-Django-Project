# Generated by Django 4.0 on 2023-01-01 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0007_alter_diet_foods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('day', models.IntegerField()),
                ('performance', models.IntegerField()),
                ('user', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.workout')),
            ],
        ),
    ]
