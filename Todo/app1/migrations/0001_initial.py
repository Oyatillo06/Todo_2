# Generated by Django 4.0.1 on 2022-01-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('vaqt', models.TimeField()),
                ('joy', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=7)),
            ],
        ),
    ]
