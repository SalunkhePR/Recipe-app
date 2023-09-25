# Generated by Django 4.2.3 on 2023-07-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm', models.CharField(max_length=50)),
                ('info', models.TextField()),
                ('img', models.ImageField(upload_to='Recipe')),
            ],
        ),
    ]
