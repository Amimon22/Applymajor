# Generated by Django 4.2.7 on 2024-01-09 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.BooleanField(default=False)),
                ('delight', models.IntegerField()),
                ('professor1', models.BooleanField(default=False)),
                ('professor2', models.BooleanField(default=False)),
                ('course', models.IntegerField()),
                ('grade', models.FloatField()),
                ('result', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
