# Generated by Django 3.2 on 2021-05-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('tole', models.TextField()),
                ('phone', models.IntegerField()),
                ('time', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
    ]
