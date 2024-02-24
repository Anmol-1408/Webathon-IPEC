# Generated by Django 4.2.10 on 2024-02-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
                ('image_id', models.CharField(max_length=255)),
                ('event_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
