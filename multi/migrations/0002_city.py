# Generated by Django 4.1.7 on 2023-03-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]