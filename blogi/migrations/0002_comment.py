# Generated by Django 3.1.dev20191112133759 on 2020-03-22 12:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2020, 3, 22, 12, 58, 13, 662951, tzinfo=utc))),
                ('text', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogi.Post')),
            ],
        ),
    ]
