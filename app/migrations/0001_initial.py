# Generated by Django 3.2 on 2021-10-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.IntegerField(blank=True)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('email_id', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.IntegerField(blank=True)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('email_id', models.CharField(blank=True, max_length=64)),
            ],
        ),
    ]
