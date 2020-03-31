# Generated by Django 3.0.1 on 2019-12-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('director_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('code', models.IntegerField()),
            ],
        ),
    ]