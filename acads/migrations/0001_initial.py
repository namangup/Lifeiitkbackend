# Generated by Django 2.2.3 on 2019-07-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcadsModel',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=8)),
            ],
        ),
    ]
