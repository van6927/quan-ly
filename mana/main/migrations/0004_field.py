# Generated by Django 5.0.1 on 2024-01-15 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('field', models.CharField(max_length=200)),
            ],
        ),
    ]