# Generated by Django 4.0 on 2022-12-21 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_diet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='foods',
            field=models.ManyToManyField(to='base.Food'),
        ),
    ]
